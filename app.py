import streamlit as st
import requests

# -----------------------------
# PAGE
# -----------------------------

st.set_page_config(
    page_title="24 Updates",
    page_icon="⚡",
    layout="centered"
)

# -----------------------------
# STYLE
# -----------------------------

st.markdown("""
<style>

.stApp {
    background: #212121;
    color: #ECECEC;
}

.main .block-container {
    max-width: 750px;
    padding-top: 60px;
}

.title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #A0A0A0;
    margin-bottom: 35px;
}

.stTextInput input {
    background: #2A2A2A !important;
    color: #ECECEC !important;
    border: 1px solid #444 !important;
    border-radius: 12px !important;
}

.stButton button {
    width: 100%;
    background: #10A37F;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-weight: 600;
}

.stButton button:hover {
    background: #0D8F71;
}

.response {
    background: #2A2A2A;
    border: 1px solid #3F3F3F;
    border-radius: 15px;
    padding: 22px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="title">⚡ 24 Updates</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter your Gemini API key and ask anything'
    '</div>',
    unsafe_allow_html=True
)

# -----------------------------
# API KEY INPUT
# -----------------------------

api_key = st.text_input(
    "🔑 Gemini API Key",
    type="password",
    placeholder="Enter your Gemini API key"
)

# -----------------------------
# USER QUESTION
# -----------------------------

question = st.text_input(
    "💬 Your Question",
    placeholder="Example: What are today's cricket updates?"
)

# -----------------------------
# BUTTON
# -----------------------------

if st.button("✨ Generate Response"):

    if not api_key.strip():

        st.warning("Please enter your Gemini API key.")

    elif not question.strip():

        st.warning("Please enter your question.")

    else:

        url = (
            "https://generativelanguage.googleapis.com/"
            "v1beta/models/gemini-2.5-flash:generateContent"
        )

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": api_key
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": question
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

        with st.spinner("Generating response..."):

            try:

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

                    st.markdown(
                        '<div class="response">',
                        unsafe_allow_html=True
                    )

                    st.markdown("### ⚡ Response")

                    st.markdown(answer)

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

                else:

                    st.error(
                        f"API Error: {response.text}"
                    )

            except Exception as e:

                st.error(
                    f"Connection error: {e}"
                )
