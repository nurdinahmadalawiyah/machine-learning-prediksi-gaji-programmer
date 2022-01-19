import streamlit as st
from predict_page import show_predict_page
from about_page import show_about_page
from PIL import Image



page = st.sidebar.selectbox("Navigasi", ("Prediksi Gaji", "Tentang Kami"))

if page == "Prediksi Gaji":
    show_predict_page()
else:
    show_about_page()

image = Image.open('TEDC.png')

st.sidebar.image(image)