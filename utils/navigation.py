import streamlit as st

def top_nav():
    pages = ["Home", "Preprocessing", "Model Config", "Training", "Evaluation"]

    cols = st.columns(len(pages))

    for col, page in zip(cols, pages):
        with col:
            if st.button(
                page,
                use_container_width=True,
                type="primary" if st.session_state.page == page else "secondary"
            ):
                st.session_state.page = page

    st.divider()
