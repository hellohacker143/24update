import streamlit as st
from google import genai

st.set_page_config(
    page_title="24 Updates",
    page_icon="⚡"
)

st.title("⚡ 24 Updates")
st.caption("Cricket • Movies • News • Jobs")

# API key
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Category
category = st.selectbox(
    "Select Category",
    [
        "🏏 Cricket",
        "🎬 Movies",
        "📰 News",
        "💼 Jobs"
    ]
)

# Time
time = st.selectbox(
    "Updates",
    ["Last 24 Hours", "Last 48 Hours"]
)

# Search
question = st.text_input(
    "Search",
    placeholder="Ask anything..."
)

if st.button("Get Updates"):

    prompt = f"""
Give me the latest {category} updates from the {time}.

Give 5 important updates.

Keep each update simple:

1. Title
2. Short 2-line summary
3. Date/time if available

Do not make up information.
"""

    if question:
        prompt += f"""

User wants to know:
{question}
"""

    with st.spinner("Getting updates..."):

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

    st.markdown("### Latest Updates")
    st.write(response.text)
