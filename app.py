import streamlit as st
import requests

# =========================================================
# PAGE
# =========================================================

st.set_page_config(
    page_title="24 Updates",
    page_icon="⚡",
    layout="wide"
)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #212121;
    color: #ECECEC;
}

[data-testid="stHeader"] {
    background: #212121;
}

[data-testid="stSidebar"] {
    background: #171717;
}

.main .block-container {
    max-width: 1050px;
    padding-top: 35px;
}

.title {
    font-size: 42px;
    font-weight: 700;
    letter-spacing: -1px;
}

.subtitle {
    color: #A0A0A0;
    margin-bottom: 25px;
}

.card {
    background: #2A2A2A;
    border: 1px solid #3F3F3F;
    border-radius: 16px;
    padding: 22px;
    margin-top: 20px;
}

.stButton button {
    background: #10A37F;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

.stButton button:hover {
    background: #0D8F71;
}

.stTextInput input {
    background: #2A2A2A !important;
    color: white !important;
    border: 1px solid #3F3F3F !important;
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# API KEY
# =========================================================

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error(
        "GEMINI_API_KEY is missing. "
        "Add it in Streamlit Cloud → Manage app → Settings → Secrets."
    )
    st.stop()

# =========================================================
# GEMINI + GOOGLE SEARCH
# =========================================================

def ask_gemini(prompt):

    url = (
        "https://generativelanguage.googleapis.com/"
        "v1beta/models/gemini-3.7-flash:generateContent"
    )

    headers = {
        "x-goog-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    data = {
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

    try:

        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

        if response.status_code != 200:
            return None, f"Gemini API Error: {response.text}"

        result = response.json()

        text = (
            result
            .get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "")
        )

        if not text:
            return None, "No response was returned."

        return text, None

    except requests.exceptions.Timeout:
        return None, "Request timed out. Please try again."

    except Exception as e:
        return None, str(e)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ⚡ 24 Updates")

    st.caption(
        "Live AI-powered updates"
    )

    st.divider()

    time_range = st.radio(
        "Time Range",
        [
            "Last 24 Hours",
            "Last 48 Hours"
        ]
    )

    st.divider()

    st.caption(
        "Choose a category and get the latest information."
    )

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">⚡ 24 Updates</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Fresh Cricket • Movies • News • Jobs'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# CATEGORY
# =========================================================

category = st.selectbox(
    "Category",
    [
        "🏏 Cricket",
        "🎬 Movies",
        "📰 News",
        "💼 Jobs"
    ]
)

# =========================================================
# SEARCH
# =========================================================

question = st.text_input(
    "🔎 Search",
    placeholder="Ask about this category..."
)

# =========================================================
# GET UPDATES
# =========================================================

if st.button(
    "✨ Get Latest Updates",
    use_container_width=True
):

    if question.strip():

        user_request = question

    else:

        user_request = (
            f"Give me the most important {category} updates."
        )

    prompt = f"""
You are the live updates assistant for an application
called "24 Updates".

CATEGORY:
{category}

TIME RANGE:
{time_range}

USER REQUEST:
{user_request}

IMPORTANT:

Use Google Search to find current information.

Only include information that you can verify from
current web sources.

Give me 5 important updates.

For every update use this structure:

## Title

Short 2-3 sentence summary.

🕒 Published/Updated:
📌 Source:

Rules:

1. Prioritize information from the requested time range.
2. Do not present old information as new.
3. Do not invent facts.
4. Do not create fake source names.
5. If an item cannot be verified, leave it out.
6. Keep the response simple.
7. For Cricket, include match information and important
   player/team updates when available.
8. For Movies, include releases, trailers, OTT,
   Telugu cinema and box-office updates.
9. For News, prioritize India, Telangana and Hyderabad
   along with major national/world news.
10. For Jobs, prioritize fresh software jobs,
    internships, fresher opportunities, Hyderabad
    and remote jobs.
11. Clearly separate facts from predictions or opinions.
"""

    with st.spinner(
        f"Searching for latest {category} updates..."
    ):

        result, error = ask_gemini(prompt)

    if error:

        st.error(error)

    else:

        st.divider()

        st.markdown(
            f"## {category} — {time_range}"
        )

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        st.markdown(result)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "⚡ 24 Updates • Gemini + Google Search"
)
