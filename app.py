import gradio as gr
import tf_keras as keras
import numpy as np
import cv2
from tf_keras.applications.efficientnet import preprocess_input
from PIL import Image
import gdown, os, tensorflow as tf

MODEL_PATH = "model.keras"
if not os.path.exists(MODEL_PATH):
    gdown.download(f"https://drive.google.com/uc?id=1oWblhBhZ0ZdkgybXb4qn5I_ik4_MlVwi", MODEL_PATH)

model = keras.models.load_model(MODEL_PATH)

def predict(image):
    img = Image.fromarray(image).resize((96, 96))
    img_array = preprocess_input(np.expand_dims(np.array(img), axis=0))
    pred = model.predict(img_array, verbose=0)[0][0]
    if pred >= 0.5:
        return f"🔴 Cancer Detected - {pred:.2%}"
    return f"✅ No Cancer - {(1-pred):.2%}"

gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs=gr.Text(),
    title="🩺 Breast Cancer Detection"
).launch()
