import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Happiness.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "haberman.csv")

st.title("Cancer prediction - Dashboard")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

status = st.selectbox("Select the status:", df['status'].unique())



for i in df.columns:
    fig_1 = px.histogram(df[df['status'] == status], x=i)
    st.plotly_chart(fig_1, use_container_width=True)
    
