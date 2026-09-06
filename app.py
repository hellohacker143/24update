import os
import streamlit as st
from google import genai

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Charans LLM",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# API Key
# -----------------------------
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ GEMINI_API_KEY is not configured.")
    st.info("Set your Gemini API key as an environment variable and restart Streamlit.")
    st.stop()

# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.6-flash"

# -----------------------------
# UI
# -----------------------------
st.title("🤖 Charans LLM")
st.caption("Powered by Gemini")

prompt = st.text_area(
    "Ask anything",
    placeholder="Type your question here...",
    height=150
)

if st.button("Generate", use_container_width=True):

    if not prompt.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Thinking..."):

        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            st.subheader("Response")
            st.write(response.text)

        except Exception as e:
            st.error("API Error")
            st.code(str(e))
