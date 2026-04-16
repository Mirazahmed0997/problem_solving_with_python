import streamlit as st

num1=st.number_input("Enter your first number",value=None)
num2=st.number_input("Enter your second Number",value=None)

selected=st.selectbox("Choose your operation",("+","-","*","/"),index=None,placeholder="Select")

pressed=st.button("Enter to confirm", type='primary')



if pressed:
    if selected == '+':
        st.write(num1 + num2)

    elif selected == '-':
        st.write(num1 - num2)

    elif selected == '*':
        st.write(num1 * num2)

    elif selected == '/':
        if num2 != 0:
            st.write(num1 / num2)
        else:
            st.error("Cannot divide by zero")
