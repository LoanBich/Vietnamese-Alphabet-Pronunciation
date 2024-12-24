import base64
import streamlit as st
import studying


def get_base64_from_file(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


def show_home():
    # Đường dẫn đến hình ảnh
    img_path = "./images/home.jpg"  # Đảm bảo đường dẫn chính xác

    # Chuyển đổi hình ảnh sang base64
    base64_image = get_base64_from_file(img_path)

    # CSS để hiển thị hình nền với kích thước phù hợp
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_image}");
            background-size: cover; /* Bao phủ toàn bộ trang */
            background-position: center; /* Canh giữa hình nền */
            background-repeat: no-repeat; /* Không lặp hình ảnh */
            height: 100vh; /* Chiều cao bằng toàn bộ cửa sổ */
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Nội dung của trang
    st.markdown(
        """
        <div style="
            text-align: center; 
            padding-top: 20vh; 
            color: #000; 
            background: rgba(255, 255, 255, 0.7); 
            border-radius: 10px; 
            padding: 100px; 
            max-width: 1200px; 
            margin: 0 auto;">
            <h1 style="font-size: 2.5rem; margin-bottom: 20px;">Chào mừng đến với trang web học phát âm bảng chữ cái tiếng Việt!</h1>
            <p style="font-size: 1.2rem; margin-bottom: 30px;">Trang web giúp bạn học phát âm một cách dễ dàng và hiệu quả.</p>
            <a href="./studying.py" style="
                text-decoration: none; 
                color: white; 
                background-color: #FF7F7F; 
                padding: 10px 20px; 
                border-radius: 5px; 
                font-size: 1.2rem;">Bắt đầu học phát âm</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
