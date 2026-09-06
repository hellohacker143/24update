import streamlit as st
import requests

st.set_page_config(
    page_title="24 Updates",
    page_icon="⚡"
)

st.title("⚡ 24 Updates")
st.caption("Ask anything about Cricket, Movies, News or Jobs")

# API key from Streamlit Secrets
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    st.error("Add GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# Simple input
user_input = st.text_input(
    "Ask your question",
    placeholder="Example: What are today's cricket updates?"
)

if st.button("Get Response"):

    if not user_input.strip():
        st.warning("Please enter something.")
        st.stop()

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-2.5-flash:generateContent"
    )

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_input
                    }
                ]
            }
        ],
        "tools": [
            {
                "google_search": {}
            }
        ]
    }

    with st.spinner("Thinking..."):

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

    if response.status_code == 200:

        result = response.json()

        answer = (
            result["candidates"][0]
            ["content"]["parts"][0]
            ["text"]
        )

        st.divider()
        st.markdown("### ⚡ Response")
        st.markdown(answer)

    else:

        st.error(
            f"API Error: {response.text}"
        )
