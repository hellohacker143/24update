import streamlit as st
from datetime import datetime, timedelta

# =========================================================
# PAGE CONFIG
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
CARD_HOVER = "#303030"
TEXT = "#ECECEC"
MUTED = "#A0A0A0"
BORDER = "#3F3F3F"
GREEN = "#10A37F"
GREEN_DARK = "#0D8F71"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>

    /* MAIN APP */
    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    [data-testid="stHeader"] {{
        background: {BG};
    }}

    .main .block-container {{
        max-width: 1100px;
        padding-top: 35px;
        padding-bottom: 80px;
    }}

    /* SIDEBAR */
    [data-testid="stSidebar"] {{
        background: {SIDEBAR};
        border-right: 1px solid {BORDER};
    }}

    [data-testid="stSidebar"] * {{
        color: {TEXT};
    }}

    /* TITLE */
    .app-title {{
        font-size: 38px;
        font-weight: 700;
        letter-spacing: -1px;
        color: {TEXT};
        margin-bottom: 4px;
    }}

    .app-subtitle {{
        color: {MUTED};
        font-size: 15px;
        margin-bottom: 28px;
    }}

    /* CATEGORY BAR */
    .category-bar {{
        display: flex;
        gap: 8px;
        padding: 6px;
        background: #191919;
        border: 1px solid {BORDER};
        border-radius: 14px;
        margin-bottom: 25px;
        overflow-x: auto;
    }}

    .category-item {{
        padding: 9px 15px;
        border-radius: 9px;
        color: {MUTED};
        font-size: 14px;
        font-weight: 500;
        white-space: nowrap;
    }}

    .category-item.active {{
        background: {CARD};
        color: {TEXT};
    }}

    /* SECTION TITLE */
    .section-title {{
        font-size: 20px;
        font-weight: 600;
        color: {TEXT};
        margin: 20px 0 15px 0;
    }}

    /* UPDATE CARD */
    .update-card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 16px;
        padding: 21px;
        margin-bottom: 15px;
        transition: 0.2s ease;
        min-height: 175px;
    }}

    .update-card:hover {{
        background: {CARD_HOVER};
        border-color: #555555;
    }}

    .category-badge {{
        display: inline-block;
        background: #353535;
        color: #D5D5D5;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 12px;
        margin-bottom: 12px;
    }}

    .update-title {{
        color: {TEXT};
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 8px;
    }}

    .update-description {{
        color: #B8B8B8;
        font-size: 14px;
        line-height: 1.55;
        margin-bottom: 17px;
    }}

    .update-time {{
        color: #858585;
        font-size: 12px;
    }}

    /* SEARCH */
    .stTextInput input {{
        background: #2A2A2A !important;
        color: {TEXT} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
    }}

    .stTextInput input:focus {{
        border-color: {GREEN} !important;
        box-shadow: 0 0 0 1px {GREEN} !important;
    }}

    /* SELECT BOX */
    div[data-baseweb="select"] > div {{
        background: #2A2A2A;
        border-color: {BORDER};
        border-radius: 10px;
    }}

    /* RADIO */
    [data-testid="stSidebar"] .stRadio label {{
        color: {TEXT};
    }}

    /* BUTTON */
    .stButton button {{
        background: {GREEN};
        color: white;
        border: none;
        border-radius: 9px;
        font-weight: 600;
    }}

    .stButton button:hover {{
        background: {GREEN_DARK};
        color: white;
    }}

    /* DIVIDER */
    hr {{
        border-color: {BORDER};
    }}

    /* FOOTER */
    .footer {{
        text-align: center;
        color: #777777;
        font-size: 12px;
        margin-top: 40px;
    }}

    /* MOBILE */
    @media (max-width: 768px) {{

        .main .block-container {{
            padding: 20px 15px 60px 15px;
        }}

        .app-title {{
            font-size: 30px;
        }}

        .app-subtitle {{
            font-size: 14px;
        }}

        .update-card {{
            min-height: auto;
            padding: 17px;
        }}

        .update-title {{
            font-size: 17px;
        }}

        .category-bar {{
            margin-bottom: 20px;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        f"""
        <div style="
            font-size:24px;
            font-weight:700;
            margin-bottom:5px;
            color:{TEXT};
        ">
            ⚡ 24 Updates
        </div>

        <div style="
            color:{MUTED};
            font-size:13px;
            margin-bottom:30px;
        ">
            Your daily update assistant
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Filters")

    time_filter = st.radio(
        "Time range",
        ["24 Hours", "48 Hours"],
        index=0
    )

    st.markdown("### Categories")

    category = st.selectbox(
        "Choose category",
        [
            "All Updates",
            "🏏 Cricket",
            "🎬 Movies",
            "📰 News",
            "💼 Jobs"
        ]
    )

    st.divider()

    st.markdown(
        f"""
        <div style="
            color:{MUTED};
            font-size:12px;
            line-height:1.8;
        ">
            ⚡ Fresh updates<br>
            🔎 Smart search<br>
            🕒 24/48 hour filter<br>
            📱 Responsive design
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="app-title">24 Updates</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="app-subtitle">'
    'Fresh Cricket, Movies, News & Jobs — all in one place.'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# SEARCH
# =========================================================

search = st.text_input(
    "Search",
    placeholder="Search updates..."
)

# =========================================================
# CATEGORY BAR
# =========================================================

st.markdown(
    """
    <div class="category-bar">

        <div class="category-item active">
            ⚡ All
        </div>

        <div class="category-item">
            🏏 Cricket
        </div>

        <div class="category-item">
            🎬 Movies
        </div>

        <div class="category-item">
            📰 News
        </div>

        <div class="category-item">
            💼 Jobs
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SAMPLE DATA
# =========================================================

updates = [

    {
        "category": "🏏 Cricket",
        "title": "Latest Cricket Match Updates",
        "description": (
            "Today's match schedules, results, team news "
            "and important cricket developments."
        ),
        "hours": 2
    },

    {
        "category": "🏏 Cricket",
        "title": "Upcoming Cricket Matches",
        "description": (
            "Check upcoming matches, teams, timings "
            "and recent performances."
        ),
        "hours": 8
    },

    {
        "category": "🎬 Movies",
        "title": "Latest Movie Updates",
        "description": (
            "New movie announcements, trailers, releases "
            "and entertainment updates."
        ),
        "hours": 4
    },

    {
        "category": "🎬 Movies",
        "title": "OTT & Box Office Updates",
        "description": (
            "Latest OTT releases, streaming information "
            "and box-office developments."
        ),
        "hours": 18
    },

    {
        "category": "📰 News",
        "title": "Top Breaking News",
        "description": (
            "Important current events and major "
            "developments from reliable sources."
        ),
        "hours": 3
    },

    {
        "category": "📰 News",
        "title": "Trending News",
        "description": (
            "Popular stories and important updates "
            "from the latest news cycle."
        ),
        "hours": 20
    },

    {
        "category": "💼 Jobs",
        "title": "Latest Jobs & Internships",
        "description": (
            "Fresh opportunities for students, freshers "
            "and technology professionals."
        ),
        "hours": 5
    },

    {
        "category": "💼 Jobs",
        "title": "Developer Job Updates",
        "description": (
            "Recently posted developer jobs and "
            "internship opportunities."
        ),
        "hours": 22
    }

]

# =========================================================
# FILTER DATA
# =========================================================

max_hours = 24 if time_filter == "24 Hours" else 48

filtered = []

for item in updates:

    # Time filter
    if item["hours"] > max_hours:
        continue

    # Category filter
    if category != "All Updates":

        if item["category"] != category:
            continue

    # Search filter
    if search:

        searchable = (
            item["title"]
            + " "
            + item["description"]
            + " "
            + item["category"]
        ).lower()

        if search.lower() not in searchable:
            continue

    filtered.append(item)

# =========================================================
# RESULTS HEADER
# =========================================================

st.markdown(
    f'<div class="section-title">'
    f'Latest {time_filter} updates'
    f'</div>',
    unsafe_allow_html=True
)

# =========================================================
# UPDATE CARDS
# =========================================================

if not filtered:

    st.info(
        "No updates found. Try another search or filter."
    )

else:

    columns = st.columns(2)

    now = datetime.now()

    for index, item in enumerate(filtered):

        posted = now - timedelta(
            hours=item["hours"]
        )

        with columns[index % 2]:

            st.markdown(
                f"""
                <div class="update-card">

                    <div class="category-badge">
                        {item["category"]}
                    </div>

                    <div class="update-title">
                        {item["title"]}
                    </div>

                    <div class="update-description">
                        {item["description"]}
                    </div>

                    <div class="update-time">
                        🕒 Updated {item["hours"]} hours ago
                        &nbsp;•&nbsp;
                        {posted.strftime(
                            "%d %b %Y, %I:%M %p"
                        )}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# FOOTER
# =========================================================

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
        Live-data integration can be added next.
    </div>
    """,
    unsafe_allow_html=True
)
