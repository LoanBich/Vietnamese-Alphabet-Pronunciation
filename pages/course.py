from pathlib import Path

import streamlit as st

from menu import Routes
from utils import config_page

config_page(Routes.COURSE)

LESSONS = [
    {"title": "Chữ cái E", "label": "E"},
    {"title": "Chữ cái H", "label": "H"},
    {"title": "Chữ cái I", "label": "I"},
    {"title": "Chữ cái L", "label": "L"},
    {"title": "Chữ cái N", "label": "N"},
    {"title": "Chữ cái Ơ", "label": "Ơ"},
    {"title": "Chữ cái U", "label": "U"},
    {"title": "Chữ cái V", "label": "V"},
]

st.sidebar.divider()
lesson = st.sidebar.radio(
    "Bài học",
    options=range(len(LESSONS)),
    index=None,
    format_func=lambda option: LESSONS[option]["title"],
    key="lessons",
)

if lesson is None:
    st.markdown("Chọn bài học ở bên trái.")
else:
    video_file = (
        Path(__file__).parents[1]
        / "assets"
        / "videos"
        / f"{LESSONS[lesson]['label']}.mov"
    )
    st.subheader(LESSONS[lesson]["title"])
    st.video(video_file)
