import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Visualisasi Dataset dengan Chart Bawaan Streamlit")

# Upload dataset dari file CSV
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    # Membaca dataset yang diupload
    df = pd.read_csv(uploaded_file)
    
    st.write("Dataframe yang diupload:")
    st.dataframe(df)

    # Pilih kolom untuk sumbu X dan Y
    columns = df.columns.tolist()
    
    if len(columns) >= 2:
        x_column = st.selectbox("Pilih kolom untuk sumbu X", columns)
        y_column = st.selectbox("Pilih kolom untuk sumbu Y", columns)

        # Membuat dataframe yang hanya berisi kolom yang dipilih
        selected_data = df[[x_column, y_column]]

        # Pilih tipe chart
        chart_type = st.selectbox("Pilih tipe chart", ["Line Chart", "Area Chart", "Bar Chart"])

        # Menampilkan chart sesuai tipe yang dipilih
        if chart_type == "Line Chart":
            st.line_chart(selected_data.set_index(x_column))
        elif chart_type == "Area Chart":
            st.area_chart(selected_data.set_index(x_column))
        elif chart_type == "Bar Chart":
            st.bar_chart(selected_data.set_index(x_column))
    else:
        st.write("Dataset memerlukan setidaknya dua kolom untuk divisualisasikan.")
else:
    st.write("Silakan upload file CSV terlebih dahulu.")
