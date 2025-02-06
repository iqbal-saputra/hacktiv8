[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/z_lXnDqw)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15352109&assignment_repo_type=AssignmentRepo)
# Live Code 6 - Set 3

---

## Assignment Objectives

*Live Code 6* ini dibuat guna mengevaluasi konsep Unsupervised Learning sebagai berikut:

- Mampu memahami konsep Unsupervised Learning dengan KMeans.

- Mampu mempersiapkan data untuk digunakan saat training dengan algoritma KMeans.

- Mampu mengimplementasikan KMeans untuk membuat prediksi.

---

## Dataset Desciription

Dataset Name : `influencers.csv`

Dataset Description : Dataset ini merupakan data influencer yang melakukan promosi suatu produk via Facebook Live. Untuk menjaga kerahasiaan identitas influencer, kolom-kolom yang terkait dengan identitas seperti `fullname`, `first_name`, `last_name` dan `username` diganti menjadi data fiktif. Selain kolom-kolom tersebut merupakan data yang asli.

| Column | Description |
| --- | --- |
| `fullname` | Nama lengkap influencer |
| `first_name` | Nama depan influencer |
| `last_name` | Nama belakang influencer |
| `username` | Username influencer |
| `gender` | Jenis kelamin influencer |
| `num_reactions` | Jumlah viewer yang memberikan reaksi saat seorang influencer live |
| `num_comments` | Jumlah viewer yang memberikan komentar saat seorang influencer live |
| `num_shares` | Jumlah viewer yang melakukan share live video influencer tersebut |
| `num_likes` | Jumlah viewer yang menyukai live video influencer tersebut |
| `num_loves` | Jumlah viewer yang memberikan reaksi `love` saat seorang influencer live |
| `num_wows` | Jumlah viewer yang memberikan reaksi `wow` saat seorang influencer live |
| `num_hahas` | Jumlah viewer yang memberikan reaksi `haha` saat seorang influencer live |
| `num_sads` | Jumlah viewer yang memberikan reaksi `sad` saat seorang influencer live |
| `num_angrys` | Jumlah viewer yang memberikan reaksi `angry` saat seorang influencer live |

---

## Problems

Sebuah perusahaan ingin menyewa influencer dari platform Facebook untuk membantu mempromosikan produknya. Bantulah perusahaan tersebut dengan memberikan rekomendasi nama-nama influencer dari dataset yang disediakan jika produk perusahaan tersebut merupakan produk kecantikan wanita. **Nyatakan secara jelas siapa influencer yang Anda rekomendasikan di bagian Kesimpulan**.

*Dataset terlampir pada repository*

---

## Instruction

*Live Code 6* dikerjakan dalam format ***notebook (.ipynb)*** dengan beberapa **kriteria wajib** dibawah ini:
1. Machine learning framework yang digunakan adalah *Scikit-Learn*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan objective yang ingin dicapai.

   2. Import Libraries
      > Cell pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.

   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.

   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset yang diberikan dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.

   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
       > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model.

   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam data untuk membuat model. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.

   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.

4. *Notebook* harus diupload dalam akun GitHub masing-masing student untuk selanjutnya dinilai.

5. **Disarankan mengerjakan menggunakan Google Colab**.
    > Segala jenis problem yang muncul akibat masalah yang dialami komputer student saat Live Code karena menggunakan Jupyter Notebook seperti laptop blue screen, laptop freeze, dll, menjadi tanggung jawab student.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `P1LC6_Set_3_<nama-students>.ipynb` misal `P1LC6_Set_3_raka_ardhi.ipynb`.

- Push Assigment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

---

## Assignment Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (normalisasi, scaling, dll) | 35 pts |
| PCA | Mampu melakukan reduksi dimensi dengan menggunakan PCA | 10 pts |
| KMeans | Mampu melakukan training data dengan algoritma KMeans | 10 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berjalan dan berfungsi dengan sempurna | 10 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Terdapat section Perkenalan yang jelas dan lengkap terkait masalah dan latar belakang masalah yang akan diselesaikan.
2. Tidak menyalin markdown dari tugas lain.
3. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
4. Pemakaian fungsi markdown yang optimal (Heading, text formating, dll).
5. Terdapat komentar pada setiap baris kode.
6. Adanya pemisah yang jelas antar section, dll.
7. Tidak adanya typo.
```

### Analysis

| Criteria | Meet Expectations | Points|
| --- | --- | --- |
| Model Analysis | Mampu melakukan evaluasi model untuk menentukan nilai `K` / jumlah cluster | 15 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 20 pts |

```
Hint : 

Setelah jumlah cluster yang optimal terbentuk, silakan lakukan beberapa hal dibawah ini : 
1. Visualisasikan dalam ruang 2D.
2. Lakukan eksplorasi terhadap masing-masing cluster sehingga ciri khas setiap cluster dapat diketahui.
3. Narasikan influencer mana yang Anda rekomendasikan.
```
---

```
Total Points : 125
```

---

## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 6 menjadi 0.**
