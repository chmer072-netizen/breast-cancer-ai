import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import google.generativeai as genai
import os

# Gemini API
genai.configure(api_key=os.getenv("AIzaSyA0WMXWReh3HnfhDpphyj1m1l4u0tx850g"))

# Load model
model = tf.keras.models.load_model("model.h5")

# Title
st.title("Breast Cancer AI Assistant")

# Upload image
uploaded_file = st.file_uploader("Upload Histopathology Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).resize((96,96))
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # preprocess
    img = np.array(image)/255.0
    img = np.expand_dims(img, axis=0)

    # prediction
    prediction = model.predict(img)[0][0]

    if prediction > 0.5:
        result = "Cancer Detected"
    else:
        result = "Normal"

    st.subheader(f"Prediction: {result}")

# Chatbot
st.header("Medical Chatbot")

question = st.text_input("Ask a medical question")

if question:

    model_gemini = genai.GenerativeModel("gemini-1.5-flash")

    response = model_gemini.generate_content(
        f"""
        You are an AI medical assistant specialized in breast cancer.
        Answer professionally and clearly.

        Question:
        {question}
        """
    )

    st.write(response.text)

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

chat_model = genai.GenerativeModel("gemini-1.5-flash")

st.subheader("Medical AI Chatbot")

question = st.text_input("Ask a medical question")

if question:
    response = chat_model.generate_content(question)

    st.write(response.text)
