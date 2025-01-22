import io
from pathlib import Path

import numpy as np
import streamlit as st
from audiorecorder import audiorecorder

from src.models import load_model, predict_score
from src.ui.menu import Routes
from src.ui.utils import (
    add_vertical_space,
    config_page,
    unique_audio_filename,
    unique_session_id,
    upload_file,
)

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


@st.fragment
def show_lesson(lesson):
    lesson_title = lesson["title"]
    lesson_id = lesson["id"]
    lesson_video_file = (
        Path(__file__).parents[1] / "assets" / "videos" / f"{lesson_id}.mov"
    )

    st.subheader(lesson_title)
    st.video(lesson_video_file)

    add_vertical_space(1)

    st.subheader("Chấm điểm")
    st.markdown("Sau khi học xong bài học, hãy đọc lại chữ cái đó để hệ thống chấm điểm")
    audio = audiorecorder(
        "",  # "Ấn để bắt đầu ghi âm",
        "",  # "Ấn để dừng lại",
        key=lesson_id,
    )

    if len(audio) > 0:
        st.info(
            "Hãy giúp tớ check lại phát âm xem đã đúng và rõ ràng chưa nhé ạ! Nếu chưa được thì hãy ghi âm lại giúp tớ nha ạ!!",
            icon="ℹ️",
        )
        st.audio(audio.export().read())

    if st.button(label="Chấm điểm", type="primary"):
        if len(audio) > 0:
            with st.spinner("Evaluating..."):
                score = None
                waveform = np.asarray(
                    audio.set_frame_rate(16000).get_array_of_samples()
                ).T.astype(np.float32)

                try:
                    score = predict_score(model, waveform, actual_label=lesson_id)
                    if score > 3.8:
                        st.info("Bạn phát âm rất tốt!")
                    else:
                        st.warning(
                            "Bạn cần cải thiện thêm. Xem lại video và phát âm lại nhé!"
                        )
                except:
                    st.error(
                        "Giúp tớ thu âm lại nha, bạn nhớ phát âm to rõ nhé", icon="🚨"
                    )

                # upload to Dropbox
                audio_buffer = io.BytesIO()
                audio.export(audio_buffer, format="wav", parameters=["-ar", str(16000)])
                upload_file(
                    audio_buffer.getvalue(),
                    unique_audio_filename(
                        st.session_state["session_id"],
                        lesson_id,
                        score,
                    ),
                )
        else:
            st.error("Chưa được rồi, giúp tớ thu âm lại nha", icon="🚨")


if "session_id" not in st.session_state:
    st.session_state["session_id"] = unique_session_id()

model = load_model()

st.sidebar.divider()
lesson = st.sidebar.radio(
    "Bài học",
    options=range(len(LESSONS)),
    index=None,
    format_func=lambda option: LESSONS[option]["title"],
    key="lessons",
)

add_vertical_space(1)

if lesson is None:
    st.info(
        "Chọn bài học ở bên trái.",
        icon="ℹ️",
    )
else:
    show_lesson(LESSONS[lesson])
