import streamlit as st

import streamlit as st
import time
import random

st.title("간단한 시뮬레이션")

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(100):
    # 시뮬레이션 진행
    progress_bar.progress(i + 1)
    status_text.text(f"시뮬레이션 진행 중... {i+1}%")
    time.sleep(0.1)  # 0.1초 대기

status_text.text("시뮬레이션 완료!")
st.balloons()

# 결과 표시
result = random.randint(1, 100)
st.write(f"시뮬레이션 결과: {result}")