import streamlit as st

def render():
    st.markdown("""
    <div class="card">
        <h1 style="text-align:center; color:#e5e7eb;">🧠 ML Playground Pro</h1>
        <h4 style="text-align:center; color:#94a3b8;">
        Interactive End-to-End Machine Learning Experimentation Platform
        </h4>
        <hr style="border:1px solid #1e293b;">
        <p style="color:#cbd5f5; font-size:18px; text-align:center;">
        Design, preprocess, train, validate, and evaluate Machine Learning models
        using an intuitive, no-code interface — inspired by industry ML systems.
        </p>
        <br>
        <p style="text-align:center; color:#a5b4fc;">
        👤 <b>Author:</b> Ayush Soni<br>
        🎯 AI & Machine Learning Engineer
        </p>
    </div>
    """, unsafe_allow_html=True)

  