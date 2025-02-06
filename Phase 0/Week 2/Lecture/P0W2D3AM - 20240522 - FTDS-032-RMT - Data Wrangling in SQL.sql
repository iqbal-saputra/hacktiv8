-- Melihat data di table crunchbase_companies
SELECT *
FROM crunchbase_companies_clean_data;

-- Melihat kolom founded_at
SELECT name, founded_at
FROM crunchbase_companies_clean_data;

-- Mengurutkan berdasarkan founded_at
SELECT name, founded_at
FROM crunchbase_companies_clean_data
ORDER BY founded_at ASC;

-- Convert format datetime (tahun-bulan-tanggal)
UPDATE crunchbase_companies_clean_data
SET founded_at = TO_DATE(founded_at, 'MM/DD/YY');

ALTER TABLE crunchbase_companies_clean_data
ALTER COLUMN founded_at TYPE DATE USING founded_at::date;

-- Extract masing-masing value dari column founded_at
SELECT
	name,
	founded_at,
	EXTRACT(year from founded_at) as tahun,
	EXTRACT(month from founded_at) as bulan,
	EXTRACT(day from founded_at) as tanggal,
	EXTRACT(quarter from founded_at) as quarter
FROM crunchbase_companies_clean_data;

-- Mencari perusahaan yang didirikan tahun 2010
SELECT * 
FROM 
	(SELECT
		name,
		founded_at,
		EXTRACT(year from founded_at) as tahun,
		EXTRACT(month from founded_at) as bulan,
		EXTRACT(day from founded_at) as tanggal,
		EXTRACT(quarter from founded_at) as quarter
	FROM crunchbase_companies_clean_data) as data_company
WHERE tahun=2010;

-- Mencari tahu waktu saat ini
SELECT 
	CURRENT_DATE as date,
	CURRENT_TIME as time,
	CURRENT_TIMESTAMP as timestamp,
	LOCALTIME as local_time,
	NOW() as now;
	
-- Mencari tahu lama waktu berdirinya perusahaan
SELECT
	name, 
	founded_at,
	CURRENT_DATE as date,
	CURRENT_DATE - founded_at as jangka_waktu_hari,
	(CURRENT_DATE - founded_at)/365 as jangka_waktu_tahun
FROM crunchbase_companies_clean_data;

-- Replace missing values
SELECT founded_at, COALESCE(founded_at, '01-01-1900')
FROM crunchbase_companies_clean_data;

-- Mengekstrak tanggal, waktu, dan menit dari start_time
SELECT
	start_time,
	LEFT(start_time::TEXT, 10) AS tanggal,
	RIGHT(start_time::TEXT, 8) AS waktu,
	SUBSTRING(start_time::TEXT FROM 15 FOR 2) AS menit
FROM dc_bikeshare_q1_2012;

-- Menghapus huruf "M" pada kata MADAM
SELECT
	TRIM(leading 'M' from 'MmMADAM') as result_leading,
	TRIM(trailing 'M' from 'MADAM') as result_trailing,
	TRIM(both 'M' from 'MADAM') as result_both;
	
-- Menghapus karakter "W0" pada column bike_number
SELECT 
	bike_number,
	TRIM(LEADING 'W0' from bike_number) as result_trim,
	length(bike_number) as panjang_awal,
	length(TRIM(LEADING 'W0' from bike_number)) as panjang_after_trim
FROM dc_bikeshare_q1_2012;

-- Uppercase dan lowercase
SELECT 
	name,
	UPPER(name) as capital_letter,
	LOWER(name) as lower_letter
FROM crunchbase_companies_clean_data;

-- Menggabungkan start_station dengan end_station
SELECT
	start_station,
	end_station,
	concat(start_station, ' - ', end_station) as rute
FROM dc_bikeshare_q1_2012;
	
	
	
	

	
	
	
	
