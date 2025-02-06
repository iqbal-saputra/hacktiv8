[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7uRqIoRT)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15291030&assignment_repo_type=AssignmentRepo)
# Live Code 4 - Set 2

---

## Assignment Objectives

*Live Code 4* ini dibuat guna mengevaluasi konsep Regression sebagai berikut:

- Mampu memahami konsep regression dengan Linear Regression.

- Mampu mempersiapkan data untuk digunakan dalam model Linear Regression.

- Mampu mengimplementasikan Linear Regression untuk membuat prediksi.

---

## Dataset Description

Dataset Name : `university-tuition-fees.csv`

Dataset Description : This dataset contains information of top universities in United Kingdom

| Column | Description |
| --- | --- |
| `region` | Region where university is located |
| `founded_year` | Founded year of the university |
| `uk_rank` | Ranking of the university in United Kingdom |
| `world_rank` | Ranking of the university in the world |
| `minimum_ielts_score` | Minimum IELTS score reuired to enter the univeristy |
| `tuition_fees` | Average tuition fees for undergraduate program (in Poundsterling) |
| `international_students` | International student allocation (%). Higher scores mean more students from different parts of the world. |
| `student_satisfaction` | Student satisfaction score (%). Higher scores means the student is satisfied or happy with the University's programs such as curriculum, campus life, lecture delivery, etc. |
| `student_enrollment` | Student enrolled count per year |
| `academic_staff` | Academic staff count |
| `type` | Type of University (`Public` or `Private`) |
| `location` | University location |
| `cost_of_living` | Estimated cost of living per year (in Poundsterling) |

---

## Problems

Anda adalah seorang Data Scientist disebuah organisasi non profit yang bergerak dibidang pendidikan yang berada di UK. Dikarenakan UK merupakan negara maju, maka tidak jarang mahasiswa yang kuliah disana berasal dari berbagai macam negara. Hal ini juga selaras dengan banyaknya universitas baru di UK. Organisasi tempat Anda bekerja meminta Anda untuk membantu mengestimasi total biaya yang harus dibayarkan oleh seseorang jika ingin kuliah di UK.

Buatlah model Linear Regression untuk memprediksi biaya pendidikan disebuah universitas yang harus dibayar oleh seseorang menggunakan dataset yang disediakan. Dataset terlampir pada repository dan jawablah pertanyaan dibawah ini.

***Note : Anda diwajibkan untuk menjawab pertanyaan-pertanyaan dibawah ini. Namun, Anda juga dipersilakan untuk melakukan Exploratory Data Analysis (EDA) dan analisa model lainnya pada bagian Model Evaluation diluar pertanyaan yang diminta.***

### Lakukan pada bagian Exploratory Data Analysis (EDA)
1. Informasi yang diberikan dibawah ini adalah jenis universitas berdasarkan rangking secara globalnya (`world_rank`). 

   * `League A` : `world_rank` < 99
   
   * `League B` : 100 ≤ `world_rank` < 499
   
   * `League C` : 500 ≤ `world_rank` < 999
   
   * `League D` : 1000 ≤ `world_rank` < 1999
   
   * `League E` : 2000 ≤ `world_rank` < 3999
   
   * `League F` : `world_rank` ≥ 4000

   Buatlah bar plot yang menampilkan besarnya masing-masing jenis diatas dan urutkan dari jumlah jenis terbanyak hingga terkecil. 

### Lakukan pada bagian Model Evaluation
1. Analisa hasil prediksi dengan langkah-langkah dibawah ini : 
   1. Lakukan prediksi pada test-set. 
   
   2. Dari keseluruhan test-set yang diprediksi, berapa nilai minimum dan nilai maksimum yang diprediksi oleh model. 
   
   3. Bandingkan nilai minimum dan nilai maksimum dari keseluruhan hasil prediksi dengan nilai minimum dan nilai maksimum yang sebenarnya dari keseluruhan test-set.
   
   4. Analisa dan narasikan hasil ini.
 
2. Apakah model Anda cenderung menghasilkan harga prediksi yang lebih rendah ataukah cenderung menghasilkan harga prediksi yang lebih tinggi dari harga sebenarnya baik dari train-set maupun test-set ? Buktikan hal ini dengan sebuah eksplorasi.

---

## Instruction

*Live Code 4* dikerjakan dalam format ***notebook (.ipynb)*** dengan beberapa **kriteria wajib** dibawah ini:

1. Machine learning framework yang digunakan adalah *Scikit-Learn*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* **harus berisi dan hanya berisi** semua *library* yang digunakan dalam *project*.

   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi eksplorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.
   
   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-test, transformasi data (normalisasi, encoding, dll.), dan proses-proses lain yang dibutuhkan.

   6. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

   7. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
   8. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   9. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model.

   10. Model Inference
       > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled.
   
   11. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, **harus berisi** kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.
    
4. *Notebook* harus diupload dalam akun GitHub masing-masing student untuk selanjutnya dinilai.

---

## Assignment Submission

- Simpan assignment pada sesi ini dengan nama `P1LC4_Set_2_<nama-students>.ipynb` misal `P1LC4_Set_2_raka_ardhi.ipynb`.

- Push Assigment yang telah Anda buat ke akun Github Classroom Anda masing-masing.

---

## Assignment Rubrics

### Code Review

| Criteria| Meet Expectations | Points |
| --- | --- | --- |
| Feature Engineering | Mampu melakukan preprocessing dataset sebelum melakukan proses modeling (split data, normalisasi, encoding, dll) | 35 pts |
| Linear Regression | Mengimplementasikan Linear Regression dan menentukan hyperparameter yang tepat dengan Scikit-Learn | 10 pts |
| Model Inference | Mencoba model yang telah dibuat dengan data baru | 10 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar | 10 pts |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata dengan Baik| Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 15 pts |

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

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Model Analysis | Menganalisa informasi dari model yang telah dibuat | 25 pts |
| Overall Analysis | Menarik informasi/kesimpulan dari keseluruhan kegiatan yang dilakukan | 10 pts |

```
Contoh kriteria analisa yang baik diantaranya adalah: 

1. Terdapat penjelasan macam-macam hasil metric evaluasi dan interpretasinya terhadap kasus yang diselesaikan.
2. Dapat menjelaskan KELEBIHAN dan KELEMAHAN dari model yang dibuat DENGAN KAITANNYA DENGAN DOMAIN BUSINESS YANG DIHADAPI yang dibuktikan dengan eksplorasi sederhana (grafik, plot, teori, dll).
3. Dapat memberikan statement untuk improvement selanjutnya dari model yang dibuat. 
4. Dapat menyebutkan insight yang dapat diambil setelah proses EDA, dll.
```

---

```
Total Points : 115
```

---
## Notes

* **Deadline : pukul 12:15 WIB.**

* **Keterlambatan pengumpulan tugas mengakibatkan skor LC 4 menjadi 0.**
