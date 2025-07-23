# 🩺 Aplikasi Prediksi Risiko Penyakit Gula (Diabetes)

Website ini dibangun menggunakan **Streamlit** untuk memprediksi risiko penyakit gula (diabetes) berdasarkan data gejala dan gaya hidup pengguna. Model klasifikasi menggunakan **Random Forest** dan dataset internal.

## 🚀 Fitur
- Input data pengguna melalui sidebar
- Prediksi risiko (Ya/Tidak)
- Tampilkan dataset asli
- Bisa dijalankan di Jupyter Lab atau Streamlit Cloud

## 📁 Struktur File
```
diabetes-app/
├── app.py                # Aplikasi utama Streamlit
├── predic_tabel.csv      # Dataset klasifikasi
└── requirements.txt      # Dependensi Python
```

## 📦 Cara Menjalankan Secara Lokal

1. **Clone repository** ini atau unduh ZIP:
```
git clone https://github.com/username/diabetes-app.git
cd diabetes-app
```

2. **Instal dependensi**
```
pip install -r requirements.txt
```

3. **Jalankan aplikasi**
```
streamlit run app.py
```

## 🌐 Deploy ke Streamlit Cloud
1. Upload folder ini ke GitHub
2. Masuk ke [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Hubungkan akun GitHub, pilih repo, dan jalankan file `app.py`

## 📊 Dataset
Dataset berisi kolom:
- Usia, Jenis Kelamin, Merokok, Bekerja, Rumah Tangga
- Aktivitas Begadang, Olahraga, Asuransi, Penyakit Bawaan
- Target: `Hasil` (Ya/Tidak)

---

🧠 *Dibuat oleh Firly Fahrizah untuk studi kasus klasifikasi penyakit gula.*