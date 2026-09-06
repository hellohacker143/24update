import streamlit as st
import requests

API_KEY = "YOUR_NEWSAPI_KEY"

st.set_page_config(page_title="24 Updates", page_icon="⚡")

st.title("⚡ 24 Updates")

category = st.radio(
    "Select Category",
    ["Cricket", "Movies", "News", "Jobs"],
    horizontal=True
)

query_map = {
    "Cricket": "cricket",
    "Movies": "movies OR ott OR box office",
    "News": "india",
    "Jobs": "internship OR jobs"
}

query = query_map[category]

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={query}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
)

try:
    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])

    if not articles:
        st.warning("No updates found.")
    else:
        for article in articles[:20]:

            st.markdown("---")

            st.subheader(article["title"])

            if article.get("urlToImage"):
                st.image(article["urlToImage"])

            st.write(article.get("description", ""))

            st.caption(
                f"Source: {article['source']['name']} | "
                f"{article['publishedAt']}"
            )

            st.link_button(
                "Read More",
                article["url"]
            )

except Exception as e:
    st.error(str(e))
