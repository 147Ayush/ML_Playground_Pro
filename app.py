import streamlit as st
from utils.navigation import top_nav
from ui import home, data_preprocessing, model_config, training, evaluation

st.set_page_config(
    page_title="ML Playground Pro",
    layout="wide"
)

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
body {
    background-color: #F8FAFC;
}

.navbar {
    background-color: #2563EB;
    padding: 16px;
    border-radius: 12px;
}

.nav-item {
    color: white;
    font-weight: 600;
    cursor: pointer;
    text-align: center;
}

.card {
    background-color: black;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Home"

top_nav()

page = st.session_state.page

if page == "Home":
    home.render()
elif page == "Preprocessing":
    data_preprocessing.render()
elif page == "Model Config":
    model_config.render()
elif page == "Training":
    training.render()
elif page == "Evaluation":
    evaluation.render()
