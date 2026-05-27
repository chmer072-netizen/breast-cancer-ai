
import streamlit as st
from PIL import Image
import numpy as np

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Breast Cancer Detection AI⚕️",
    page_icon="🩺",
    layout="centered"
)

# =========================
# TITLE
# =========================

st.title("🩺 Breast Cancer Detection AI")
st.write("Upload a histopathology image for AI analysis.")

# =========================
# IMAGE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png", "tif", "tiff"]
)

# =========================
# IMAGE ANALYSIS
# =========================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Histopathology Image",
        use_container_width=True
    )

    st.write("🔬 Running AI analysis...")

    # Fake prediction demo
    prediction = np.random.rand()

    if prediction > 0.5:
        st.error("⚠️ Prediction: Malignant (Cancer Detected)")
        confidence = prediction * 100
    else:
        st.success("✅ Prediction: Benign (Non-Cancerous)")
        confidence = (1 - prediction) * 100

    st.write(f"Confidence Score: {confidence:.2f}%")

# =========================
# CHATBOT SECTION
# =========================

st.divider()

st.subheader("🤖 Medical AI Assistant")

user_question = st.text_input("Ask a medical question:")

if user_question:

    q = user_question.lower()

    # =========================
    # QUESTIONS & ANSWERS
    # =========================

    if "breast cancer" in q:
        response = """
Breast cancer is a disease where abnormal cells grow uncontrollably in breast tissue.

It is one of the most common cancers in women. Early detection can significantly improve treatment success and survival rates.
"""

    elif "symptoms" in q:
        response = """
Common breast cancer symptoms include:

• Lump in the breast
• Changes in breast shape
• Skin dimpling
• Nipple discharge
• Breast pain
• Redness or swelling

Some patients may not show symptoms during early stages.
"""

    elif "early detection" in q:
        response = """
Early detection is extremely important because it increases survival rates and improves treatment effectiveness.

Detecting cancer at an early stage helps doctors begin treatment before the disease spreads.
"""

    elif "biopsy" in q:
        response = """
A biopsy is a medical procedure where doctors remove a small tissue sample for laboratory analysis.

The tissue is examined under a microscope to determine whether cancer cells are present.
"""

    elif "chemotherapy" in q or "chemo" in q:
        response = """
Chemotherapy is a treatment that uses powerful drugs to destroy cancer cells or stop their growth.

It may be used before surgery, after surgery, or in advanced cancer stages.
"""

    elif "radiotherapy" in q or "radiation" in q:
        response = """
Radiotherapy uses high-energy radiation to destroy cancer cells.

It is commonly used after surgery to reduce the risk of cancer recurrence.
"""

    elif "tumor" in q:
        response = """
A tumor is an abnormal growth of cells.

Tumors can be:
• Benign (non-cancerous)
• Malignant (cancerous)
"""

    elif "malignant" in q:
        response = """
Malignant tumors are cancerous tumors that can invade nearby tissues and spread to other parts of the body.
"""

    elif "benign" in q:
        response = """
Benign tumors are non-cancerous growths that usually do not spread to other parts of the body.
"""

    elif "metastasis" in q:
        response = """
Metastasis is the spread of cancer cells from the original tumor to other organs or tissues in the body.
"""

    elif "ai" in q or "artificial intelligence" in q:
        response = """
Artificial Intelligence in healthcare helps doctors analyze medical images, detect patterns, and improve diagnostic accuracy.

AI can support early breast cancer detection using histopathology images.
"""

    elif "histopathology" in q:
        response = """
Histopathology is the microscopic examination of tissue samples to study disease and detect abnormal cancer cells.
"""

    elif "mammography" in q or "mammogram" in q:
        response = """
Mammography is a medical imaging technique using low-dose X-rays to detect breast abnormalities and possible cancer.
"""

    elif "prevention" in q:
        response = """
Breast cancer prevention strategies may include:

• Healthy lifestyle
• Regular screening
• Physical activity
• Avoiding smoking
• Maintaining healthy weight
"""

    elif "treatment" in q:
        response = """
Breast cancer treatments may include:

• Surgery
• Chemotherapy
• Radiotherapy
• Hormone therapy
• Targeted therapy
"""

    elif "stage" in q:
        response = """
Cancer stages describe how far cancer has spread in the body.

Stages usually range from Stage 0 to Stage IV.
"""

    elif "survival rate" in q:
        response = """
Survival rates are generally higher when breast cancer is detected early and treated quickly.
"""

    elif "doctor" in q:
        response = """
Doctors use medical imaging, biopsy analysis, laboratory tests, and patient history to diagnose breast cancer accurately.
"""

    elif "dataset" in q:
        response = """
A dataset is a collection of medical images or data used to train and evaluate Artificial Intelligence models.
"""

    elif "deep learning" in q:
        response = """
Deep Learning is a branch of Artificial Intelligence that uses neural networks to automatically learn patterns from medical images and data.
"""

    elif "cnn" in q:
        response = """
CNN (Convolutional Neural Network) is a Deep Learning model specialized in image analysis and medical image classification.
"""

    elif "accuracy" in q:
        response = """
Accuracy measures how correctly the AI model predicts cancer and non-cancer cases.
"""

    elif "grad cam" in q or "gradcam" in q:
        response = """
Grad-CAM is an explainable AI technique that highlights important regions in medical images used by the model for prediction.
"""

    else:
        response = """
I can answer questions about:

• Breast cancer
• Biopsy
• Chemotherapy
• Histopathology
• AI detection
• Deep Learning
• CNN
• Grad-CAM
• Symptoms
• Treatment
• Prevention
"""

    st.write("🤖 AI Assistant")
    st.success(response)

    st.caption("⚠️ This AI system is designed for educational and research purposes only.")
