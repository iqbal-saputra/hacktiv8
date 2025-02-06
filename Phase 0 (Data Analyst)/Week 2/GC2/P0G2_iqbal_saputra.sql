-- Muhammad Iqbal Saputra | RMT-032


-- 4. Relational Database & SQL

-- 4.1
-- Membuat DATABASE

-- CREATE DATABASE gc2;

-- 4.2 
-- (TCL) 
BEGIN;

-- (DDL)
-- Membuat table segment
CREATE TABLE Segment (
    segment_id SERIAL PRIMARY KEY,
    segment VARCHAR(255) NOT NULL
);

-- Membuat table country
CREATE TABLE Country (
    country_id SERIAL PRIMARY KEY,
    country VARCHAR(255) NOT NULL
);

-- Membuat table product
CREATE TABLE Product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    manufacturing_price FLOAT NOT NULL
);

-- Membuat table discount
CREATE TABLE Discount (
    discount_id SERIAL PRIMARY KEY,
    discount_band VARCHAR(255) NOT NULL
);

-- Membuat table sales
CREATE TABLE Sales (
    ID SERIAL PRIMARY KEY,
    segment_id INT REFERENCES Segment(segment_id),
    country_id INT REFERENCES Country(country_id),
    product_id INT REFERENCES Product(product_id),
    discount_id INT REFERENCES Discount(discount_id),
    units_sold FLOAT NOT NULL,
    gross_sales FLOAT NOT NULL,
    sales FLOAT NOT NULL,
    cogs FLOAT NOT NULL,
    profit FLOAT NOT NULL,
    date DATE NOT NULL
);

-- (DML)
-- Impor data segment dari segment_table.csv
COPY Segment(segment_id, segment)
FROM 'C:\tmp\segment_table.csv'
DELIMITER ','
CSV HEADER;

-- Impor data segment dari country_table.csv
COPY Country(country_id, country)
FROM 'C:\tmp\country_table.csv'
DELIMITER ','
CSV HEADER;

-- Impor data segment dari product_table.csv
COPY Product(product_id, product_name, manufacturing_price)
FROM 'C:\tmp\product_table.csv'
DELIMITER ','
CSV HEADER;

-- Impor data segment dari discount_table.csv
COPY Discount(discount_id, discount_band)
FROM 'C:\tmp\discount_table.csv'
DELIMITER ','
CSV HEADER;

-- Impor data segment dari sales_table.csv
COPY Sales(ID, segment_id, country_id, product_id, discount_id, units_sold, gross_sales, sales, cogs, profit, date)
FROM 'C:\tmp\sales_table.csv'
DELIMITER ','
CSV HEADER;

-- (DCL)
-- Pembuatan 2 user
CREATE USER admin_user WITH PASSWORD 'admin_password';
CREATE USER read_user WITH PASSWORD 'read_password';

-- Memberikan akses penuh ke database gc2
GRANT ALL PRIVILEGES ON DATABASE gc2 TO admin_user;

-- Memberikan akses untuk menggunakan schema public
GRANT USAGE ON SCHEMA public TO read_user;

-- Memberikan akses SELECT pada semua tabel di schema public
GRANT SELECT ON ALL TABLES IN SCHEMA public TO read_user;

-- Membatasi akses write (INSERT, UPDATE, DELETE, TRUNCATE) pada semua tabel di schema public
REVOKE INSERT, UPDATE, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA public FROM read_user;


-- 5. Pengujian Database

--5.1.a
CREATE TABLE segment_profit AS
SELECT Segment.segment, SUM(Sales.profit) AS total_profit
FROM Sales
JOIN Segment ON Sales.segment_id = Segment.segment_id
JOIN Discount ON Sales.discount_id = Discount.discount_id
WHERE Discount.discount_id = 1
GROUP BY Segment.segment
ORDER BY total_profit DESC;

SELECT *
FROM segment_profit
ORDER BY Total_profit DESC

--5.1.b
CREATE TABLE statistics_summary AS
SELECT Country.country, 
       AVG(Sales.sales) AS average_sales, 
       MIN(Sales.sales) AS min_sales, 
       MAX(Sales.sales) AS max_sales
FROM Sales
JOIN Country ON Sales.country_id = Country.country_id
GROUP BY Country.country;

SELECT * 
FROM statistics_summary
ORDER BY average_sales DESC

-- (TCL)
COMMIT;



