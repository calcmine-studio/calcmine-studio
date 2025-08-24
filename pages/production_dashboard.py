import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import data_loader, chart_generator, export_utils

st.title("📊 Production Dashboard")

# Input tanggal
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Upload data
uploaded_file = st.file_uploader("Upload production data (CSV/Excel)", type=["csv", "xlsx"])
if uploaded_file:
    df = data_loader.load_data(uploaded_file)
    st.dataframe(df.head())

    # Chart
    fig = chart_generator.plot_production(df)
    st.pyplot(fig)

    # Download hasil
    export_utils.download_excel(df, "production_output.xlsx")
