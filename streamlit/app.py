from google import genai
import os 
from dotenv import load_dotenv
import streamlit as st




load_dotenv()

api_key=os.environ.get("GEMINI_API_KEY")

text=st.text_input("Ask anytinhg to Miraz")

client=genai.Client(api_key=api_key) 

response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=text
)

st.markdown(response.text)

