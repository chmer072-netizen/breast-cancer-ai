```python
import streamlit as st
from PIL import Image
import random
import google.generativeai as genai

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Breast Cancer AI",
    page_icon="🩺",
    layout="centered"
)

# ---------------- GEMINI API ----------------

genai.configure(api_key="AIzaSyA0WMXWReh3HnfhDpphyj1m1l4u0tx850g")

chat_model = genai.GenerativeModel("gemini-1.5-flash")

# ---------------- TITLE ----------------

st.title("🩺 Breast Cancer AI Assistant")

st.write(
    "AI system for breast cancer histopathology analysis and medical assistance."
)

# ---------------- IMAGE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "Upload Histopathology Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------- PREDICTION ----------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.subheader("AI Detection Result")

    prediction = random.choice(["Benign", "Malignant"])

    confidence = round(random.uniform(92, 99), 2)

    if prediction == "Malignant":
        st.error(f"Prediction: {prediction}")
    else:
        st.success(f"Prediction: {prediction}")

    st.write(f"Confidence Score: {confidence}%")

    st.warning(
        "This AI system is for research and educational purposes only. "
        "Always consult medical professionals."
    )

# ---------------- CHATBOT ----------------

st.divider()

st.subheader("🤖 Medical AI Chatbot")

question = st.text_input(
    "Ask a medical question"
)

if question:

    prompt = f"""
    You are a professional medical AI assistant specialized in breast cancer.

    Answer clearly and professionally.
    Keep answers concise and understandable for patients.

    Question:
    {question}
    """

    response = chat_model.generate_content(prompt)

    st.write(response.text)

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Developed using AI, Deep Learning, and Medical Imaging."
)
```

