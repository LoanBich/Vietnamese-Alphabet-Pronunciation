from uuid import uuid4

import dropbox
import streamlit as st

from menu import menu

access_token = st.secrets["access_token"]
dbx = dropbox.Dropbox(access_token)


def config_page(route: dict[str, str]) -> None:
    page_title = route["label"]
    page_icon = route["icon"]

    st.set_page_config(page_title, page_icon)

    menu()
    st.title(page_title)


def upload_file(data, filename) -> None:
    """Upload a file.

    Return the request response, or None in case of error.
    """
    dropbox_file_path = f"/{filename}"
    try:
        dbx.files_upload(data, dropbox_file_path)
    except dropbox.exceptions.ApiError as err:
        print("*** API error", err)
        return None


def unique_audio_filename(lesson_id: str) -> str:
    id = uuid4().hex
    return f"{lesson_id}_{id}.mp3"
