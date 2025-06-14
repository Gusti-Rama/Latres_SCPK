import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title="123230040 Gusti Rama")
st.title("WP Pemilihan Smartphone")
st.write("Gusti Rama / 123230040 / IF-F")

st.subheader("Load data file CSV")
df = pd.read_csv("smartphone.csv", sep=';')
st.dataframe(df, use_container_width=True)

# 1. Menentukan Alternatif
a = df['Name'].tolist()

# 2. Matriks Keputusan
x = df.drop(columns=['Name']).to_numpy()

# 3. Membuat Cost / Benefit Per kriteria
k = [1, 1, 1, 1, 1, 1]

# 4. Membuat Bobot Per kriteria
w = [3, 4, 4, 5, 3, 4]

# 5. Normalisasi Kriteria
w_norm = [c / sum(w) for c in w]

# 6. Menghitung S(i)
# m = Jumlah Alternatif, n = jumlah kriteria
m = len(a)
n = len(w)

s = [1]*m # [1, 1, 1]

for i in range(m): #misal i = 0
    for j in range(n):
        s[i] = s[i] * (x[i][j] ** (k[j] * w_norm[j]))

# 7. Menghitung V
v = [u / sum(s) for u in s]

df_hasil = pd.DataFrame({
    'Smartphone': a,
    'WP Score': v
})

df_hasil = df_hasil.sort_values(by='WP Score', ascending=False).reset_index(drop=True)

st.subheader("Hasil ranking WP")
st.dataframe(
    df_hasil.style.format({'WP Score': '{:.6f}'}),
)
terbaik = a[v.index(max(v))]
st.success(f"Smartphone terbaik adalah: {terbaik} ")