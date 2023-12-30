


import streamlit as st
import os
import requests


st.set_page_config(layout="wide")

st.write("---")
col1, col2, col3,col4, col5 = st.columns([1,1,1,1,1])
with col3:
    st.header("STREAMLIT")

st.write("---")


st.subheader("Welcome To Streamlit Tutorial")

st.write('* This is my sample and first streamlit app.')

st.write('* streamlit is a python library.')

st.write('* If you want to learn more about STREAMLIT tutorial/Documentation click below.')

st.write("[Click Here](https://docs.streamlit.io/library/cheatsheet)")

st.write("* Click below for STREAMLIT tutorial from GeeksForGeeks website.")

st.write("[Click Here](https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/)")

st.write("##")
st.write("##")


col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
with col5:
    st.write("M.Prasanth Kumar Reddy")

st.balloons()
    
