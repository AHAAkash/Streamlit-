import streamlit as st
from datetime import datetime
# This code creates a simple user information form using Streamlit
st.title("User Information Form:")
st.subheader("Please fill out the form below:")

form_values ={
    "name": None,
    "height": None,    
    "gender": None,
    "dob": None
}
min_date = datetime(1900, 1, 1)
max_date = datetime.now()
with st.form(key='user_info_form'):
    form_values["name"] = st.text_input("Enter your name")
    form_values["height"] = st.number_input("Enter your height (cm)", min_value=0, max_value=300)
    form_values["gender"] = st.selectbox("Gender",["Male","Female"] )
    form_values["dob"] = st.date_input("Date of Birth", max_value=max_date, min_value=min_date)
  
    submit_button = st.form_submit_button("Submit")
    if submit_button:
      if not all(form_values.values()):
          st.error("Please fill out all fields.")
      else:
        st.balloons()
        st.write("### Info")
        for key, value in form_values.items():
            st.write(f"{key}: {value}")