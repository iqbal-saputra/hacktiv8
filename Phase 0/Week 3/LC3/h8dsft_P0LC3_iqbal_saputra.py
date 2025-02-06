'''
==============================

Nama: Muhammad Iqbal Saputra

Batch: RMT-032

Objektif dari program ini adalah:
- Membuat API sederhana untuk menampilkan dataset

==============================
'''

from fastapi import FastAPI, HTTPException, Header
import pandas as pd

app = FastAPI()

# sumber data
df = pd.read_csv('h8dsft_P0LC3_iqbal_saputra.csv')

# alamat halaman utama (home)
@app.get("/")

def getHome():
    return df.to_json(orient = "records")

# commend utk menjalankan diterminal
# uvicorn h8dsft_P0LC3_iqbal_saputra:app --reload