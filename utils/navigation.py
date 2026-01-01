import streamlit as st

def render_navigation():
    st.markdown("## 🧭 Navigation")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🏠 Home"):
            st.session_state.page = "Home"
    with col2:
        if st.button("🧹 Preprocessing"):
            st.session_state.page = "Data Preprocessing"
    with col3:
        if st.button("⚙️ Model Config"):
            st.session_state.page = "Model Configuration"
    with col4:
        if st.button("🚀 Training"):
            st.session_state.page = "Training"
    with col5:
        if st.button("📊 Evaluation"):
            st.session_state.page = "Evaluation"

    st.divider()
