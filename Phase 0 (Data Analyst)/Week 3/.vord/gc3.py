# %% [markdown]
# #
# <b>
# 
# ==============================
# 
# Nama: Muhammad Iqbal Saputra
# 
# Batch: RMT-032
# 
# Objektif dari program ini adalah:
# 
# 
# ==============================
# 

# %%
# import module-module yang diperlukan
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from bs4 import BeautifulSoup
import scipy.stats as stats

# %% [markdown]
# # A. Web Scraping

# %%
# inisialisasi dataframe
nama_produk = []
harga_produk = []
nama_toko = []
lokasi_toko = []
banyak_terjual = []
rating_produk = []


# %%
# membuat intance webdriver
driver = webdriver.Chrome()

# melakukan perulangan untuk 10 halaman
for i in range(10):
    url = f"https://www.tokopedia.com/search?navsource=&page={i}&q=seblak&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st="
    driver.get(url)
    time.sleep(1)

    # melakukan scrolling ke bawah
    for i in range(50):
        driver.execute_script("window.scroll(0,500)")
        time.sleep(1)

    # mengambil HTML source
    html = driver.page_source

    # membuat objek BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # menghindari elemen iklan
    iklan = soup.select(".css-1nod7cp:not(.css-1asz3by)")

    # melakukan perulangan untuk setiap elemen
    for i in iklan:
        # menghapus elemen dari HTML source
        i.extract()

    # mencari elemen dengan class 'css-1asz3by'
    boxes = soup.find_all('div', {"class": "css-1asz3by"})

    # melakukan perulangan untuk setiap kotak produk
    for box in boxes:
        # nama produk
        try:
            nama_produk_element = box.find('div', {"class": "prd_link-product-name css-3um8ox"})
            nama_produk.append(nama_produk_element.get_text())
        except:
            nama_produk.append(None)
            
        # harga produk
        try:
            harga_produk_element = box.find('div', {"class": "prd_link-product-price css-h66vau"})
            harga_produk.append(harga_produk_element.get_text())
        except:
            harga_produk.append(None)
            
        # nama toko
        try:
            shop_name_element = box.find('span', {'class': 'prd_link-shop-name css-1kdc32b flip'})
            nama_toko.append(shop_name_element.get_text())
        except:
            nama_toko.append(None)

        # lokasi toko
        try:
            shop_location_element = box.find('span', {'class': 'prd_link-shop-loc css-1kdc32b flip'})
            lokasi_toko.append(shop_location_element.get_text())
        except:
            lokasi_toko.append(None)

        # banyak terjual
        try:
            sold_element_list = box.find_all('span', {"class": "prd_label-integrity css-1sgek4h"})
            for sold_element in sold_element_list:
                banyak_terjual.append(sold_element.get_text())
        except:
            banyak_terjual.append(None)
            
        # rating produk
        try:
            rating_element_list = box.find_all('span', {"class": "prd_rating-average-text css-t70v7i"})
            for rating_element in rating_element_list:
                rating_produk.append(rating_element.get_text())
        except:
            rating_produk.append(None)
            

# inisialisasi data frame
df = pd.DataFrame()

# memastikan semua panjang data sama
common_length = min(len(nama_produk), len(harga_produk), len(rating_produk), len(banyak_terjual), len(lokasi_toko), len(nama_toko))

# menambahkan data ke data frame
df['nama produk'] = nama_produk[:common_length]
df['harga produk'] = harga_produk[:common_length]
df['nama toko'] = nama_toko[:common_length]
df['lokasi toko'] = lokasi_toko[:common_length]
df['banyak terjual'] = banyak_terjual[:common_length]
df['rating produk'] = rating_produk[:common_length]

# mematikan driver
driver.quit()

# %%
# menampilkan data frame 5 teratas (memastikan apakah webscraping kita berhasil)
df.head()

# %%
# menampilkan info data frame (memastikan apakah webscraping kita berhasil)
df.info()

# %%
# import dataframe ke csv
df.to_csv('seblak_produk.csv', index=False)

# %% [markdown]
# # B. Data Preparation

# %%
# membaca file CSV (data hasil scraping)
data_explore = pd.read_csv('seblak_produk.csv')

# %%
# menampilkan 5 data teratas dari data_explore
data_explore.head(5)

# %%
# menampilkan 5 data terbawah dari data_explore
data_explore.tail(5)

# %% [markdown]
# sekilas setelah melihat data, format harga produk dan banyak terjual masih belum menjadi format yang benar. semestinya format kolom tersebut int/float agar mudah di olah
# 

# %%
# menampilkan informasi tentang data yang baru saja diimport dari file seblak_produk.csv
data_explore.info()

# %%
# menampilkan statistik data numerik dari data_explore
data_explore.describe()

# %% [markdown]
# dikarnakan data yang bertipe numerik hanya rating produk, hasil dari data_explore.describe() hanya hasil dari kolom rating produk, yang berarti data_explore belum bersih

# %%
# cek missing value dari setiap kolom
data_explore.isnull().sum()

# %% [markdown]
# tidak ditemukan missing value

# %%
# incase terdapat missing value, kode ini akan menghilangkan baris yang memiliki missing value
data_explore.dropna(subset=['rating produk'], inplace=True)
data_explore.dropna(subset=['banyak terjual'], inplace=True)

# %%
# cek dan menampilkan jika ada baris yang duplikat
data_explore.duplicated().sum()

# %% [markdown]
# terdapat banyak baris yang terduplikat

# %%
# menampilkan baris yang duplikat
data_explore[data_explore.duplicated()]


# %%
# menyimpan data tanpa duplikat 
data_explore_no_duplicates = data_explore.drop_duplicates()

# deep copy data agar ketika melakukan proses cleaning, tidak merubah data_explore
data_explore_no_duplicates = data_explore_no_duplicates.copy(deep=True)

# %%
# menampilkan informasi tentang data yang sudah bersih dari duplikat
data_explore_no_duplicates.info()

# %%
# double cek missing value dari data yang sudah bersih dari duplikat
data_explore_no_duplicates.isnull().sum()

# %%
# double cek incase terdapat missing value, 
# kode ini akan menghilangkan baris yang memiliki missing value
data_explore_no_duplicates.dropna(subset=['rating produk'], inplace=True)
data_explore_no_duplicates.dropna(subset=['banyak terjual'], inplace=True)

# %%
# menghapus "Rp" dari kolom "harga produk" dan merubah tipe data menjadi float
data_explore_no_duplicates['harga produk'] = data_explore_no_duplicates['harga produk'].str.replace('Rp', '').str.replace('.','').astype(float)

# %%
# menghapus karakter '+' dan 'terjual' pada kolom 'banyak terjual'
data_explore_no_duplicates['banyak terjual'] = data_explore_no_duplicates['banyak terjual'].str.replace('+', '').str.replace(' terjual', '')
# menganti 'rb+' menjadi '000'
data_explore_no_duplicates['banyak terjual'] = data_explore_no_duplicates['banyak terjual'].replace({'rb+': '000'}, regex=True).replace('[^\d\.]', '', regex=True).astype(int)
# mengubah tipe data pada kolom 'banyak terjual' menjadi numerik
data_explore_no_duplicates['banyak terjual'] = pd.to_numeric(data_explore_no_duplicates['banyak terjual'], errors='coerce')

# %%
# menampilkan data teratas yang sudah kita bersihkan (memastikan proses cleaning berhasil)
data_explore_no_duplicates.head()

# %%
# menampilkan informasi data yang sudah kita bersihkan (memastikan proses cleaning berhasil)
data_explore_no_duplicates.info()

# %%
# menampilkan statistik data yang berupa numerik
data_explore_no_duplicates.describe()

# %%
# export data yang sudah dibersihkan ke csv 
data_explore_no_duplicates.to_csv('data_clean.csv')

# %% [markdown]
# # C. Business Understanding/Problem Statement

# %% [markdown]
# ## **SMART Framework**
# 
# > Specific      : Menganalisis faktor-faktor yang mempengaruhi penjualan produk seblak di Tokopedia yang bertujuan utk meningkatkan penjualan.
# 
# > Measureable   : Diukur dari peningkatan jumlah konversi penjualan dan rating produk sebelum dan sesudah mengimplementasikan strategi, target terukur meningkatkan penjualan sebesar 15% dari serta meningkatkan skor rating minimal 0.5.
# 
# > Achieveable   : Menggunakan analisis data untuk menentukan harga jual yang optimal terhadap potensi pasar yang mempertimbangkan metriks-metriks penjualan seperti lokasi toko, harga produk, rating produk dan lain sebagainya.
# 
# > Relevant      : Mengoptimalkan penjualan produk pada platform, dan membantu para penjual/pelaku UMKM membuat keputusan bisnis berdasarkan data.
# 
# > Time-bound    : Proses ini akan dilakukan dalam waktu 6 bulan, termasuk pengumpulan data, analisis, dan implementasi.
# 
# Problem statment 
# ---
# "Dalam waktu 6 bulan, kami akan meningkatkan penjualan produk seblak di Tokopedia sebesar 15% dan skor rating minimal 0.5 dengan menganalisis faktor-faktor kunci seperti lokasi toko, harga produk, dan rating produk, serta menggunakan hasil analisis untuk menentukan harga jual yang optimal dan membuat strategi penjualan yang efektif."

# %% [markdown]
# # D. Analysis

# %%
# import data yang sudah bersih
data_analysis = pd.read_csv('data_clean.csv')

# %%
# make sure data yang ingin kita analisis tipe datanya sudah sesuai
data_analysis.info()

# %% [markdown]
# ## 1. Mean, Median, Standard Deviation, Skewness, Kurtosis

# %%
# menghitung rata-rata, median, standar deviasi, skew, dan kurtosis dari masing-masing kolom

# harga produk 
mean_hp = data_analysis['harga produk'].mean()
median_hp = data_analysis['harga produk'].median()
std_hp = data_analysis['harga produk'].std()
skew_hp = data_analysis['harga produk'].skew()
kurtosis_hp = data_analysis['harga produk'].kurtosis()

# banyak terjual
mean_bt = data_analysis['banyak terjual'].mean()
median_bt = data_analysis['banyak terjual'].median()
std_bt = data_analysis['banyak terjual'].std()
skew_bt = data_analysis['banyak terjual'].skew()
kurtosis_bt = data_analysis['banyak terjual'].kurtosis()

# rating produk
mean_r = data_analysis['rating produk'].mean()
median_r = data_analysis['rating produk'].median()
std_r = data_analysis['rating produk'].std()
skew_r = data_analysis['rating produk'].skew()
kurtosis_r = data_analysis['rating produk'].kurtosis()

# %%
# Menampilkan hasil statistik

print(f"{'harga produk':^30}")
print(f"{'---------':^30}")
print(f"Mean \t\t\t= {mean_hp:.2f}")
print(f"Median \t\t\t= {median_hp:.2f}")
print(f"Standar deviasi \t= {std_hp:.2f}")
print(f"Skewness \t\t= {skew_hp:.2f}")
print(f"Kurtosis \t\t= {kurtosis_hp:.2f}")

print(f"\n{'banyak terjual':^30}")
print(f"{'---------':^30}")
print(f"Mean \t\t\t= {mean_bt:.2f}")
print(f"Median \t\t\t= {median_bt:.2f}")
print(f"Standar deviasi \t= {std_bt:.2f}")
print(f"Skewness \t\t= {skew_bt:.2f}")
print(f"Kurtosis \t\t= {kurtosis_bt:.2f}")

print(f"\n{'rating produk':^30}")
print(f"{'---------':^30}")
print(f"Mean \t\t\t= {mean_r:.2f}")
print(f"Median \t\t\t= {median_r:.2f}")
print(f"Standar deviasi \t= {std_r:.2f}")
print(f"Skewness \t\t= {skew_r:.2f}")
print(f"Kurtosis \t\t= {kurtosis_r:.2f}")
print(f"{'---------':^30}")


# %% [markdown]
# ### **Insight**
# ***'harga produk'***
# - **Mean dan Median**: harga produk rata-rata sekitar Rp21,074.81, tapi harga median lebih rendah yaitu Rp16,990.00. ini menunjukkan bahwa sebagian besar produk memiliki harga yang lebih rendah dari rata-rata, dengan beberapa produk yang memiliki harga sangat tinggi yang meningkatkan rata-rata (mungkin karena beberapa toko menjual dalam jumlah pcs yang berbeda, contoh toko A menjual per 100pcs sedangkan toko B menjual per 10pcs).
# - **Standar Deviasi**: standar deviasi yang tinggi (Rp20,672.20) menunjukkan variasi harga yang sangat besar di antara produk seblak.
# - **Skewness**: skewness yang positif (3.78) menunjukkan distribusi harga yang miring ke kanan, artinya ada beberapa produk dengan harga yang sangat tinggi.
# - **Kurtosis**: kurtosis yang sangat tinggi (20.63) menunjukkan bahwa distribusi harga memiliki banyak outlier atau harga yang ekstrem.
# 
# ***'banyak terjual'***
# - **Mean dan Median**: rata-rata penjualan sekitar 1,154.68 unit, tapi median jauh lebih rendah pada 250 unit. Ini menunjukkan bahwa sebagian besar produk terjual dalam jumlah yang lebih rendah, dengan beberapa produk terjual dalam jumlah sangat besar yang meningkatkan rata-rata.
# - **Standar Deviasi**: standar deviasi yang sangat tinggi (2,461.28 unit) menunjukkan bahwa ada variasi besar dalam jumlah produk yang terjual.
# - **Skewness**: skewness yang positif (2.93) menunjukkan distribusi jumlah terjual yang miring ke kanan, artinya ada beberapa produk yang terjual dalam jumlah sangat besar.
# - **Kurtosis**: kurtosis yang tinggi (7.63) menunjukkan bahwa distribusi jumlah terjual memiliki banyak outlier atau jumlah yang ekstrem.
# 
# ***'rating produk'***
# - **Mean dan Median**: rata-rata rating produk sangat tinggi pada 4.87, dengan median hampir sama yaitu 4.90. Ini menunjukkan bahwa mayoritas produk seblak mendapatkan rating yang sangat baik.
# - **Standar Deviasi**: standar deviasi yang rendah (0.12) menunjukkan bahwa rating produk cukup konsisten dan sebagian besar berada di sekitar rata-rata tinggi.
# - **Skewness**: skewness yang negatif (-2.23) menunjukkan distribusi rating yang miring ke kiri, artinya sebagian besar produk mendapatkan rating yang sangat tinggi.
# - **Kurtosis**: kurtosis yang sangat tinggi (12.00) menunjukkan bahwa distribusi rating memiliki beberapa outlier dengan rating yang ekstrem (mungkin didapat dari produk dengan rating yang sangat rendah).

# %%
# mengplot hasil statistik agar audience lebih mudah melihat data
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(14, 12))

# plot untuk 'harga produk'
data_analysis['harga produk'].plot(kind='hist', bins=20, ax=axes[0, 0], color='skyblue', edgecolor='black')
axes[0, 0].set_title('Histogram Harga Produk')
axes[0, 0].set_xlabel('Harga Produk')
axes[0, 0].set_ylabel('Frekuensi')

data_analysis['harga produk'].plot(kind='box', ax=axes[0, 1], vert=False, patch_artist=True, boxprops=dict(facecolor='skyblue'))
axes[0, 1].set_title('Box Plot Harga Produk')
axes[0, 1].set_xlabel('Harga Produk')

# plot untuk 'banyak terjual'
data_analysis['banyak terjual'].plot(kind='hist', bins=20, ax=axes[1, 0], color='lightgreen', edgecolor='black')
axes[1, 0].set_title('Histogram Banyak Terjual')
axes[1, 0].set_xlabel('Banyak Terjual')
axes[1, 0].set_ylabel('Frekuensi')

data_analysis['banyak terjual'].plot(kind='box', ax=axes[1, 1], vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
axes[1, 1].set_title('Box Plot Banyak Terjual')
axes[1, 1].set_xlabel('Banyak Terjual')

# plot untuk 'rating produk'
data_analysis['rating produk'].plot(kind='hist', bins=20, ax=axes[2, 0], color='lightcoral', edgecolor='black')
axes[2, 0].set_title('Histogram Rating Produk')
axes[2, 0].set_xlabel('Rating Produk')
axes[2, 0].set_ylabel('Frekuensi')

data_analysis['rating produk'].plot(kind='box', ax=axes[2, 1], vert=False, patch_artist=True, boxprops=dict(facecolor='lightcoral'))
axes[2, 1].set_title('Box Plot Rating Produk')
axes[2, 1].set_xlabel('Rating Produk')

plt.tight_layout()
plt.show()


# %% [markdown]
# ## 2. Potensi minimum & maksimum jika menjual produk seblak
# 

# %%
# menghitung pendapatan per bulan
data_analysis['pendapatan'] = data_analysis['harga produk'] * data_analysis['banyak terjual']

# menghitung rata-rata dan standar deviasi dari pendapatan
mean_pendapatan = data_analysis['pendapatan'].mean()
std_pendapatan = data_analysis['pendapatan'].std()

# menghitung confidence level, menggunakan metode z-score
confidence_level = 0.95
z_score = stats.norm.ppf((1 + confidence_level) / 2)

# menghitung margin of error
margin_of_error = z_score * (std_pendapatan / np.sqrt(len(data_analysis['pendapatan'])))

# menghitung confidence interval
lower_bound = mean_pendapatan - margin_of_error
upper_bound = mean_pendapatan + margin_of_error

# hasil
print(f"Rata-rata pendapatan\t\t\t: {mean_pendapatan:.2f}")
print(f"Standar deviasi pendapatan\t\t: {std_pendapatan:.2f}")
print(f"Margin of Error\t\t\t\t: {margin_of_error:.2f}")
print(f"95% Confidence Interval for Pendapatan\t: ({lower_bound:.2f}, {upper_bound:.2f})")


# %% [markdown]
# dari hasil tersebut
# - potensi minimum pendapatan menjual seblak adalah Rp17.629.188/bulan
# - potensi maximum pendapatan menjual seblak adalah Rp34.794.635/bulan

# %%
# memastikan kolom pendapatan sudah berhasil ditambahkan
data_analysis.info()

# %%
# memastikan kolom pendapatan berhasil ditambahkan
data_analysis.head(3)

# %% [markdown]
# ## 3. Perbandingan harga antara Jabodetabek dan di luar Jabodetabek

# %% [markdown]
# <h4> Hipotesis
# 
# - H0: Harga barang di Jabodetabek dan luar Jabodetabek tidak berbeda signifikan
# > μ₁ = μ₂
# - H1 : Harga barang di Jabodetabek dan luar Jabodetabek berbeda signifikan 
# > μ₁ ≠ μ₂
# 
# 

# %%
# cek dimana saja lokasi toko
data_analysis['lokasi toko'].value_counts()

# %%
# membuat list yang berisikan kota-kota Jabodetabek
jabodetabek = ['Jakarta Selatan','Jakarta Timur','Jakarta Pusat','Jakarta Utara','Jakarta Barat ','Tangerang Selatan','Kab. Tangerang','Tangerang','Depok','Kab. Bogor','Bogor']

# membuat kolom baru yang mengklasifikasikan lokasi toko apakah jabodetabek atau bukan
data_analysis['lokasi'] = np.where(data_analysis['lokasi toko'].isin(jabodetabek), 'Jabodetabek', 'Luar Jabodetabek')

# %%
# cek kolom
data_analysis.head(3)

# %%
# menghitung harga produk rata-rata di Jabodetabek dan luar Jabodetabek
harga_jabodetabek = data_analysis[data_analysis['lokasi'] == 'Jabodetabek']['harga produk'].mean()
harga_luar_jabodetabek = data_analysis[data_analysis['lokasi'] != 'Jabodetabek']['harga produk'].mean()

# hipotesis
h0 = np.mean(data_analysis[data_analysis['lokasi'] == 'Jabodetabek']['harga produk']) != np.mean(data_analysis[data_analysis['lokasi'] != 'Jabodetabek']['harga produk'])
h1 = np.mean(data_analysis[data_analysis['lokasi'] == 'Jabodetabek']['harga produk']) == np.mean(data_analysis[data_analysis['lokasi'] != 'Jabodetabek']['harga produk'])

# uji t-test
t_stat, p_value = stats.ttest_ind(data_analysis[data_analysis['lokasi'] == 'Jabodetabek']['harga produk'], data_analysis[data_analysis['lokasi'] != 'Jabodetabek']['harga produk'])

# Tampilkan hasil uji hipotesis
print(f"Rata-rata harga produk di Jabodetabek\t\t: {harga_jabodetabek}")
print(f"Rata-rata harga produk di Luar Jabodetabek\t: {harga_luar_jabodetabek}")
print(f"T-stats\t\t\t\t\t\t: {t_stat}")
print(f"P-Value\t\t\t\t\t\t: {p_value}")

print("")
# Buat kesimpulan
if p_value < 0.05:
    print('Hipotesis nol ditolak')
else:
    print('Hipotesis nol diterima')

# %% [markdown]
# **Penjelasan:**
# 
# - Pada uji hipotesis kali ini kita menggunakan t-stat dikarnakan size sample lebih dari 30, dan jenis hipotesis komparatif yang menggunakan hipotesis dua sisi (two-tailed hypothesis)
# 
# - T-stats: Nilai t-stats yang rendah (-0.21) nilai ini menunjukkan perbedaan rata-rata harga antara Jabodetabek dan luar Jabodetabek sangat kecil
# 
# - P-value: Nilai p-value yang tinggi (0.84) jauh lebih besar dari tingkat signifikansi (0.05). ini menunjukkan bahwa tidak ada bukti yang cukup untuk menolak hipotesis null
# 
# Berdasarkan data yang tersedia, tidak ada bukti yang cukup kuat untuk menunjukkan bahwa harga barang di Jabodetabek berbeda secara signifikan dengan harga di luar Jabodetabek. Perbedaan kecil pada rata-rata harga mungkin karna faktor lain selain biaya bahan baku, seperti biaya transportasi, permintaan, dan penawaran.
# 

# %% [markdown]
# ## 4. Apakah orang lebih cenderung suka dengan produk yang harganya murah?

# %%
sns.lmplot(data = data_analysis,x='rating produk',y='harga produk')

# %% [markdown]
# #### Pearson Correlation (Hubungan Linear)

# %%
# uji korelasi pearson
corr_r , pval_p = stats.pearsonr(data_analysis['harga produk'],data_analysis['rating produk'])

print(f"r-correlation: {corr_r:.2f}\np-value : {pval_p}")

# %% [markdown]
# - Terdapat hubungan korelasi negatif antara rating produk dan harga produk.
# - Artinya, semakin tinggi harga produk, semakin rendah rating produknya.
# - Namun, nilai koefisien korelasinya kecil (kurang dari 0.3), menunjukkan bahwa hubungannya lemah.
# - Nilai p jauh lebih kecil dari 0.05 (tingkat signifikansi umum), menunjukkan bahwa terdapat bukti statistik yang kuat untuk menolak hipotesis null (H0) yang menyatakan bahwa tidak terdapat hubungan antara rating produk dan harga produk.

# %% [markdown]
# #### Spearman Correlation (Hubungan Non-Linear)

# %%
# uji korelasi spearman
if len(data_analysis['harga produk']) == len(data_analysis['rating produk']):
    corr_a, pval_b = stats.spearmanr(data_analysis['harga produk'].values.reshape(-1,1), data_analysis['rating produk'].values.reshape(-1,1))
    print(f"Spearman correlation: {corr_a:.2f}\np-value: {pval_b}")

# %% [markdown]
# - Terdapat hubungan korelasi non-linear yang lemah antara rating produk dan harga produk.
# - Arah hubungannya tidak dapat ditentukan secara pasti.
# - Nilai p lebih besar dari 0.05 (tingkat signifikansi umum), menunjukkan bahwa tidak terdapat bukti statistik yang cukup untuk menolak hipotesis null (H0) yang menyatakan bahwa tidak terdapat hubungan antara rating produk dan harga produk.

# %% [markdown]
# # E. Conclusion

# %% [markdown]
# ### 1.


