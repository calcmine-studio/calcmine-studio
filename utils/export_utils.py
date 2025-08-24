import streamlit as st
import pandas as pd
from io import BytesIO

def download_excel(df, filename="output.xlsx"):
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    st.download_button(
        label="⬇️ Download Excel",
        data=buffer,
        file_name=filename,
        mime="application/vnd.ms-excel"
    )
