# image_viewer.py

import streamlit as st
from PIL import Image

def main():
    st.title("Image Uploader and Viewer")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
st.image(image, caption="Uploaded Image.", use_container_width=True)
except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error("Please upload a valid image file.")

if __name__ == "__main__":
    main()
