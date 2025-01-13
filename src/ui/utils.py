from uuid import uuid4

import dropbox
import streamlit as st

from src.ui.menu import menu

dbx = dropbox.Dropbox(
    oauth2_refresh_token=st.secrets["dropbox_refresh_token"],
    app_key=st.secrets["dropbox_app_key"],
    app_secret=st.secrets["dropbox_app_secret"],
)


def config_page(route: dict[str, str]) -> None:
    page_title = route["label"]
    page_icon = route["icon"]

    st.set_page_config(page_title, page_icon, layout="wide")

    menu()
    st.title(page_title)


def add_vertical_space(num_lines: int = 1) -> None:
    for _ in range(num_lines):
        st.write("")


def upload_file(data, filename) -> None:
    dropbox_file_path = f"/{filename}"

    try:
        dbx.files_upload(data, dropbox_file_path)
    except dropbox.exceptions.ApiError as err:
        print("Dropbox API error", err)
        return None


def unique_audio_filename(lesson_id: str) -> str:
    id = uuid4().hex
    return f"{lesson_id}_{id}.mp3"
