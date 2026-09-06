import streamlit as st
from google import genai

st.set_page_config(page_title="Charans LLM")

st.title("🤖 Charans LLM")

api_key = st.secrets["AQ.Ab8RN6LW6A3HA71ENi7kV0QLfG-GKg9sIG2-21m-viFP-ccU_A"]

client = genai.Client(api_key=api_key)

user_input = st.text_input("Enter your question")

if st.button("Ask"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=user_input
            )

        st.write(response.text)
    else:
        st.warning("Please enter something.")
