import streamlit as st


class Routes:
    HOME = {
        "page": "pages/home.py",
        "label": "Trang chủ",
        "icon": ":material/home:",
    }

    COURSE = {
        "page": "pages/course.py",
        "label": "Học phát âm",
        "icon": ":material/school:",
    }


def menu():
    st.sidebar.page_link(**Routes.HOME)
    st.sidebar.page_link(**Routes.COURSE)
