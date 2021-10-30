
import streamlit as st
import numpy as np
import numpy.matlib
import random
from PIL import Image


# enable users to upload images for the model to make predictions
file_up = st.file_uploader("Upload an image", type = "jpg")

num_clusters = st.slider("Number of clusters", 1, 20, 8)
num_iters = st.slider("Number of iters", 1, 100, 30)
