import streamlit as st
import numpy as np
import pandas as pd
import joblib

from eda import eda_page
from prediction import model_page

#Load data
data = pd.read_csv("P1G5_Set_1_iqbal_saputra.csv")

st.header('GC 5')
st.write("""
Created by Iqbal Saputra - RMT032 """)

st.write('Program ini dibuat untuk memprediksi default payment next month berdasarkan fitur-fitur yang terdapat dari dataset ml_datasets dari database credit_card_default pada public data bigquery')
st.write('default payment next month data')
data

def main():
    # Define menu options
    menu_options = ["eda", "model"]

    # Create sidebar menu
    selected_option = st.sidebar.radio("Menu", menu_options)

    # Display selected page
    if selected_option == "eda":
        eda_page()
    elif selected_option == "model":
        model_page()


if __name__ == "__main__":
    main()