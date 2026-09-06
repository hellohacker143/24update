import streamlit as st
from google import genai
from datetime import datetime

# =========================================================
# PAGE
# =========================================================

st.set_page_config(
    page_title="24 Updates",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# COLORS
# =========================================================

BG = "#212121"
SIDEBAR = "#171717"
CARD = "#2A2A2A"
CARD2 = "#303030"
TEXT = "#ECECEC"
MUTED = "#A0A0A0"
BORDER = "#3F3F3F"
GREEN = "#10A37F"

# =========================================================
# STYLE
# =========================================================

st.markdown(f"""
<style>

.stApp {{
    background:{BG};
    color:{TEXT};
}}

[data-testid="stHeader"] {{
    background:{BG};
}}

[data-testid="stSidebar"] {{
    background:{SIDEBAR};
    border-right:1px solid {BORDER};
}}

.main .block-container {{
    max-width:1100px;
    padding-top:35px;
    padding-bottom:70px;
}}

.logo {{
    font-size:27px;
    font-weight:700;
}}

.title {{
    font-size:40px;
    font-weight:700;
    letter-spacing:-1px;
    margin-bottom:5px;
}}

.subtitle {{
    color:{MUTED};
    font-size:15px;
    margin-bottom:25px;
}}

.update-card {{
    background:{CARD};
    border:1px solid {BORDER};
    border-radius:16px;
    padding:20px;
    margin-bottom:15px;
}}

.update-card:hover {{
    background:{CARD2};
    border-color:#555;
}}

.badge {{
    display:inline-block;
    background:#383838;
    padding:5px 10px;
    border-radius:20px;
    color:#D5D5D5;
    font-size:12px;
    margin-bottom:10px;
}}

.update-title {{
    font-size:19px;
    font-weight:600;
    margin-bottom:8px;
}}

.update-text {{
    color:#B8B8B8;
    line-height:1.6;
    font-size:14px;
}}

.time {{
    color:#888;
    font-size:12px;
    margin-top:14px;
}}

.stTextInput input {{
    background:#2A2A2A !important;
    color:{TEXT} !important;
    border:1px solid {BORDER} !important;
    border-radius:12px !important;
}}

.stTextInput input:focus {{
    border-color:{GREEN} !important;
}}

.stButton button {{
    border-radius:10px;
    border:1px solid {BORDER};
    background:{CARD};
    color:{TEXT};
}}

.stButton button:hover {{
    border-color:{GREEN};
    color:white;
}}

.footer {{
    text-align:center;
    color:#777;
    font-size:12px;
    margin-top:40px;
}}

</style>
""", unsafe_allow_html=True)

# =========================================================
# GEMINI CLIENT
# =========================================================

try:
    API_KEY = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(
        api_key=API_KEY
    )

except Exception:
    client = None

# =========================================================
# CATEGORY PROMPTS
# =========================================================

PROMPTS = {

    "🏏 Cricket": """
Give me the latest cricket updates.

Cover:
- Today's important matches
- Upcoming matches
- Recent results
- Major player updates
- Team news
- Important tournaments

Return 6 concise updates.

For every update use this format:

TITLE:
SUMMARY:
TIME:

Do not invent current events.
If you cannot verify something as current, say that it could not be verified.
""",

    "🎬 Movies": """
Give me the latest movie and entertainment updates.

Cover:
- New movie announcements
- Trailers
- Releases
- OTT releases
- Box office
- Telugu cinema
- Major Indian cinema updates

Return 6 concise updates.

For every update use:

TITLE:
SUMMARY:
TIME:

Do not invent current information.
""",

    "📰 News": """
Give me the most important latest news.

Focus on:
- India
- Telangana
- Hyderabad
- Technology
- Business
- Major world events

Return 6 concise updates.

For every update use:

TITLE:
SUMMARY:
TIME:

Do not invent current information.
""",

    "💼 Jobs": """
Give me the latest job and internship opportunities.

Focus on:
- Software jobs
- Full Stack jobs
- Python jobs
- AI/ML jobs
- Internships
- Fresher opportunities
- Hyderabad
- Remote opportunities

Return 6 concise updates.

For every update use:

TITLE:
SUMMARY:
TIME:

Do not invent job postings or application links.
If a job cannot be verified, clearly say so.
"""
}

# =========================================================
# GEMINI FUNCTION
# =========================================================

def get_updates(category, time_range):

    if client is None:
        return "Gemini API key is not configured."

    prompt = PROMPTS[category]

    prompt += f"""

The user selected:

Time range: {time_range}

Current date and time:
{datetime.now().strftime("%d %B %Y, %I:%M %p")}

Give the answer in clean Markdown.
Keep each update short and easy to read.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini API error: {str(e)}"

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="logo">⚡ 24 Updates</div>',
        unsafe_allow_html=True
    )

    st.caption("Your AI-powered updates assistant")

    st.divider()

    time_range = st.radio(
        "Time range",
        [
            "24 Hours",
            "48 Hours"
        ]
    )

    st.divider()

    st.markdown("### Categories")

    category = st.selectbox(
        "Select",
        [
            "🏏 Cricket",
            "🎬 Movies",
            "📰 News",
            "💼 Jobs"
        ]
    )

    st.divider()

    refresh = st.button(
        "🔄 Get Latest Updates",
        use_container_width=True
    )

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">24 Updates</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Fresh updates powered by Gemini'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# SEARCH
# =========================================================

search = st.text_input(
    "🔎 Search",
    placeholder="Ask about this category..."
)

# =========================================================
# CATEGORY BUTTONS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

buttons = [
    ("🏏 Cricket", col1),
    ("🎬 Movies", col2),
    ("📰 News", col3),
    ("💼 Jobs", col4)
]

for name, col in buttons:

    with col:

        if st.button(
            name,
            use_container_width=True
        ):

            category = name
            st.rerun()

# =========================================================
# MAIN CONTENT
# =========================================================

st.divider()

st.markdown(
    f"## {category}"
)

st.caption(
    f"Latest {time_range} • AI-generated summary"
)

# =========================================================
# GET RESPONSE
# =========================================================

if "result" not in st.session_state:
    st.session_state.result = None

if refresh or st.session_state.result is None:

    with st.spinner(
        f"Fetching {category} updates..."
    ):

        st.session_state.result = get_updates(
            category,
            time_range
        )

# =========================================================
# SEARCH MODE
# =========================================================

if search:

    with st.spinner("Searching with Gemini..."):

        search_prompt = f"""
You are the assistant inside a current updates application.

Category:
{category}

User query:
{search}

Time range:
{time_range}

Give a concise useful answer.

Do not invent current events.
Clearly distinguish verified facts from predictions or analysis.
"""

        try:

            search_response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=search_prompt
            )

            st.markdown(search_response.text)

        except Exception as e:

            st.error(
                f"Search error: {str(e)}"
            )

else:

    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    st.markdown(
        '<div class="update-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state.result
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    ⚡ 24 Updates
    &nbsp;•&nbsp;
    Cricket
    &nbsp;•&nbsp;
    Movies
    &nbsp;•&nbsp;
    News
    &nbsp;•&nbsp;
    Jobs

    <br><br>

    Powered by Gemini

    </div>
    """,
    unsafe_allow_html=True
)
