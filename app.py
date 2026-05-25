# Breast Cancer AI Application
# Add your Python code here

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("model.h5")

# Title
st.title("Breast Cancer Detection AI")

st.write("Upload a histopathology image to detect cancer.")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Show image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Resize image
    image = image.resize((96, 96))

    # Convert to array
    img_array = np.array(image)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)

    # Result
    if prediction[0][0] > 0.5:
        st.error("Cancer Detected")
    else:
        st.success("No Cancer Detected")

    # Probability
    st.write(f"Prediction Score: {prediction[0][0]:.4f}")
