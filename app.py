# Breast Cancer AI Application
# Add your Python code here

import streamlit as st
import tf_keras as keras
import numpy as np
import cv2
from tf_keras.applications.efficientnet import preprocess_input
from PIL import Image
import gdown
import os

# Download model from Google Drive
MODEL_PATH = "final_cancer_model.keras"
if not os.path.exists(MODEL_PATH):
    st.info("Loading model...")
    # Bdel YOUR_FILE_ID b ID dial model mn Google Drive
    gdown.download(f"https://drive.google.com/uc?id=1oWblhBhZ0ZdkgybXb4qn5I_ik4_MlVwi", MODEL_PATH, quiet=False)

model = keras.models.load_model(MODEL_PATH)

def make_gradcam_heatmap(img_array, model):
    efficientnet_model = model.get_layer("efficientnetb0")
    grad_model = keras.models.Model(
        inputs=efficientnet_model.input,
        outputs=[
            efficientnet_model.get_layer("top_conv").output,
            efficientnet_model.output
        ]
    )
    import tensorflow as tf
    with tf.GradientTape() as tape:
        last_conv_output, preds = grad_model(img_array)
        class_channel = preds[:, 0]
    grads = tape.gradient(class_channel, last_conv_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    heatmap = last_conv_output[0] @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-8)
    return heatmap.numpy()

# UI
st.set_page_config(layout="wide")
st.title("🩺 CancerDetect AI")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Accuracy", "85%")
with col2:
    st.metric("Model", "EfficientNetB0")
with col3:
    st.metric("Dataset", "220K images")

uploaded = st.file_uploader("Upload Histopathologic Image", type=["tif", "png", "jpg", "jpeg"])

if uploaded:
    img = Image.open(uploaded).convert("RGB").resize((96, 96))
    img_array = np.array(img)
    img_input = preprocess_input(np.expand_dims(img_array.copy(), axis=0))

    pred = model.predict(img_input, verbose=0)[0][0]

    heatmap = make_gradcam_heatmap(img_input, model)
    heatmap_resized = cv2.resize(heatmap, (96, 96))
    heatmap_smooth = cv2.GaussianBlur(heatmap_resized, (11, 11), 0)
    heatmap_colored = cv2.applyColorMap(np.uint8(255 * heatmap_smooth), cv2.COLORMAP_JET)
    heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)
    superimposed = cv2.addWeighted(img_array, 0.6, heatmap_colored, 0.4, 0)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.image(img_array, caption="Original Image")
    with c2:
        st.image(heatmap_smooth, caption="Grad-CAM Heatmap", clamp=True)
    with c3:
        st.image(superimposed, caption="Superimposed")

    if pred >= 0.5:
        st.error(f"🔴 Cancer Detected - Confidence: {pred:.2%}")
    else:
        st.success(f"✅ No Cancer Detected - Confidence: {(1-pred):.2%}")
