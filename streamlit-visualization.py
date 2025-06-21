
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul halaman
st.title("Dashboard Data COVID-19 Indonesia")

# Sidebar untuk input tahun
tahun = st.sidebar.selectbox("Pilih Tahun", ["2020", "2021", "2022", "2023"])

# Tampilkan teks
st.write(f"Kamu memilih data tahun {tahun}")

# Contoh dataframe
data = pd.DataFrame({
    "Provinsi": ["DIY", "Jawa Tengah", "Jawa Timur"],
    "Kasus": [1200, 3400, 5000]
})

st.dataframe(data)

# Visualisasi
fig, ax = plt.subplots()
ax.bar(data["Provinsi"], data["Kasus"])
st.pyplot(fig)