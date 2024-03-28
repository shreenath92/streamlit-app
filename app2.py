import streamlit as st
from datetime import datetime
st.subheader("1.Text input")
d=st.text_input("enter your name")
st.write('hello',d)
st.subheader("2.Text area")
st.text_area("Tell me something about yourself in 100 words",height=200,max_chars=500,help='Makimum 500 characters are allowed')
st.subheader('3.Password')
st.text_input('enter your password',type="password",help="At least have 9 characters")
st.subheader('4.Numeric Input')
st.number_input('enter your age',min_value=0,max_value=110,step=1,value=24)
st.subheader("5. Date input")
time=datetime.now().date()
date=st.date_input("Enter your date",value=time,min_value=time,max_value=time.replace(year=time.year+1))
st.write("you have selected",datetime.strftime(date,'%d/%m/%Y'))

st.subheader("6.Gender")
gender=st.radio("Select your gender",options=('male','female','other'),help='Choose one',horizontal=True)
st.write("You have selected a gender",gender)
st.subheader("7.Select box")
option=st.selectbox("Select your option",options=('data analysis','ML','DL','AI'),help='Choose one')
st.write(option)
st.subheader("8. multiselect box")
options=st.multiselect("Select your option",options=('data analysis','ML','DL','AI'),help='Choose multiple',default="data analysis")
st.subheader("9. Button")
st.button("Say Hello")
st.subheader("10. Checkbox")
st.checkbox("I agree to the terms and conditions",help="You must agree to proceed")
st.subheader("11.Color picker")
st.color_picker("Submit your response")


st.subheader("12. BMI Calculator or Rate yourself")
def bmi():
    with st.form("BMI calculator"):
        col1,col2,col3=st.columns([3,2,1])
    with col1:
        weight=st.number_input("Enter your weight in kg")
    with col2:
        height=st.number_input("Enter your height in Meters")
    with col3:
        d=st.form_submit_button('Calculate')
    if d:
        bmi=round((weight/(height**2)),2)
        if(bmi<=18.5):
            st.error('Underweight')
        elif bmi>18.5 and bmi<=24.9:
            st.success("Healthy and normal")
        elif(bmi>24.9):
            st.warning("Overweight")
def rate_yourself():
    with st.sidebar:
        st.title('Rate Yourself')
        languages = st.text_input('Enter the programming languages you know with comma separation',)
        languages = [i.strip() for i in languages.split(',')]

    st.subheader('How would you rate your experience in the following programming languages & tools?')

    for language in languages:
        #st.write(language)
        st.slider(language, min_value=0., max_value=10., step=2.0)
ch = st.sidebar.selectbox("Menu", ['BMI', 'Rate Yourself'])

if ch == 'BMI':
    bmi()
elif ch == 'Rate Yourself':
    rate_yourself()
