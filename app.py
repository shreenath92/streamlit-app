import streamlit as st
st.title("hello Geeks, how are u")
st.header("header -> Geeks for geeks")
st.subheader("subheader -> Geeks for geeks")
st.text('Text-> geeks for geeks')
st.markdown('##HI')
st.markdown('##HI')
st.markdown('###HI')
st.success("data is succesful")
st.info("information")
st.warning("warning")
st.error("Error!")
exp=ZeroDivisionError("divison not posdsible with zero")
st.exception(exp)
st.help(ZeroDivisionError)
st.write(range(1,10))
st.write(1+2+3+4)
st.write('1+2+3+4')
st.code('x=10\n'
        'for i in range(1,10):\n'
        '\tprint(i)')
st.checkbox("male")
st.checkbox("female")
if(st.checkbox("adult")):
    st.write("you are an adult")
rd=st.radio("select",("male","female","other"))
if(rd=="male"):
    st.write("you are an male")
elif(rd=="female"):
   st.write("you are female")
elif(rd=="other"):
    st.write("you are other gender")
st.subheader("select box")
box=st.selectbox("data Science",("data analysis","web scrapping","machine learning","Deep learning","Computer Vison","Image proceesing"))
st.write("you have selected a select box0",box)
st.subheader("Multi select box")
multi=st.multiselect("data Science",("data analysis","web scrapping","machine learning","Deep learning","Computer Vison","Image proceesing"))
st.write("you have selected a select box0",multi)
st.subheader("button")
if(st.button("click me")):
    st.write("thx for clicking")
st.slider("select volume",1,100,step=2)
st.subheader("text input")
st.text_input("name:")
password=st.text_input("password:","")
st.subheader("text area")
test=st.text_area("write about yourself in 100",height=2)
st.subheader("number input")
st.number_input("enter no")
st.subheader("Input date")
st.date_input("date")
st.subheader("Input time")
st.time_input("time")