import streamlit as st

def render():
    st.markdown("## 🚀 Model Training")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🔁 Cross Validation")
    st.slider("Number of folds", 2, 10, 5)

    if st.button("▶️ Start Training"):
        with st.spinner("Training model..."):
            st.success("Training completed successfully!")

    st.markdown('</div>', unsafe_allow_html=True)
