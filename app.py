import streamlit as st
from google import genai

# -------------------------
# Page
# -------------------------
st.set_page_config(
    page_title="Charans LLM",
    page_icon="🤖"
)

st.title("🤖 Charans LLM")
st.write("Ask anything")

# -------------------------
# API Key
# -------------------------
API_KEY = st.secrets["AQ.Ab8RN6LW6A3HA71ENi7kV0QLfG-GKg9sIG2-21m-viFP-ccU_A"]

client = genai.Client(api_key=API_KEY)

# -------------------------
# Input
# -------------------------
question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is Python?"
)

# -------------------------
# Generate Response
# -------------------------
if st.button("Ask", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Thinking..."):

                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=question
                )

            st.subheader("Answer")
            st.write(response.text)

        except Exception as e:
            st.error("Something went wrong.")
            st.code(str(e))
