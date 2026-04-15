import streamlit as st

st.title("Basic Info")
st.divider()
name= st.text_input("Enter your name")
password = st.text_input("Enter your password",type="password")

pressed=st.button("Enter to confirm", type='primary')

if(pressed):
    st.write(f"Your name is {name} and your is {password}.")
