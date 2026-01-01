import streamlit as st

def render():
    st.markdown("## ⚙️ Model Configuration")
    st.markdown("Choose algorithm and tune hyperparameters")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    task = st.radio("Select Task Type", ["Classification", "Regression", "Clustering"])

    model = st.selectbox(
        "Select Model",
        ["Logistic Regression", "Random Forest", "SVM", "KNN"]
    )

    st.subheader("🔧 Hyperparameters")
    st.slider("Parameter 1", 1, 100, 10)
    st.slider("Parameter 2", 0.01, 1.0, 0.1)

    st.markdown('</div>', unsafe_allow_html=True)
