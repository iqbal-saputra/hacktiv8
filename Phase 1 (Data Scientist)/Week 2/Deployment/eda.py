import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
    #membuat judul
    st.title('FIFA 2022 Player Rating Prediction')

    #membuat sub header
    st.subheader('EDA untuk Analisa Dataset FIFA 2022')

    #tambahkan gambar
    image = Image.open('gambar_bola.jpg')
    st.image(image, caption = 'FIFA 2022')

    #menambahkan deskripsi
    st.write('Page ini dibuat oleh Hana')

    #font size
    #font terbesar
    st.write('# Halo')
    st.write('## Halo')
    #bold
    st.write('**Tes**')
    #italic
    st.write('*Tes*')

    #mmebuat batas dengan garis lurus
    st.markdown('---')

    #show dataframe
    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/master/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(data)

    #membuat bar plot
    st.write('#### Plot AttackingWorkRate')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='AttackingWorkRate', data = data)
    st.pyplot(fig)

    #membuat histogram
    st.write('#### Histogram of Rating')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data['Overall'], bins = 30, kde = True)
    st.pyplot(fig)

    #membuat histogram berdasarkan input user
    st.write('#### Histogram berdasarkan input user')
    option = st.selectbox('Pilih column : ', ('Age', 'Weight', 'Height', 'ShootingTotal'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[option], bins = 30, kde = True)
    st.pyplot(fig)

    #membuat plotly plot
    #membandingkan ratingpemain bola dengan proce nya
    st.write('#### Plotly plot - ValueEUR vs Overall')
    fig = px.scatter(data, x = 'ValueEUR', y = 'Overall', hover_data = ['Name', 'Age'])
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()
