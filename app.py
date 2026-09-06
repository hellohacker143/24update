import streamlit as st
from google import genai

API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hello"
)

st.write(response.text)
