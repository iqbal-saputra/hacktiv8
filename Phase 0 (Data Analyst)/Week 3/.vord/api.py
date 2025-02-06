from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_no_outliers = pd.read_csv('iqbal.csv')

@app.get("/data")
def get_data():
    return df_no_outliers.to_dict(orient="records")
