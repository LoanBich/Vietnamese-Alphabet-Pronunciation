import streamlit as st

from menu import Routes
from utils import config_page

config_page(Routes.HOME)

# Đường dẫn đến hình ảnh
img_path = "app/static/home.jpg"  # Đảm bảo đường dẫn chính xác

# CSS để hiển thị hình nền với kích thước phù hợp
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{img_path}");
        background-size: cover; /* Bao phủ toàn bộ trang */
        background-position: center; /* Canh giữa hình nền */
        background-repeat: no-repeat; /* Không lặp hình ảnh */
        height: 100vh; /* Chiều cao bằng toàn bộ cửa sổ */
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("Chào mừng đến với trang web học phát âm bảng chữ cái tiếng Việt!")
st.markdown("Trang web giúp bạn học phát âm một cách dễ dàng và hiệu quả.")
