import streamlit as st

st.title('**Streamlit Tutorial**')

st.write('Give the answers of all the questions')

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
agree = st.checkbox("I agree to the terms")

if agree == True:
  st.write('welcome',name)

  if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old and identify as {gender}.")
  
