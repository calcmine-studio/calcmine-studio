import streamlit as st

st.set_page_config(page_title="CalcMine Studio", page_icon="⛏️", layout="wide")

# =========================
# Hero Section
# =========================
st.markdown(
    """
    <div style="text-align: center; padding: 50px 0;">
        <h1>⛏️ CalcMine Studio</h1>
        <h3>Automated Mining Dashboards for Cost, Financial, and Production Analysis 🚀</h3>
        <p style="font-size:18px; color: gray;">
            Turn raw mining data into powerful insights with just a few clicks.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,1,1])
with col2:
    if st.button("🚀 Start Free Trial", use_container_width=True):
        st.switch_page("main.py")  # butuh streamlit-extras

# =========================
# Features Section
# =========================
st.markdown("---")
st.subheader("✨ Key Features")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 📊 Production Dashboard")
    st.write("Visualize and monitor production trends over time.")
with col2:
    st.markdown("### 💰 Cost Dashboard")
    st.write("Track cost structure and optimize expenses effectively.")
with col3:
    st.markdown("### 📈 Financial Dashboard")
    st.write("Analyze KPIs, revenue, and profitability in one place.")

# =========================
# Pricing Section
# =========================
st.markdown("---")
st.subheader("💵 Pricing Plans")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### Free\n- Limited features\n- Demo data only\n- Community support\n\n**$0 / month**")
    st.button("Choose Free", key="free")
with col2:
    st.markdown("### Pro\n- Full dashboards\n- Export to Excel\n- Priority support\n\n**$29 / month**")
    st.button("Choose Pro", key="pro")
with col3:
    st.markdown("### Enterprise\n- Custom dashboards\n- On-premise support\n- Dedicated success manager\n\n**Contact Us**")
    st.button("Contact Sales", key="enterprise")

# =========================
# Footer
# =========================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>© 2025 CalcMine Studio — All rights reserved.</p>",
    unsafe_allow_html=True
)
