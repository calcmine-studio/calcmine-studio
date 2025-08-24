import streamlit as st
import pandas as pd
from utils import data_loader, chart_generator, export_utils

st.title("💰 Cost Dashboard")

uploaded_file = st.file_uploader("Upload cost data (CSV/Excel)", type=["csv", "xlsx"])
if uploaded_file:
    df = data_loader.load_data(uploaded_file)
    st.dataframe(df.head())

    st.bar_chart(df.set_index(df.columns[0]))

    export_utils.download_excel(df, "cost_output.xlsx")
