import streamlit as st
import pandas as pd
st.subheader("uploading csv")
df=st.file_uploader("upload csv file:",type=['csv','xlsx'])
if df is not None:
    st.dataframe(df)
st.subheader("dealing with images")
st.image("C:\\Users\SHREENATH S HEBBAR\Pictures\zomato pics\WhatsApp Image 2023-04-18 at 17.51.45.jpg")
df=st.file_uploader("upload image file:",type=['png','jpeg'])
if df is not None:
    st.image(df)
st.subheader("upload video file")
video =st.file_uploader("video",type=["mp4"])
st.video(video)



