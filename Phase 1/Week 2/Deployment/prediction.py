import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

#Load All files
#Load model

with open('list_cat_cols.txt', 'r') as file_1:
  list_cat_col = json.load(file_1)

with open('list_num_cols.txt', 'r') as file_2:
  list_num_col = json.load(file_2)

with open('model_encoder.pkl', 'rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('model_scaler.pkl', 'rb') as file_4:
  model_scaler = pickle.load(file_4)

with open('model_lin_reg.pkl', 'rb') as file_5:
  model_lin_reg = pickle.load(file_5)

def run():
    with st.form('form_fifa_2022'):
        #nama, value untuk default value
        name = st.text_input('Name', value = ' ')

        #age, min_value untuk minimum nilai yang bisa diisi, max_value maksimum nilai yang bisa diisi
        age = st.number_input('Age', value = 25, min_value = 15, max_value = 60, help = 'isi dengan usia pemain')

        #height 
        height = st.number_input('Height', value = 170, min_value = 100, help = 'in cm')

        weight = st.slider('Weight', value = 70, min_value = 50, max_value = 150)

        price = st.number_input('Price', value = 0)

        st.markdown('---')
        #index untuk default value di selctbox/radio button
        attacking_work_rate = st.selectbox('Attacking Work Rate', ('Low', 'Medium', 'High'), index = 1)

        defensive_work_rate = st.radio('Defensive Work Rate', ('Low', 'Medium', 'High'), index = 1)

        pace = st.number_input('Pace', min_value = 0, max_value = 100, value = 50)
        shooting = st.number_input('Shooting Score', min_value = 0, max_value = 100, value = 50)
        passing = st.number_input('Passing Score', min_value = 0, max_value = 100, value = 50)
        dribbling = st.number_input('Dribbling Score', min_value = 0, max_value = 100, value = 50)
        defending = st.number_input('Defending Score', min_value = 0, max_value = 100, value = 50)
        physicality = st.number_input('Pysicality Score', min_value = 0, max_value = 100, value = 50)

        #bikin submit button form
        submitted = st.form_submit_button('Predict')

    data_inf = {
       'Name' : name,
       'Age' : age,
       'Height' : height,
       'Weight' : weight,
       'Price' : price,
       'AttackingWorkRate' : attacking_work_rate,
       'DefensiveWorkRate' : defensive_work_rate,
       'PaceTotal' : pace,
       'ShootingTotal' : shooting,
       'PassingTotal' : passing,
       'DribblingTotal' : dribbling,
       'DefendingTotal' : defending,
       'PhysicalityTotal' : physicality
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        #split between numerical and categorical columns
        data_inf_num = data_inf[list_num_col]
        data_inf_cat = data_inf[list_cat_col]

        #feature scaling and encoding

        data_inf_num_scaled = model_scaler.transform(data_inf_num)
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis = 1)

        #predict using linear reg model

        y_pred_inf = model_lin_reg.predict(data_inf_final)

        st.write('## Rating : ', str(int(y_pred_inf)))


if __name__ == '__main__':
   run()


