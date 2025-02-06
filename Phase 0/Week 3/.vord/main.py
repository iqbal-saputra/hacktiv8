from fastapi import FastAPI, HTTPException, Header
import pandas as pd

# membuat object 
app = FastAPI()

# password api key
API_KEY = "secret123$"
# sumber data
df = pd.read_csv('dataset.csv')

# define url
# alamat halaman utama (home)

@app.get("/")

def getHome():
    return{
        "message":"hello from API",
        "numbers": [1,2,3,4,5],
        "location": "Jakarta"
    }
    
@app.get("/data")

def getData(api_key:str = Header(None)):
    if api_key != API_KEY or api_key == None:
        # error handling
        raise HTTPException(401,detail="Authentication error")
    # cek apakah api_key ada isinya dan sama dengan var API_KEY
    return df.to_dict(orient='records')

# alamt untuk mengambil data specific (misal: berdasarkan lokasi)
# 127.0.0.1:8000/data/jakarta -> output user yang asalnya jakarta
# 127.0.0.1:8000/data/semarang -> output user yang asalnya semarang
@app.get("/data/{location}")

def getUserByLocation(location):
    # filter data
    filter = df[df['location'] == location]
    
    # cek apakah hasil filter == None?
    if len(filter) == 0:
        # error handling
        raise HTTPException(404, detail="data tidak ditemukan")
    
    return filter.to_dict(orient='records')

# uvicorn main:app --reload