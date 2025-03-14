import streamlit as st
import pandas as pd

st.title('**AI-BASED TRAINER**')
st.image("action-athlete-barbell-841130.jpg", caption="This is a sample image", use_container_width=True)

st.header("Profile creation")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])

goal = st.selectbox('Select your goal: ', ['Muscle gain','Keep Fit','Weight Loss'])
body = st.multiselect('Select the focus muscle: ',['Chest','Back','Shoulder','Leg','Arm','Abs','Full body'])

exercise_routine = st.selectbox('Select your workout habit:', ['beginner', 'intemediate', 'advanced', 'professional'])

agree = st.checkbox("I agree to the terms")


if agree == True:
  
  st.sidebar.title("Personal Information")
  st.sidebar.write(f"Name: {name}")
  st.sidebar.write(f"Age: {age}")
  st.sidebar.write(f"Gender: {gender}")
  st.sidebar.write(f"Goal: {goal}")
  if len(body) >= 6:
    af = pd.DataFrame({'Muscle' : ['Full body']})
    with st.sidebar.expander('Muscle'):
      af
  else:
    af = pd.DataFrame({'Muscles': body})
    with st.sidebar.expander('Muscle'):
      af
  continue_button = st.checkbox('Next')
  ans = False
  for i in body:
    if i == 'Full body':
      ans = True
  if continue_button == True:
    if ans!=True:
      for i in body:



        
        if i == 'Chest':
          exc = pd.DataFrame({'Exercise':['Regular push-ups','Diamond push-ups','Barbell Bench Press','Incline Barbell Bench Press'],
                              'Reps' : [20,15,8,10],
                              'Sets' : [4,3,4,5]
                             })
          with st.expander('Chest'):
            exc
        if i == 'Back':
          exc = pd.DataFrame({'Exercise':['Pull-ups (Weighted or Bodyweight','Chin-ups','Dumbbell Rows','Deadlifts'],
                              'Reps' : [12,10,12,4],
                              'Sets' : [3,3,4,5]
                             })
          with st.expander('Back'):
            exc
        if i == 'Shoulder':
          exc = pd.DataFrame({'Exercise':['Barbell Overhead Press','Dumbbell Shoulder Press ','Lateral Raises','Upright Rows'],
                              'Reps' : [8,10,12,10],
                              'Sets' : [4,4,4,3]
                             })
          with st.expander('Shoulder'):
            exc
        if i == 'Arm':
          exc = pd.DataFrame({'Exercise':['Preacher Curls','Dumbbell Bicep Curls','Overhead Triceps Extensions','Hammer Curls'],
                              'Reps' : [12,11,8,10],
                              'Sets' : [3,3,3,3]
                             })
          with st.expander('Arm'):
            exc
        if i == 'Abs':
          exc = pd.DataFrame({'Exercise':['Plank','Reverse Crunches ','Decline Sit-ups','Russian Twists'],
                              'Reps' : ['45 seconds',10,12,4],
                              'Sets' : [3,3,4,5]
                             })
          with st.expander('Abs'):
            exc
         if i == 'Leg':
          exc = pd.DataFrame({'Exercise':['Leg Press','Barbell Squats ','Bulgarian Split Squats','Seated Hamstring Curls ],
                              'Reps' : ['45 seconds',10,12,4],
                              'Sets' : [3,3,4,5]
                             })
          with st.expander('Leg'):
            exc




    
    else:



      
      exc = pd.DataFrame({'Exercise':['Regular push-ups','Diamond push-ups','Barbell Bench Press','Incline Barbell Bench Press'],
                              'Reps' : [20,15,8,10],
                              'Sets' : [4,3,4,5]
                             })
      with st.expander('Chest'):
        exc
      exc = pd.DataFrame({'Exercise':['Pull-ups (Weighted or Bodyweight','Chin-ups','Dumbbell Rows','Deadlifts'],
                              'Reps' : [12,10,12,4],
                              'Sets' : [3,3,4,5]
                             })
      with st.expander('Back'):
        exc
      exc = pd.DataFrame({'Exercise':['Barbell Overhead Press','Dumbbell Shoulder Press ','Lateral Raises','Upright Rows'],
                              'Reps' : [8,10,12,10],
                              'Sets' : [4,4,4,3]
                             })
      with st.expander('Shoulder'):
        exc
      exc = pd.DataFrame({'Exercise':['Preacher Curls','Dumbbell Bicep Curls','Overhead Triceps Extensions','Hammer Curls'],
                              'Reps' : [12,11,8,10],
                              'Sets' : [3,3,3,3]
                             })
      with st.expander('Arm'):
        exc
      exc = pd.DataFrame({'Exercise':['Plank','Reverse Crunches ','Decline Sit-ups','Russian Twists'],
                              'Reps' : ['45 seconds',10,12,4],
                              'Sets' : [3,3,4,5]
                             })
      with st.expander('Abs'):
        exc
      exc = pd.DataFrame({'Exercise':['Leg Press','Barbell Squats ','Bulgarian Split Squats','Seated Hamstring Curls ],
                              'Reps' : ['45 seconds',10,12,4],
                              'Sets' : [3,3,4,5]
                             })
      with st.expander('Leg'):
        exc

      
      
      

        
        
    


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
  
