import streamlit as st

from src.ui.menu import Routes, menu

menu()
st.switch_page(Routes.HOME["page"])
