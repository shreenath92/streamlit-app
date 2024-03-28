import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

st.title("Data Visualization with seaborn and Matplotib")
df=pd.read_csv("D:\Csv files\Iris_data_sample.csv")
st.text("1.Displaying the Data Set")
st.dataframe(df)


st.text("2.Bar plot using Matplotlib")
fig=plt.figure(figsize=(15,8))
df["Species"].value_counts().plot(kind="bar")
st.pyplot(fig)


st.text("3.displot using seaborn")
fig=plt.figure(figsize=(15,8))
df["SepalLengthCm"] = pd.to_numeric(df["SepalLengthCm"], errors="coerce")
df = df.dropna(subset=["SepalLengthCm"])

sns.distplot(df["SepalLengthCm"])
st.pyplot(fig)

st.text('4.Displaying Multiple Graphs')
col1,col2=st.columns([1,1])
with col1:
    
    col1.write("KDE is False")
    fig1=plt.figure()
    sns.distplot(df["SepalLengthCm"],kde=False)
    st.pyplot(fig1)

with col2:
    col2.write("Hist is False")
    fig2=plt.figure()
    sns.distplot(df["SepalLengthCm"],hist=False)
    st.pyplot(fig2)


st.text("5. ScatterPLot")
fig=plt.figure(figsize=(15,8))
plt.scatter( *np.random.random(size=(2,100)))
st.pyplot(fig)

st.text("5.Count plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df)
st.pyplot(fig)

st.text("6.box plot")
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x="Species",y="SepalLengthCm")
st.pyplot(fig)

st.text("7.violin plot")
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x="Species",y="SepalLengthCm")
st.pyplot(fig)


st.text("Visulaization using Plotly")
st.text("1.Pie")
fig=px.pie(df,values="SepalLengthCm",names="Species")
st.plotly_chart(fig)

st.text("2.Pie chart type with hole")
fig=px.pie(df,values="SepalLengthCm",names="Species",opacity=.7,hole=.5,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)


st.title("Interactive graphs with with plotly")
x1=np.random.randn(200)+2
x2=np.random.randn(200)
x3=np.random.randn(200)-2
hist=[x1,x2,x3]
labels=['G1','G2','G3']
fig=ff.create_distplot(hist,labels,bin_size=[.5,.2,.3])
st.plotly_chart(fig)

