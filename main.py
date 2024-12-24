import streamlit as st
from streamlit_option_menu import option_menu
import home
import studying

st.set_page_config(page_title="Học phát âm", layout="wide")

selected = option_menu(
    menu_title=None,
    options=["Trang chủ", "Học phát âm", "Về chúng tôi"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    orientation="horizontal",
    styles={
        "container": {
            "padding": "5px",
            "background-color": "#F6F5F2",
        },  # Màu nền thanh menu
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "color": "#000000",  # Màu chữ mặc định
        },
        "nav-link-hover": {"color": "#F0EBE3"},  # Màu khi di chuột
        "nav-link-selected": {
            "background-color": "#F0EBE3",  # Màu nền khi được chọn
            "color": "#3B3030",  # Màu chữ khi được chọn
            "font-weight": "bold",  # Chữ đậm
        },
    },
)

if selected == "Trang chủ":
    home.show_home()
elif selected == "Học phát âm":
    studying.show_studying()
