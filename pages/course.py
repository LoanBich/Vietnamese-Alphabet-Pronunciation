from pathlib import Path

import streamlit as st
from audiorecorder import audiorecorder

from menu import Routes
from utils import config_page, unique_audio_filename, upload_file

config_page(Routes.COURSE)

LESSONS = [
    {"title": "Chữ cái E", "id": "E"},
    {"title": "Chữ cái H", "id": "H"},
    {"title": "Chữ cái I", "id": "I"},
    {"title": "Chữ cái L", "id": "L"},
    {"title": "Chữ cái N", "id": "N"},
    {"title": "Chữ cái Ơ", "id": "Ơ"},
    {"title": "Chữ cái U", "id": "U"},
    {"title": "Chữ cái V", "id": "V"},
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
    lesson_title = LESSONS[lesson]["title"]
    lesson_id = LESSONS[lesson]["id"]
    lesson_video_file = (
        Path(__file__).parents[1] / "assets" / "videos" / f"{lesson_id}.mov"
    )

    st.subheader(lesson_title)
    st.video(lesson_video_file)

    audio = audiorecorder("", "")

    if len(audio) > 0:
        st.audio(audio.export().read())
        upload_file(audio.export().read(), unique_audio_filename(lesson_id))
