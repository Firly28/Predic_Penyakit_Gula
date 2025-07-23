import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Prediksi Penyakit Gula", layout="wide")
st.title("🩺 Prediksi Risiko Penyakit Gula")

# Load data
df = pd.read_csv("predic_tabel.csv")

# Encode semua kolom kategorikal
le = LabelEncoder()
df_encoded = df.copy()
for col in df.columns[1:]:  # Lewati kolom "No"
    df_encoded[col] = le.fit_transform(df[col])

# Pisahkan fitur dan target
X = df_encoded.drop(["Hasil"], axis=1)
y = df_encoded["Hasil"]

# Latih model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Ambil kolom input asli (non-encoded)
fitur_input = df.columns[1:-1]

# Sidebar input
st.sidebar.header("📋 Masukkan Data Pengguna")
user_input = {}
for fitur in fitur_input:
    nilai_unik = df[fitur].unique().tolist()
    user_input[fitur] = st.sidebar.selectbox(fitur, nilai_unik)

# Prediksi
if st.sidebar.button("🔍 Prediksi"):
    input_df = pd.DataFrame([user_input])
    input_encoded = input_df.copy()
    for col in input_df.columns:
        le.fit(df[col])
        input_encoded[col] = le.transform(input_df[col])
    pred = model.predict(input_encoded)[0]
    hasil_prediksi = "✅ Risiko: Ya" if pred == 1 else "🟢 Risiko: Tidak"
    st.success(hasil_prediksi)

# Tampilkan data dan visualisasi
with st.expander("📊 Lihat Dataset"):
    st.dataframe(df)

st.caption("Model: Random Forest | Dataset: predic_tabel.csv")