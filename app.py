# Breast Cancer AI Application
# Add your Python code here

import streamlit as st

st.set_page_config(layout="wide")

st.title("🩺 CancerDetect AI")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("Accuracy","92%")

with col2:
    st.metric("AUC","0.97")

with col3:
    st.metric("Dataset","220K")

uploaded = st.file_uploader("Upload Image")

if uploaded:
    st.image(uploaded)

st.chat_input("Ask AI...")
