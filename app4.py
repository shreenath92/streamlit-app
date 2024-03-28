import time
import numpy as np
import streamlit as st
import pandas as pd
st.set_page_config(page_title="Shreenath")

tab1, tab2 = st.tabs(["Cat", "Dog"])
tab1.image("https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg")
tab2.image("https://t3.ftcdn.net/jpg/06/10/71/64/360_F_610716498_li6BIgt75TXw8B4W89pbf3VtKgHNQkXo.jpg")

img = pd.read_csv("C:\\Users\\SHREENATH S HEBBAR\\Documents\\python\\web_scrapping\\imagelink.csv")['link']
tabs = st.tabs(["ID"] * 30)

for tab in tabs:
    with tab:
        imgs = img[np.random.randint(1, 160)]
        st.image(imgs) 

cases=[]
for i in range(36):
    cases.append(np.random.randint(1,7))
st.write(cases)
data=[]
for i in range(1,7):
    data.append(cases.count(i))
st.header("Frequency of getting a no in dice")

st.bar_chart({"Data":data})

with st.expander(" See Explanation"):
    st.write('''
             The chart shows about numbers i got from rolling a dice 100 times
             and its basically about how many times each face appears ''')
    st.image("https://df0b18phdhzpx.cloudfront.net/ckeditor_assets/pictures/1154563/original_573935_Question_Dice.png")

with st.empty():
    st.write("You need to wait for 10 seconds")
    for seconds in range(11):
        st.write('🚀'+str(seconds)+'seconds remained')
        time.sleep(1)
    st.write("10 seconds completed")


with st.spinner("Wait for it"):
    time.sleep(5)
    st.write("Thanks for being Patient")
with st.empty():
    for per in range(100):
        time.sleep(.1)
        st.progress(per+1,'Processing')
    st.success("Completed")
st.balloons()
st.snow()
st.