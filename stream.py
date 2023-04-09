from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt
import cv2
from tensorflow import keras
import numpy as np
from PIL import Image,ImageOps

model = keras.models.load_model('saved_model/model.04-1.02.h5')
class_names = ['rock','paper','scissors']

uploaded_image = st.file_uploader(label='Image upload',type=['png','jpg'])
if uploaded_image:
    file_bytes = np.asarray(bytearray(uploaded_image.read()),dtype=np.uint8)
    cv_image = cv2.imdecode(file_bytes,1)
    gray_img = cv2.cvtColor(cv_image,cv2.COLOR_BGR2RGB)
    gray_img = cv2.resize(gray_img,dsize=(224,224))
    gray_img = gray_img.astype('float32')
    gray_img /= 255
    gray_img = np.array([gray_img])
    for_display_image = cv2.cvtColor(cv_image,cv2.COLOR_BGR2RGB)
    for_display_image = cv2.resize(for_display_image,dsize=(120,120,))
    st.image(for_display_image)
with st.form("key1"):
        # ask for input
    button_check = st.form_submit_button("Predict")
if button_check:
    st.text(class_names[np.argmax(model.predict(gray_img))])
