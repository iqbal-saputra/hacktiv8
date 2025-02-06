-- Buat database jika belum ada
CREATE DATABASE marketing_campaign;

-- TCL
BEGIN;

-- Buat tabel untuk menyimpan data
CREATE TABLE marketing_data (
    ID INT PRIMARY KEY,
    Year_Birth INT,
    Education VARCHAR(50),
    Marital_Status VARCHAR(50),
    Income FLOAT,
    Kidhome INT,
    Teenhome INT,
    Dt_Customer DATE,
    Recency INT,
    MntWines FLOAT,
    MntFruits FLOAT,
    MntMeatProducts FLOAT,
    MntFishProducts FLOAT,
    MntSweetProducts FLOAT,
    MntGoldProds FLOAT,
    NumDealsPurchases INT,
    NumWebPurchases INT,
    NumCatalogPurchases INT,
    NumStorePurchases INT,
    NumWebVisitsMonth INT,
    AcceptedCmp3 INT,
    AcceptedCmp4 INT,
    AcceptedCmp5 INT,
    AcceptedCmp1 INT,
    AcceptedCmp2 INT,
    Response INT,
    Complain INT,
    Country VARCHAR(50)
);

-- Load data dari CSV ke tabel (Uncleaned data)
COPY marketing_data (ID, Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome, Dt_Customer, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1, AcceptedCmp2, Response, Complain, Country)
FROM 'C:/tmp/marketing_data.csv' 
DELIMITER ',' 
CSV HEADER
NULL AS ''
QUOTE '"'
ESCAPE '\';

SELECT *
FROM marketing_data

COMMIT;

-- TCL
BEGIN;

-- Buat tabel untuk menyimpan data
CREATE TABLE marketing_data_clean (
    ID INT PRIMARY KEY,
    EDUCATION VARCHAR(50),
    MARITAL_STATUS VARCHAR(50),
    AGE INT,
    TOTAL_CHILDREN INT,
    INCOME FLOAT,
    TOTAL_SPENDING FLOAT,
    COUNTRY VARCHAR(50),
    DATE_ENROLLED DATE,
    RECENCY INT,
    AMOUNT_WINES FLOAT,
    AMOUNT_FRUITS FLOAT,
    AMOUNT_MEAT FLOAT,
    AMOUNT_FISH FLOAT,
    AMOUNT_SWEET FLOAT,
    AMOUNT_GOLD FLOAT,
    DISC_PURCHASE INT,
    WEB_PURCHASE INT,
    CATALOG_PURCHASE INT,
    STORE_PURCHASE INT,
    WEBVISIT INT,
    CMP1 INT,
    CMP2 INT,
    CMP3 INT,
    CMP4 INT,
    CMP5 INT,
    RESPONSE INT,
    COMPLAIN INT
);

-- Load data dari CSV ke tabel
COPY marketing_data_clean (
    ID, EDUCATION, MARITAL_STATUS, AGE, TOTAL_CHILDREN, INCOME, TOTAL_SPENDING,
    COUNTRY, DATE_ENROLLED, RECENCY, AMOUNT_WINES, AMOUNT_FRUITS, AMOUNT_MEAT,
    AMOUNT_FISH, AMOUNT_SWEET, AMOUNT_GOLD, DISC_PURCHASE, WEB_PURCHASE,
    CATALOG_PURCHASE, STORE_PURCHASE, WEBVISIT, CMP1, CMP2, CMP3, CMP4, CMP5,
    RESPONSE, COMPLAIN
)
FROM 'C:/tmp/marketing_data_clean.csv' 
DELIMITER ',' 
CSV HEADER
NULL AS ''
QUOTE '"'
ESCAPE '\';

-- Tampilkan data untuk verifikasi
SELECT *
FROM marketing_data_clean;

COMMIT;

