import streamlit as st

from menu import Routes, menu

menu()
st.switch_page(Routes.HOME["page"])
