import streamlit as st

from menu import menu


def config_page(route: dict[str, str]) -> None:
    page_title = route["label"]
    page_icon = route["icon"]

    st.set_page_config(page_title, page_icon)

    menu()
    st.title(page_title)
