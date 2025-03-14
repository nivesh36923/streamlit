import streamlit as st
import pandas as pd

st.title('**AI-BASED TRAINER**')
st.image("action-athlete-barbell-841130.jpg", caption="This is a sample image", use_container_width=True)

st.header("Profile creation")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])

what = st.selectbox('Select your goal: ', ['Muscle gain','Keep Fit','Weight Loss'])


exercise_routine = st.selectbox('Select your workout habit:', ['beginner', 'intemediate', 'advanced', 'professional'])

agree = st.checkbox("I agree to the terms")

# st.sidebar.title("Personal Information")
# # age = st.slider("Select your age", 1, 100, 25)
# st.write(f"You selected {age} years old.")

# df = pd.DataFrame({
#     "A": [1, 2, 3, 4],
#     "B": [5, 6, 7, 8]
# })

# st.write("DataFrame Example:")

# df




# if agree == True:
#   st.write('welcome',name)

#   if st.button("Submit"):
#     st.write(f"Hello, {name}! You are {age} years old and identify as {gender}.")
  
