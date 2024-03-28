import time
import numpy as np
import streamlit as st

col1,col2,col3=st.columns([1,1,1])
with col1:
    st.header("Cat")
    st.image("https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg")
with col2:
    st.header("Dog")
    st.image("https://t3.ftcdn.net/jpg/06/10/71/64/360_F_610716498_li6BIgt75TXw8B4W89pbf3VtKgHNQkXo.jpg")
with col3:
    st.header("Owl")
    st.image("https://images.pexels.com/photos/86596/owl-bird-eyes-eagle-owl-86596.jpeg?cs=srgb&dl=pexels-pixabay-86596.jpg&fm=jpg")
n=int(st.number_input("Enter the number of input u want to display",1,10))
cols=st.columns(n)
for col in cols:
    with col:
        st.image("https://t3.ftcdn.net/jpg/06/10/71/64/360_F_610716498_li6BIgt75TXw8B4W89pbf3VtKgHNQkXo.jpg")