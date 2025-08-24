import streamlit as st

st.set_page_config(page_title="CalcMine Studio", page_icon="⛏️", layout="wide")

# Hero section
st.markdown("<h1 style='text-align: center;'>⛏️ CalcMine Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Automated Mining Dashboards for Cost, Financial, and Production Analysis 🚀</p>", unsafe_allow_html=True)

# CTA
st.markdown("<div style='text-align:center; margin:20px;'>", unsafe_allow_html=True)
if st.button("🚀 Start Free Trial"):
    st.switch_page("main.py")  # butuh streamlit-extras
st.markdown("</div>", unsafe_allow_html=True)

# Features
st.subheader("✨ Key Features")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("📊 **Production Dashboard**\nVisualize production data over time.")
with col2:
    st.markdown("💰 **Cost Dashboard**\nTrack cost breakdown and optimize expenses.")
with col3:
    st.markdown("📈 **Financial Dashboard**\nAnalyze KPIs, revenue, and profitability.")

# Pricing
st.subheader("💵 Pricing Plans")
st.write("""
- **Free**: Limited features  
- **Pro**: Full dashboards, export, premium support  
- **Enterprise**: Custom solutions for mining companies  
""")
