import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Breast Cancer AI Assistant",
    page_icon="🔬",
    layout="centered"
)

# =========================
# TITLE
# =========================
st.markdown("<h1 style='text-align: center; color: #ff4da6;'>🎗️ Breast Cancer AI Assistant 🤖</h1>", unsafe_allow_html=True)

st.write("Ask any medical question about breast cancer, diagnosis, treatment, or prevention.")

# =========================
# QUESTIONS & ANSWERS
# =========================
questions_responses = {

    "what is breast cancer":
    "Breast cancer is a disease where abnormal cells grow uncontrollably in breast tissue. Early detection greatly improves treatment success.",

    "what are the symptoms of breast cancer":
    "Common symptoms include a lump in the breast, changes in breast shape, nipple discharge, skin dimpling, breast pain, or redness.",

    "what is chemotherapy":
    "Chemotherapy is a cancer treatment that uses strong drugs to destroy cancer cells or stop their growth.",

    "what is radiotherapy":
    "Radiotherapy uses high-energy radiation to kill cancer cells and shrink tumors.",

    "what is immunotherapy":
    "Immunotherapy helps the immune system recognize and attack cancer cells more effectively.",

    "what is a biopsy":
    "A biopsy is a medical procedure where doctors remove a small tissue sample to examine it for cancer cells under a microscope.",

    "why is early detection important":
    "Early detection increases the chances of successful treatment, reduces complications, and improves survival rates.",

    "how can breast cancer be detected":
    "Breast cancer can be detected using mammograms, biopsies, MRI scans, ultrasound imaging, and AI-assisted histopathology analysis.",

    "can breast cancer be cured":
    "Many breast cancer cases can be successfully treated, especially when detected early.",

    "what causes breast cancer":
    "Breast cancer may be caused by genetic mutations, hormonal factors, lifestyle habits, age, obesity, smoking, and family history.",

    "what are the risk factors of breast cancer":
    "Risk factors include age, family history, obesity, smoking, alcohol consumption, genetic mutations, and hormonal exposure.",

    "what is a mammogram":
    "A mammogram is an X-ray imaging test used to detect abnormalities or tumors in breast tissue.",

    "what is metastasis":
    "Metastasis occurs when cancer cells spread from the original tumor to other parts of the body.",

    "what are benign tumors":
    "Benign tumors are non-cancerous growths that usually do not spread to other tissues.",

    "what are malignant tumors":
    "Malignant tumors are cancerous growths that can invade nearby tissues and spread to other organs.",

    "how does ai help detect breast cancer":
    "AI can analyze medical images and histopathology slides to identify cancer patterns quickly and assist doctors in diagnosis.",

    "what is histopathology":
    "Histopathology is the microscopic examination of tissue samples to detect diseases such as cancer.",

    "what are cancer cells":
    "Cancer cells are abnormal cells that divide uncontrollably and may spread to other body parts.",

    "what is targeted therapy":
    "Targeted therapy uses drugs that specifically attack cancer-related molecules while minimizing damage to healthy cells.",

    "how can breast cancer be prevented":
    "Maintaining a healthy lifestyle, regular screenings, exercise, and avoiding smoking or excessive alcohol may reduce risk.",

    "can men get breast cancer":
    "Yes, although rare, men can also develop breast cancer.",

    "what is tumor staging":
    "Tumor staging describes the size of cancer and whether it has spread in the body.",

    "what is stage 1 breast cancer":
    "Stage 1 breast cancer is an early stage where the tumor is small and has limited spread.",

    "what is stage 4 breast cancer":
    "Stage 4 breast cancer means the cancer has spread to distant organs such as bones, lungs, liver, or brain.",

    "what is precision":
    "Precision measures how many predicted positive cases were actually positive.",

    "what is recall":
    "Recall measures how many actual positive cases were correctly detected by the AI model.",

    "what is accuracy":
    "Accuracy measures the percentage of correct predictions made by the AI model.",

    "what is auc roc":
    "AUC-ROC evaluates the performance of a classification model by measuring its ability to distinguish classes.",

    "what is deep learning":
    "Deep learning is a branch of artificial intelligence that uses neural networks to learn patterns from data.",

    "what is cnn":
    "CNN stands for Convolutional Neural Network, a deep learning model commonly used for image analysis.",

    "what is grad cam":
    "Grad-CAM is a visualization technique that highlights image regions influencing AI predictions.",

    "how accurate is ai in cancer detection":
    "AI models can achieve high accuracy in cancer detection when trained on high-quality medical datasets.",

    "what is medical imaging":
    "Medical imaging refers to technologies used to visualize the inside of the body for diagnosis and treatment.",

    "what is pathology":
    "Pathology is the medical specialty that studies diseases through laboratory examination of tissues and cells."
}

# =========================
# CHATBOT
# =========================
st.subheader("🤖 AI Medical Assistant")

user_question = st.text_input("Ask a medical question:")

if user_question:

    cleaned_question = (
        user_question.lower()
        .strip()
        .replace('"', '')
        .replace("'", "")
        .replace("?", "")
    )

    found = False

    for question, answer in questions_responses.items():

        clean_db_question = (
            question.lower()
            .strip()
            .replace("?", "")
        )

        if cleaned_question == clean_db_question:
            st.success(answer)
            found = True
            break

    if not found:
        st.warning("Sorry, I do not have an answer for this question yet.")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.caption("⚠️ This AI system is designed for educational and research purposes only.")

