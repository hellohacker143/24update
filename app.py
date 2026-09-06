
import streamlit as st
from datetime import datetime, timedelta

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="24 Updates",
    page_icon="⚡",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
    }

    .subtitle {
        color: #888;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        margin-bottom: 15px;
        background: #11151c;
    }

    .category {
        font-size: 25px;
        font-weight: 700;
        margin-top: 20px;
    }

    .time {
        color: #888;
        font-size: 13px;
    }

    .badge {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 20px;
        background: #222;
        font-size: 12px;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="title">⚡ 24 Updates</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Fresh updates in Cricket, Movies, News & Jobs</div>',
    unsafe_allow_html=True
)

# -----------------------------
# TOP FILTERS
# -----------------------------
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    time_filter = st.selectbox(
        "Time",
        ["24 Hours", "48 Hours"]
    )

with col2:
    category = st.selectbox(
        "Category",
        [
            "All",
            "🏏 Cricket",
            "🎬 Movies",
            "📰 News",
            "💼 Jobs"
        ]
    )

with col3:
    search = st.text_input(
        "🔎 Search updates",
        placeholder="Search Cricket, Movies, News or Jobs..."
    )

st.divider()

# -----------------------------
# SAMPLE DATA
# -----------------------------
updates = [
    {
        "category": "🏏 Cricket",
        "title": "Latest Cricket Match Updates",
        "description": "Check today's matches, team updates, results and important cricket news.",
        "hours": 2
    },
    {
        "category": "🏏 Cricket",
        "title": "Upcoming Cricket Matches",
        "description": "View upcoming matches and important match information.",
        "hours": 10
    },
    {
        "category": "🎬 Movies",
        "title": "Latest Movie Updates",
        "description": "New movie announcements, trailers, releases and entertainment updates.",
        "hours": 4
    },
    {
        "category": "🎬 Movies",
        "title": "OTT & Box Office Updates",
        "description": "Latest OTT releases and box-office developments.",
        "hours": 18
    },
    {
        "category": "📰 News",
        "title": "Top Breaking News",
        "description": "Important current news and major developments.",
        "hours": 3
    },
    {
        "category": "📰 News",
        "title": "Trending News",
        "description": "Popular stories and important updates from the last 24 hours.",
        "hours": 20
    },
    {
        "category": "💼 Jobs",
        "title": "Latest Jobs & Internships",
        "description": "Fresh job and internship opportunities for students and freshers.",
        "hours": 5
    },
    {
        "category": "💼 Jobs",
        "title": "Developer Job Updates",
        "description": "Recently posted opportunities for developers and technology professionals.",
        "hours": 22
    }
]

# -----------------------------
# FILTER
# -----------------------------
max_hours = 24 if time_filter == "24 Hours" else 48

filtered_updates = []

for item in updates:

    # Time filter
    if item["hours"] > max_hours:
        continue

    # Category filter
    if category != "All" and item["category"] != category:
        continue

    # Search filter
    if search:
        text = (
            item["title"] + " " +
            item["description"] + " " +
            item["category"]
        ).lower()

        if search.lower() not in text:
            continue

    filtered_updates.append(item)

# -----------------------------
# RESULTS
# -----------------------------
st.markdown(
    f"### Latest {time_filter} Updates"
)

if not filtered_updates:

    st.info("No updates found.")

else:

    columns = st.columns(2)

    now = datetime.now()

    for index, item in enumerate(filtered_updates):

        posted_time = now - timedelta(hours=item["hours"])

        with columns[index % 2]:

            st.markdown(
                f"""
                <div class="card">

                    <div class="badge">
                        {item["category"]}
                    </div>

                    <h3>{item["title"]}</h3>

                    <p>
                        {item["description"]}
                    </p>

                    <div class="time">
                        🕒 Updated {item["hours"]} hours ago
                        <br>
                        {posted_time.strftime("%d %b %Y • %I:%M %p")}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.caption(
    "⚡ 24 Updates • Cricket • Movies • News • Jobs"
)

st.caption(
    "Demo version — connect live APIs/feeds to display real-time updates."
)
