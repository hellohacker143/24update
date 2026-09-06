import streamlit as st
import requests

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="24 Updates",
    page_icon="⚡",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: #212121;
    color: #ECECEC;
}

.main .block-container {
    max-width: 760px;
    padding-top: 55px;
}

h1 {
    text-align: center;
    font-size: 42px !important;
}

.subtitle {
    text-align: center;
    color: #A0A0A0;
    margin-bottom: 35px;
}

.card {
    background: #2A2A2A;
    border: 1px solid #3F3F3F;
    border-radius: 16px;
    padding: 24px;
    margin-top: 25px;
}

.stTextInput input {
    background: #2A2A2A !important;
    color: #ECECEC !important;
    border: 1px solid #444 !important;
    border-radius: 12px !important;
}

.stTextInput input:focus {
    border-color: #10A37F !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #2A2A2A;
    border-radius: 12px;
}

.stButton button {
    width: 100%;
    background: #10A37F;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
    padding: 10px;
}

.stButton button:hover {
    background: #0D8F71;
}

.footer {
    text-align: center;
    color: #777;
    font-size: 12px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("⚡ 24 Updates")

st.markdown(
    '<div class="subtitle">'
    'Cricket • Movies • News • Jobs'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# API KEY
# --------------------------------------------------

api_key = st.text_input(
    "🔑 Gemini API Key",
    type="password",
    placeholder="Enter your Gemini API key"
)

# --------------------------------------------------
# CATEGORY
# --------------------------------------------------

category = st.selectbox(
    "Category",
    [
        "🏏 Cricket",
        "🎬 Movies",
        "📰 News",
        "💼 Jobs"
    ]
)

# --------------------------------------------------
# TIME RANGE
# --------------------------------------------------

time_range = st.selectbox(
    "Time Range",
    [
        "Last 24 Hours",
        "Last 48 Hours"
    ]
)

# --------------------------------------------------
# QUESTION
# --------------------------------------------------

question = st.text_input(
    "💬 What do you want to know?",
    placeholder="Example: Give me today's cricket updates"
)

# --------------------------------------------------
# GEMINI REQUEST
# --------------------------------------------------

def generate_response(api_key, prompt):

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-2.5-flash:generateContent"
    )

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key
    }

    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
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

    response = requests.post(
        url,
        headers=headers,
        json=body,
        timeout=60
    )

    if response.status_code != 200:
        return None, response.text

    data = response.json()

    try:
        answer = data["candidates"][0]["content"]["parts"][0]["text"]
        return answer, None

    except (KeyError, IndexError):
        return None, "Gemini returned an unexpected response."

# --------------------------------------------------
# GENERATE BUTTON
# --------------------------------------------------

if st.button("✨ Generate Response"):

    if not api_key.strip():

        st.warning("Please enter your Gemini API key.")

    elif not question.strip():

        st.warning("Please enter your question.")

    else:

        prompt = f"""
You are the AI assistant for an application called 24 Updates.

Category:
{category}

Time range requested:
{time_range}

User question:
{question}

Give a clear and concise answer.

For current information:
- Use Google Search grounding when available.
- Prefer recent and reliable sources.
- Do not invent current events.
- Do not present old information as new.
- Clearly say when something cannot be verified.
- Keep the response easy to read.
- Include source information when available.
"""

        with st.spinner("Getting the latest response..."):

            try:

                answer, error = generate_response(
                    api_key,
                    prompt
                )

                if error:

                    st.error(
                        f"API Error: {error}"
                    )

                else:

                    st.markdown(
                        '<div class="card">',
                        unsafe_allow_html=True
                    )

                    st.markdown("### ⚡ Response")

                    st.markdown(answer)

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

            except requests.exceptions.Timeout:

                st.error(
                    "The request timed out. Please try again."
                )

            except requests.exceptions.RequestException:

                st.error(
                    "Could not connect to the Gemini API."
                )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        ⚡ 24 Updates<br>
        Powered by Gemini
    </div>
    """,
    unsafe_allow_html=True
)
