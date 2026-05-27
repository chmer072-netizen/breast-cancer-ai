
import streamlit as st
from PIL import Image
import numpy as np
import random

st.set_page_config(page_title="Breast Cancer AI", layout="centered")

st.title("🩺 Breast Cancer Detection AI")
st.write("Upload a histopathology image for AI analysis.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    st.subheader("🔍 AI Analysis")

    # Fake prediction for demo
    prediction = random.choice(["Benign", "Malignant"])

    confidence = random.randint(85, 99)

    if prediction == "Malignant":
        st.error(f"Prediction: {prediction}")
    else:
        st.success(f"Prediction: {prediction}")

    st.write(f"Confidence: {confidence}%")

    st.subheader("💡 Medical Advice")

    if prediction == "Malignant":
        st.warning("""
        The AI detected possible cancer indicators.
        
        Please consult a medical specialist for further diagnosis.
        Early detection can save lives.
        """)
    else:
        st.info("""
        No strong cancer indicators were detected.
        
        Continue regular medical checkups.
        """)

st.sidebar.title("🤖 AI Chatbot")

question = st.sidebar.text_input("Ask a medical question")

if question:

    answer = {
        "what is breast cancer":
        "Breast cancer is a disease where abnormal cells grow in breast tissue.",

        "symptoms":
        "Common symptoms include lumps, breast pain, skin changes, and nipple discharge.",

        "treatment":
        "Treatments may include surgery, chemotherapy, radiotherapy, and immunotherapy."
    }

    found = False

    for key in answer:
        if key in question.lower():
            st.sidebar.success(answer[key])
            found = True

    if not found:
        st.sidebar.info(
            "Please consult a healthcare professional for accurate medical advice."
        )

