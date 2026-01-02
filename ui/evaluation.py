import streamlit as st
import pickle

def render():
    st.markdown("## Model Evaluation")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.metric("Accuracy", "92%")
    st.metric("F1 Score", "0.91")

    dummy_model = {"model": "trained_model"}

    st.download_button(
        "Download Model",
        pickle.dumps(dummy_model),
        file_name="model.pkl"
    )

    st.info("This is the final stage of the ML pipeline.")

    st.markdown('</div>', unsafe_allow_html=True)
