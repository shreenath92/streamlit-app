import streamlit as st
import numpy as np
import pandas as pd
st.title("Line chart")
chart=pd.DataFrame(np.random.randn(20,4),columns=['l1','l2','l3','l4'])
st.line_chart(chart)

st.title("2.Area Chart")
st.area_chart(chart)

st.title("3.Bar Chart")
st.bar_chart(chart)
