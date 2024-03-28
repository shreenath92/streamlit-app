import streamlit as st
from PIL import Image
import pandas as pd
import cv2 as cv
import numpy as np
st.title("1.Image")
img=Image.open("C:\\Users\\SHREENATH S HEBBAR\\Pictures\images\\ship.jpg")
st.image(img)
st.title("2.Image from link")
st.image('https://m.media-amazon.com/images/M/MV5BYWZhOTQwM2UtZTA2ZS00ZWJjLTg4N2YtYjQ4ZjFmMDg2NWJkXkEyXkFqcGdeQXVyNjYxMTE2Mzc@._V1_.jpg')

st.title("3.Video")
d=open("C:\\Users\\SHREENATH S HEBBAR\\Videos\\1578318-hd_1920_1080_30fps.mp4",'rb')
st.video(d)


st.title("4.Audio")
audio=open("C:\\Users\\SHREENATH S HEBBAR\\Videos\\mixkit-fire-spell-with-explosion-1338.wav",'rb')
st.audio(audio)

st.title("5.Displaying the Data Frame")
df=pd.read_csv("D:\Csv files\Superstore sales.csv")
st.dataframe(df.head())

st.title("6.Displaying the  head Data Frame")

st.dataframe(df.head())
st.title("6.Displaying the tail Data Frame")

st.dataframe(df.tail())

st.title("7 .Displaying the Data Frame as a Table")

st.table(df.head())

st.title("8.File uploading")
img=st.file_uploader('Upload image',type=['png','jpg'])
if img is not None:
   
    file={'filename':img.name,'file_type':img.type,'file_size':img.size}
    st.write(file)
    st.image(Image.open(img))

st.title("9.Audio uploading")
img=st.file_uploader('Upload image',type=['wav','mp3'])
if img is not None:
   
    file={'filename':img.name,'file_type':img.type,'file_size':img.size}
    st.write(file)
    st.audio(img)


st.title("10. Video uploading")
img=st.file_uploader('Upload image',type=['mov','mp4'])
if img is not None:
   
    file={'filename':img.name,'file_type':img.type,'file_size':img.size}
    st.write(file)
    st.video(img)

st.title("11. Image Converter")

def convert_image(image_path,new1):
    with Image.open(image_path) as img:
        img=img.convert("RGB")
        n1=image_path.name.split('.')[0]+'.'+new1
       
        d = "C:\\Users\\SHREENATH S HEBBAR\\Pictures\\" + n1

        img.save(d)
        

img1=st.file_uploader("Upload your Image",type=["jpeg","png"])

new=st.selectbox("Select the output format",['png','jpeg','jpg'])
if st.button("convert"):
    if img1 is not None:
        convert_image(img1,new)
    else:
        st.error("please upload file")


st.title("Image Rotator")
st.subheader("Upload an image")

def rotate(image,angle):
    img=np.array(image)
    height,width=img.shape[:2]
    M=cv.getRotationMatrix2D((width/2,height/2),angle,1)
    rotated_img=cv.warpAffine(img,M,(width,height))
    return rotated_img

img2=st.file_uploader("Upload your Image",type=["jpeg","png"],key='image_rotator_uploader')
st.subheader("rotate the image")
angle=st.slider("Choose an angle",-180,180,0,1)

if img2 is not None:
    image=Image.open(img2)
    rotated=rotate(image,angle)
    st.image(rotated)