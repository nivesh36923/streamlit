import streamlit as st
import pandas as pd

st.title('**AI-BASED TRAINER**')
st.image("https://www.bing.com/images/search?view=detailV2&ccid=EwbatycH&id=F8232BED53A0BDD892070DC897489BFE224533D0&thid=OIP.EwbatycHx_915hcNzd7vRgHaE8&mediaurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F841130%2Fpexels-photo-841130.jpeg%3Fcs%3Dsrgb%26dl%3Daction-athlete-barbell-841130.jpg%26fm%3Djpg&exph=3289&expw=4933&q=gym+photos&simid=607995940842454132&ck=6E91FC162CAB1EB5C6D6098FA9B65681&selectedindex=0&itb=0&ajaxhist=0&ajaxserp=0&vt=0&sim=11&shtc=0&shth=OIP.EwbatycHx_915hcNzd7vRgHaE8&shsc=idp&form=EX0023&shid=c22b7fe0-8025-4b9c-b601-c47f05973761&shtp=copyUrl&shtk=MjAwKyBFbmdhZ2luZyBHeW0gUGhvdG9zIMK3IFBleGVscyDCtyBGcmVlIFN0b2NrIFBob3Rvcw%3D%3D&shdk=Rm91bmQgb24gQmluZyBmcm9tIHd3dy5wZXhlbHMuY29t&shhk=oQUuTpL%2FCrhtqW8r5d8m0dL0Q1kSZPx26XjqiaoLRas%3D", caption="Image from URL", use_column_width=True)
st.write('Give the answers of all the questions')

age = st.slider("Select your age", 1, 100, 25)
st.write(f"You selected {age} years old.")

df = pd.DataFrame({
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8]
})

st.write("DataFrame Example:")

df


name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
agree = st.checkbox("I agree to the terms")

if agree == True:
  st.write('welcome',name)

  if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old and identify as {gender}.")
  
