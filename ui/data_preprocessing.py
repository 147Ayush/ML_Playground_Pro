import streamlit as st

def render():
    st.markdown("## 🧹 Data Preprocessing")
    st.markdown("Configure data cleaning, scaling, encoding & outlier handling")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📂 Dataset Upload")
    st.file_uploader("Upload CSV file", type=["csv"])

    st.subheader("🩹 Missing Value Handling")
    st.selectbox("Strategy", ["Mean", "Median", "Mode", "Drop Rows"])

    st.subheader("📏 Feature Scaling")
    st.multiselect("Scaling Method", ["StandardScaler", "MinMaxScaler", "RobustScaler"])

    st.subheader("🚨 Outlier Handling")
    st.checkbox("Enable Outlier Removal")
    st.selectbox("Method", ["IQR", "Z-Score", "Isolation Forest"])

    st.markdown('</div>', unsafe_allow_html=True)
