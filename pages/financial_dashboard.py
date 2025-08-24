import streamlit as st
import pandas as pd
from utils import data_loader, export_utils

st.title("📈 Financial Dashboard")

uploaded_file = st.file_uploader("Upload financial data (CSV/Excel)", type=["csv", "xlsx"])
if uploaded_file:
    df = data_loader.load_data(uploaded_file)
    st.dataframe(df.describe())

    export_utils.download_excel(df, "financial_output.xlsx")
