import streamlit as st
import numpy as np
import pandas as pd
import joblib

def model_page():
    st.title("Model Prediksi default_payment_next_month")
    st.write("Memprediksi apakah pada bulan depan nasabah default pembayaran atau tidak")
    st.sidebar.header('User Input Features')

    input_data = user_input()

    st.subheader('User Input')
    st.write(input_data)

    load_model = joblib.load("KNN_best.pkl")

    prediction = load_model.predict(input_data)

    if prediction == 1:
        prediction = 'default payment next month'
    else:
        prediction = 'not defaulting'

    st.write('Based on user input, the placement model predicted: ')
    st.write(prediction)

def user_input(num_rows=1):
    education_level = st.sidebar.selectbox('Education Level', [1, 2, 3, 4])
    pay_0 = st.sidebar.number_input('Pay_0', -2, 8, 0)
    pay_2 = st.sidebar.number_input('Pay_2', -2, 8, 0)
    pay_3 = st.sidebar.number_input('Pay_3', -2, 8, 0)
    pay_4 = st.sidebar.number_input('Pay_4', -2, 8, 0)
    pay_5 = st.sidebar.number_input('Pay_5', -2, 8, 0)
    pay_6 = st.sidebar.number_input('Pay_6', -2, 8, 0)
    pay_amt_1 = st.sidebar.number_input('Pay_amt_1', 0, 30000, 0)
    pay_amt_2 = st.sidebar.number_input('Pay_amt_2', 0, 30000, 0)
    pay_amt_3 = st.sidebar.number_input('Pay_amt_3', 0, 30000, 0)
    pay_amt_4 = st.sidebar.number_input('Pay_amt_4', 0, 30000, 0)
    pay_amt_5 = st.sidebar.number_input('Pay_amt_5', 0, 30000, 0)
    pay_amt_6 = st.sidebar.number_input('Pay_amt_6', 0, 30000, 0)

    data = {
        'limit_balance': np.random.randint(5000, 100000, num_rows),
        'education_level': education_level,
        'pay_0': pay_0,
        'pay_2': pay_2,
        'pay_3': pay_3,
        'pay_4': pay_4,
        'pay_5': pay_5,
        'pay_6': pay_6,
        'pay_amt_1': pay_amt_1,
        'pay_amt_2': pay_amt_2,
        'pay_amt_3': pay_amt_3,
        'pay_amt_4': pay_amt_4,
        'pay_amt_5': pay_amt_5,
        'pay_amt_6': pay_amt_6}
    features = pd.DataFrame(data, index=[0])
    return features