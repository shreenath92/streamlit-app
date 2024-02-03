from matplotlib import figure
import streamlit as st
import  pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
chart=pd.DataFrame(np.random.randn(20,3),columns=["line1","line2","line3"])
st.subheader("Line chart")
st.line_chart(chart)
st.subheader("area chart")
st.area_chart(chart)
st.subheader("bar chart")
st.bar_chart(chart)
st.subheader("2 data visulaization with matplotlib and seaborn")
st.subheader("Loading the data frame")
df=pd.read_csv("D:\\Iris_data_sample.csv")
st.dataframe(df)
st.subheader("distribution plot")
fig=plt.figure(figsize=(15,8))
df["Species"].value_counts().plot(kind='bar')
st.pyplot(fig)
st.write(df["Species"].value_counts())
st.subheader("distribution plot with seaborn")
fig=plt.figure(figsize=(15,8))
st.write(df.columns)
sns.displot(df["Species"])
st.pyplot(fig)
st.subheader("multiple graphs")
col1,col2=st.columns(2)
with col1:
    col1.header="KDE=False"
    col1.write("KDE=False")
    fig1=plt.figure()
    sns.displot(df["SepalLengthCm"])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    

               

st.subheader("altair Sacatter plot")
chart=pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart1=alt.Chart(chart).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart1)
st.subheader("interactive charts")
lang=df.columns.tolist()
choice=st.multiselect("choose your language",lang)
new=df[choice]
st.line_chart(new)
st.subheader("ARea chart")
st.area_chart(new)
st.write(df.head())

st.subheader("data visualization with plotly")
fig=px.pie(df,values="SepalLengthCm",names="Species")
st.plotly_chart(fig)
fig=px.pie(df,values="SepalLengthCm",names="Species",opacity=.9,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)