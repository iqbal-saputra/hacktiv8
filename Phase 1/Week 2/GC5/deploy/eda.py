import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load data from a CSV file
data = pd.read_csv('P1G5_Set_1_iqbal_saputra.csv')

def eda_page():

    st.title("Eksploratory Data Analysis")
    st.write('Analisa data pada dataframe untuk lebih memahami isi dari data')
    st.markdown("<h2><b>Distribusi data kolom default_payment_next_month</b></h2>", unsafe_allow_html=True)


    # Create histogram
    fig, ax = plt.subplots(figsize=(16, 5))
    sns.barplot(data['default_payment_next_month'].value_counts(), ax=ax)

    # Display histogram using Streamlit
    st.pyplot(fig)
    st.write("**Penjelasan**:")
    st.write('Berdasarkan pie plot distribusi data kolom default_payment_next_month memiliki jumlah 3000 adalah tidak membayar dan 700 adalah membayar')
    st.write()
    # Create boxplot
    fig, axes = plt.subplots(6, 4, figsize=(15, 15))
    axes = axes.flatten()
    num_col = data.columns
    for i, column in enumerate(num_col):
        axes[i].boxplot(data[column])
        axes[i].set_title(column)

    # Remove empty subplots
    for j in range(len(num_col), len(axes)):
        axes[j].axis('off')

    # Tighten the layout
    plt.tight_layout()

    # Display boxplot using Streamlit
    st.pyplot(fig)


    # Create stacked bar chart
    categorical = ['sex', 'marital_status', 'education_level', 'pay_0', 'pay_2', 'pay_3', 'pay_4', 'pay_5', 'pay_6']
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 18))
    axes = axes.flatten()
    for i, x in enumerate(categorical):
        row = i // 3
        col = i % 3
        cross_table = pd.crosstab(data[x], data['default_payment_next_month'])
        cross_table.plot(kind='bar', stacked=False, color=['red', 'blue'], ax=axes[i])
        axes[i].set_xlabel(x)
        axes[i].set_ylabel('Count')
        axes[i].set_title(f"Relationship between {x} and default_payment_next_month")
        axes[i].legend(title='target', labels=['No', 'Yes'])
        axes[i].tick_params(axis='x', rotation=45)
    plt.tight_layout()

    # Display stacked bar chart using Streamlit
    st.pyplot(fig)

    st.write("**Penjelasan**:")
    st.write('''Berdasarkan hasil dari visualisasi hubungan default_payment_next_month dengan seluruh kolom kategori didaptkan :
* `Sex` : Berdarkan sex untuk laki-laki (1) dan perempuan (2) keduanya memiliki jumlah yang akan membayar payment kredit lebih banyak ketimbang yang tidak membayar. Untuk jumlahnya sendiri, perempuan lebih banyak untuk orang yang akan membayar tetapi lebih banyak juga untuk orang tidak membayar ketimbang laki-laki. Dari sini dapat diketahui bahwa jumlah nasabah perempuan lebih banyak dari laki-laki
* `Marital_Status` : Pada marital status terdapat perbedaan jumlah nasabah yang akan memabayar dan akan tidak membayar pada kedua jenis valuenya. Dimana untuk yang sudah menikah (1) dan belum menikah (2) jumlah nasabah yang akan memabayar kredit bulan depan lebih besar ketimbang yang tidak membayar kredit pada bulan depan
* `Education_level` : Pada education level didapatkan sebuah pola dimana jumlah yang membayar ataupun yang tidak membayar memiliki perbedaan yang signifikan sesuai dengan tingkat pendidikannya. Untuk eduaciton level ini dapat diambil asumsi sementara bahwa education_level ini memiliki hubungan dengan default_payment_next_month
* `pay_0`, `pay_2`, `pay_3`, `pay_4`, `pay_5`, `pay_6` : Pada keenam kolom ini dapat dilihat perbedaan yang sangat besar untuk nilai default_payment_next_month didalamnya. Perbedaan yang membentuk pola pada nilai pay ini dapat diasumsikan bahwa data pay ini memiliki korelasi dengan default_payment_next_month
* Dari seluruh data ini asumsi sementara adalah bahwa `education_level`, `pay_0`, `pay_2`, `pay_3`, `pay_4`, `pay_5`, `pay_6` memiliki korelasi dengan `default_payment_next_month` sedangkan `sex` dan `marital_status` masih belum dapat diambil asumsi apapun. Untuk korelasi yang lebih tepat sendiri harus dilakukan uji korelasi pada saat proses data engineering nanti agar fitur yang digunakan lebih akurat dalam menghasilkan prediksi pada model''')
    st.write()

    # Select categorical and numerical columns
    categorical = ['sex', 'marital_status', 'education_level', 'default_payment_next_month']
    numerical = [col for col in data if col not in categorical]

    # Calculate correlation matrix
    correlation_matrix = data[numerical].corr()

    # Create correlation heatmap
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title('Correlation Heatmap of Numerical Columns')

    # Display heatmap using Streamlit
    st.pyplot(fig)

    st.write("**Penjelasan**:")
    st.write('''* Berdasarkan heatmap, terdapat korelasi pada hubungan `pay_amt_1` dengan `pay_amt_2` dimana nilai korelasinya adalah `0.43`. Korelasi ini menunjukkan hubunga yang lemah dari keduanya dimana pembayaran orang pada `pay_amt_1` memiliki jumlah yang berbanding lurus dengan `pay_amt_2`
* Pada kolom bill, seluruh kolom bill memiliki korelasi yang kuat. Berdasarkan data sendiri, hal ini disebabkan karena besarnya tagihan kredit dari 1 bulan ke bulan lainnya memiliki nilai yang sama atau terus bertambah''')
    st.write()


   