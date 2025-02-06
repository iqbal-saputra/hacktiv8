import datetime as dt
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.utils.dates import days_ago
import pandas as pd
import psycopg2 as db
import logging
from elasticsearch import Elasticsearch
import os
import re

'''
=================================================
Milestone 3

Nama  : Muhammad Iqbal Saputra
Batch : RMT-032

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch.
=================================================
'''

# Step 1: Fetch data from PostgreSQL
def fetch_from_postgresql():
    '''
    Fungsi ini ditujukan untuk mengambil data dari PostgreSQL dan menyimpannya ke file CSV.

    Koneksi ke database PostgreSQL dibuat menggunakan parameter yang telah ditentukan.
    Data diambil dari tabel 'table_m3' dan disimpan ke file CSV.

    Returns:
    None

    Output:
    File CSV 'P2M3_iqbal_saputra_data_raw.csv' di direktori '/opt/airflow/dags/'

    Contoh penggunaan:
    fetch_from_postgresql()
    '''
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow' port='5432'"
    conn = db.connect(conn_string)
    df = pd.read_sql("SELECT * FROM table_m3", conn)
    df.to_csv('/opt/airflow/dags/P2M3_iqbal_saputra_data_raw.csv', sep=',', index=False)
    conn.close()

# Step 2: Clean data
def clean_data():
    '''
    Fungsi ini melakukan pembersihan data pada file CSV yang dihasilkan dari fungsi fetch_from_postgresql.

    Proses pembersihan meliputi:
    1. Menghapus data duplikat
    2. Menangani missing values
    3. Mengubah format kolom 'model_year'
    4. Ekstraksi latitude dan longitude dari 'vehicle_location'
    5. Membuat field 'location' sebagai geo_point

    Returns:
    None

    Output:
    File CSV 'P2M3_iqbal_saputra_data_clean.csv' di direktori '/opt/airflow/dags/'

    Contoh penggunaan:
    clean_data()
    '''
    logging.info("Cleaning data")
    df = pd.read_csv('/opt/airflow/dags/P2M3_iqbal_saputra_data_raw.csv')
    
    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    numeric_columns = ['postal_code', 'model_year', 'electric_range', 'base_msrp', 'legislative_district', 'dol_vehicle_id', 'census_tract_2020']
    for col in numeric_columns:
        df[col].fillna(df[col].median(), inplace=True)
    
    df.fillna('Unknown', inplace=True)
    
    df['model_year'] = pd.to_datetime(df['model_year'], format='%Y')

    # Extract latitude and longitude from vehicle_location
    def extract_lat_long(location):
        if isinstance(location, str):
            match = re.findall(r"-?\d+\.\d+", location)
            if len(match) == 2:
                return float(match[1]), float(match[0])
        return None, None

    df['latitude'], df['longitude'] = zip(*df['vehicle_location'].apply(extract_lat_long))

    # Create location field as geo_point
    df['location'] = df.apply(lambda row: {'lat': row['latitude'], 'lon': row['longitude']}, axis=1)

    # Save cleaned data
    df.to_csv('/opt/airflow/dags/P2M3_iqbal_saputra_data_clean.csv', index=False)
    logging.info("Data cleaned and saved to CSV")

# Step 3: Post to Elasticsearch
def post_to_elasticsearch():
    '''
    Fungsi ini mengambil data dari file CSV yang telah dibersihkan dan mengunggahnya ke Elasticsearch.

    Proses meliputi:
    1. Membaca file CSV hasil pembersihan
    2. Mengubah setiap baris data menjadi dokumen Elasticsearch
    3. Mengunggah setiap dokumen ke indeks 'electric_vehicles' di Elasticsearch

    Returns:
    None

    Contoh penggunaan:
    post_to_elasticsearch()
    '''
    logging.info("Posting data to Elasticsearch")
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    df = pd.read_csv('/opt/airflow/dags/P2M3_iqbal_saputra_data_clean.csv')
    
    for i, row in df.iterrows():
        doc = row.to_dict()
        doc['location'] = {
            "lat": row['latitude'],
            "lon": row['longitude']
        }
        try:
            es.index(index='electric_vehicles', doc_type='_doc', id=i, body=doc)
        except Exception as e:
            logging.error(f"Failed to index document {i}: {e}")
            logging.error(f"Document content: {doc}")
    logging.info("Data posted to Elasticsearch")

# Default arguments
default_args = {
    'owner': 'iqbal',
    'start_date': dt.datetime(2024, 7, 21, 10, 40, 0) - dt.timedelta(hours=7),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

# Define the DAG
with DAG(
    'P2M3_iqbal_saputra_DAG',
    default_args=default_args,
    description='Fetch from PostgreSQL, clean data, and post to Elasticsearch',
    schedule_interval='30 6 * * *',  # Set to run every day at 06:30
) as dag:
    
    fetch_data_task = PythonOperator(task_id='fetch_from_postgresql',
                                     python_callable=fetch_from_postgresql)
    
    clean_data_task = PythonOperator(task_id='clean_data', 
                                     python_callable=clean_data)
    
    post_to_es_task = PythonOperator(task_id='post_to_elasticsearch',
                                     python_callable=post_to_elasticsearch)

# Define task dependencies
fetch_data_task >> clean_data_task >> post_to_es_task
