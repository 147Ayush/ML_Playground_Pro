import streamlit as st

from utils.navigation import render_navigation
from ui import home, data_preprocessing, model_config, training, evaluation

# ✅ MUST be a function call with parentheses
st.set_page_config(
    page_title="ML Playground Pro",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- Global CSS ----------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.stButton > button {
    width: 100%;
    height: 3rem;
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-weight: 600;
    border: none;
    transition: all 0.3s ease-in-out;
}

.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #8b5cf6, #6366f1);
}

.card {
    background-color: #020617;
    padding: 24px;
    border-radius: 16px;
    box-shadow: 0 0 30px rgba(99,102,241,0.15);
}
</style>
""", unsafe_allow_html=True)

# ---------- Page Routing ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

render_navigation()

page = st.session_state.page

if page == "Home":
    home.render()
elif page == "Data Preprocessing":
    data_preprocessing.render()
elif page == "Model Configuration":
    model_config.render()
elif page == "Training":
    training.render()
elif page == "Evaluation":
    evaluation.render()
