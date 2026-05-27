import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# =========================
# LOAD MODEL
# =========================
model = load_model("model.h5")

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Breast Cancer AI Assistant",
    page_icon="🎗️",
    layout="centered"
)

# =========================
# TITLE
# =========================
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4da6;'>
    🎗️ Breast Cancer AI Assistant 🤖
    </h1>
    """,
    unsafe_allow_html=True
)

st.write(
    "Ask any medical question about breast cancer, diagnosis, treatment, or prevention."
)

st.markdown("---")

# =========================
# CHATBOT SECTION
# =========================
st.header("🧠 AI Medical Assistant")

question = st.text_input("Ask a medical question:")

answer = ""

if question:

    q = question.lower()

    # =========================
    # QUESTIONS & ANSWERS
    # =========================

    if "symptom" in q or "sign" in q:
        answer = """
Breast cancer symptoms may include:

• A lump in the breast or underarm  
• Changes in breast size or shape  
• Nipple discharge  
• Breast pain  
• Skin dimpling or redness  
• Inverted nipple  

Early detection is extremely important.
"""

    elif "chemotherapy" in q or "chemo" in q:
        answer = """
Chemotherapy is a cancer treatment that uses strong drugs to destroy cancer cells or stop their growth.

It may be used before surgery, after surgery, or when cancer has spread.
"""

    elif "biopsy" in q:
        answer = """
A biopsy is a medical procedure where doctors remove a small tissue sample from the breast.

The sample is examined under a microscope to check if cancer cells are present.
"""

    elif "radiotherapy" in q or "radiation" in q:
        answer = """
Radiotherapy uses high-energy radiation to destroy cancer cells.

It is often used after surgery to reduce the risk of cancer recurrence.
"""

    elif "mammography" in q or "mammogram" in q:
        answer = """
Mammography is an imaging test that uses low-dose X-rays to detect abnormalities in breast tissue.

It helps identify breast cancer early.
"""

    elif "early detection" in q:
        answer = """
Early detection increases the chances of successful treatment and survival.

Screening methods like mammography can detect cancer before symptoms appear.
"""

    elif "treatment" in q:
        answer = """
Breast cancer treatments may include:

• Surgery  
• Chemotherapy  
• Radiotherapy  
• Hormone therapy  
• Targeted therapy  

Treatment depends on the cancer stage and type.
"""

    elif "prevent" in q or "prevention" in q:
        answer = """
Breast cancer prevention strategies include:

• Regular screening  
• Healthy lifestyle  
• Physical activity  
• Avoiding smoking  
• Limiting alcohol consumption
"""

    elif "stage" in q:
        answer = """
Breast cancer stages describe how far the cancer has spread.

Stages range from Stage 0 to Stage IV.
"""

    elif "tumor" in q:
        answer = """
A tumor is an abnormal mass of tissue caused by uncontrolled cell growth.

Tumors may be benign or malignant.
"""

    elif "metastasis" in q:
        answer = """
Metastasis occurs when cancer cells spread from the breast to other organs such as bones, lungs, liver, or brain.
"""

    elif "survival" in q:
        answer = """
Survival rates depend on the cancer stage and early diagnosis.

Early-stage breast cancer often has a high survival rate.
"""

    elif "ai" in q:
        answer = """
Artificial Intelligence can help doctors analyze medical images and detect cancer patterns faster and more accurately.
"""

    else:
        answer = """
Breast cancer is a disease where abnormal cells grow uncontrollably in breast tissue.

It is one of the most common cancers in women. Early detection can significantly improve treatment success and survival rates.
"""

    st.success(answer)

st.markdown("---")

# =========================
# PREDICTION SECTION
# =========================
st.header("🔬 Breast Cancer Prediction")

uploaded_file = st.file_uploader(
    "Upload a histopathology image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Histopathology Image",
        use_container_width=True
    )

    st.write("⏳ AI is analyzing the image...")

    # =========================
    # IMAGE PREPROCESSING
    # =========================
    img = image.resize((96, 96))

    img_array = np.array(img)

    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    # =========================
    # PREDICTION
    # =========================
    prediction = model.predict(img_array)[0][0]

    # =========================
    # RESULT
    # =========================
    if prediction > 0.5:

        st.error(
            f"⚠️ Cancer Detected — Confidence: {prediction*100:.2f}%"
        )

        st.warning(
            "The AI model detected suspicious cancerous tissue patterns."
        )

    else:

        st.success(
            f"✅ Normal Tissue — Confidence: {(1-prediction)*100:.2f}%"
        )

        st.info(
            "No significant cancerous patterns were detected by the AI model."
        )

st.markdown("---")

# =========================
# FOOTER
# =========================
st.caption(
    "⚠️ This AI system is designed for educational and research purposes only."
)
  
