import streamlit as st

def render():
    st.markdown("## 📊 Model Evaluation")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.metric("Accuracy", "92.4%")
    st.metric("F1 Score", "0.91")
    st.metric("RMSE", "0.38")

    st.info("Visualizations like confusion matrix, ROC, PCA will appear here.")

    st.markdown('</div>', unsafe_allow_html=True)
