import streamlit as st
import numpy as np
import pandas as pd
import joblib

def model_page():
    st.title("Prediksi Ketepatan Waktu Pengiriman")
    st.write("")
    st.sidebar.header('Input Fitur Pengguna')

    input_data = user_input()

    st.subheader('Input Pengguna')
    st.write(input_data)

    load_model = joblib.load("best_model_pipeline.joblib")

    prediction = load_model.predict(input_data)

    if prediction == 1:
        prediction = 'Tepat Waktu'
    else:
        prediction = 'Tidak Tepat Waktu'

    st.write('Berdasarkan input pengguna, model memprediksi:')
    st.write(prediction)

def user_input(num_rows=1):
    Customer_care_calls = st.sidebar.number_input('Jumlah Panggilan Customer Care', 2, 7)
    Cost_of_the_Product = st.sidebar.number_input('Biaya Produk', 96, 310)
    Prior_purchases = st.sidebar.number_input('Pembelian Sebelumnya', 2, 5)
    Discount_offered = st.sidebar.number_input('Diskon yang Ditawarkan', 1, 19)
    Weight_in_gms = st.sidebar.number_input('Berat dalam Gram', 1492, 5017)
    Product_importance = st.sidebar.selectbox('Pentingnya Produk', ['low', 'high', 'medium'])
        
    data = {
        'Customer_care_calls': Customer_care_calls,
        'Cost_of_the_Product': Cost_of_the_Product,
        'Prior_purchases': Prior_purchases,
        'Discount_offered': Discount_offered,
        'Weight_in_gms': Weight_in_gms,
        'Product_importance': Product_importance,
        }
    features = pd.DataFrame(data, index=[0])
    return features

