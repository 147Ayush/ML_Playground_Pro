import streamlit as st

def render():
    st.markdown("## Model Training")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.info("Training logic will execute here.")
    st.success("Model trained successfully (placeholder).")

    if st.button("Next → Evaluation"):
        st.session_state.page = "Evaluation"

    st.markdown('</div>', unsafe_allow_html=True)
