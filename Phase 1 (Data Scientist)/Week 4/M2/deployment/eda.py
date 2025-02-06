import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load data from a CSV file
data = pd.read_csv('shipping.csv')

def eda_page():
    st.title("Exploratory Data Analysis")
    st.write('Eksplorasi data dilakukan untuk memahami lebih baik dataset yang ada')
    st.subheader("Distribusi Pengiriman Tepat Waktu dan Tidak Tepat Waktu")

    # Membuat plot pie untuk pengiriman tepat waktu
    pie_chart_fig, ax = plt.subplots(figsize=(10, 8))

    # Set warna latar belakang plot menjadi gelap
    ax.patch.set_facecolor('#333333')

    # Membuat pie chart
    ax.pie(data['Reached.on.Time_Y.N'].value_counts(), labels=['Tepat Waktu', 'Tidak Tepat Waktu'], 
           explode=[0, 0.1], autopct='%.0f%%', colors=['#007bff', '#ffa07a'])

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(pie_chart_fig)
    st.write("**Deskripsi**:")
    st.write('Berdasarkan gambar di atas, terdapat ketidakseimbangan antara pengiriman yang tepat waktu dan yang tidak tepat waktu. Gambar tersebut menunjukkan bahwa ada 60% pengiriman yang tidak tepat waktu dan hanya ada 40% pengiriman yang tepat waktu.')
    st.write()

    cat_columns = data.select_dtypes(include=['object']).columns

    # Membuat figure dengan ukuran yang ditentukan
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(20, 4))

    # Loop melalui kolom kategori dan membuat countplot untuk masing-masing
    for i, col in enumerate(cat_columns[:4]):
        sns.countplot(data=data, x=col, hue='Reached.on.Time_Y.N', palette='pastel', ax=axs[i])

    # Menampilkan boxplot menggunakan Streamlit
    st.pyplot(fig)
    st.write("""**Penjelasan**  \n* warehouse_block: Pada blok F banyak pengiriman tidak tepat waktu\n* mode_of_shipment: Pada pengiriman dengan kapal banyak yang tidak tepat waktu\n* product_importance: Pada kategori 'low' banyak yang tidak tepat waktu\n* gender: Pada kedua gender banyak yang tidak tepat waktu""")

    cols = data.select_dtypes(include=['int64']).columns

    num_rows = 3
    num_cols = 2

    fig = plt.figure(figsize=(20, 20))

    for index in range(1, num_rows * num_cols):
        fig.add_subplot(num_rows, num_cols, index)
        sns.boxplot(data=data, y=cols[index-1])

    st.pyplot(fig)
    st.write("**Penjelasan**:")
    st.write("""Dari kolom numerikal ditemukan: 
- Banyak data **outliers** yang harus ditangani.""")

    # Membuat histogram dari data kategori
    fig = plt.figure(figsize=(20, 20))
    sns.countplot(data=data, x="Mode_of_Shipment")
    plt.title("Jenis Pengiriman (Paling Banyak Digunakan)")
    st.pyplot(fig)
    st.write("**Penjelasan**:")
    st.write("""* Mode_of_Shipment: Ditemukan banyak yang menggunakan pengiriman dengan kapal""")

    # Mengelompokkan data berdasarkan mode pengiriman dan biaya produk
    grouped = data.groupby(["Mode_of_Shipment", "Product_importance"])["Cost_of_the_Product"].sum().unstack()

    # Membuat bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)
    ax.set_title("Mode Pengiriman vs Biaya Produk")

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    # Mengelompokkan data berdasarkan mode pengiriman dan berat produk
    grouped = data.groupby(["Mode_of_Shipment", "Product_importance"])["Weight_in_gms"].sum().unstack()

    # Membuat bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)
    ax.set_title("Mode Pengiriman vs Berat Produk")

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    # Mengelompokkan data berdasarkan mode pengiriman dan diskon yang ditawarkan
    grouped = data.groupby(["Mode_of_Shipment", "Product_importance"])["Discount_offered"].sum().unstack()

    # Membuat bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped.plot(kind="bar", ax=ax)
    ax.set_title("Mode Pengiriman vs Diskon yang Ditawarkan")

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    st.write("**Penjelasan**:")
    st.write('Untuk pengiriman dengan kapal, diskon yang ditawarkan lebih banyak. Selain itu, karena biaya dan berat produk, semakin banyak orang yang memilih kapal.')
