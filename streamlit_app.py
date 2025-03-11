import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
agree = st.checkbox("I agree to the terms")
