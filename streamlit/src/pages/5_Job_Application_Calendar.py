import streamlit as st
import pandas as pd
from streamlit_calendar import calendar
import datetime

# 캐시된 데이터 로딩 함수
@st.cache_data
def load_job_application_data():
    # 실제로는 데이터베이스나 API에서 데이터를 가져올 것입니다.
    # 여기서는 예시 데이터를 생성합니다.
    data = [
        {"title": "A기업 서류 마감", "start": "2023-06-15", "end": "2023-06-15", "color": "#FF5733"},
        {"title": "B스타트업 면접", "start": "2023-06-20", "end": "2023-06-20", "color": "#33FF57"},
        {"title": "C기업 코딩테스트", "start": "2023-06-25", "end": "2023-06-25", "color": "#3357FF"},
        {"title": "D테크 최종면접", "start": "2023-07-01", "end": "2023-07-01", "color": "#FF33F1"}
    ]
    return pd.DataFrame(data)

st.title("취업 지원 일정")

# 데이터 로드
df = load_job_application_data()

# 새 일정 추가
st.subheader("새 일정 추가")
col1, col2, col3 = st.columns(3)
with col1:
    new_title = st.text_input("일정 제목")
with col2:
    new_date = st.date_input("날짜", min_value=datetime.date.today())
with col3:
    new_color = st.color_picker("색상", "#00f900")

if st.button("일정 추가"):
    new_event = {
        "title": new_title,
        "start": new_date.strftime("%Y-%m-%d"),
        "end": new_date.strftime("%Y-%m-%d"),
        "color": new_color
    }
    df = pd.concat([df, pd.DataFrame([new_event])], ignore_index=True)
    st.success("새 일정이 추가되었습니다!")

# 캘린더 표시
calendar_events = df.to_dict('records')
calendar(events=calendar_events, options={
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridMonth,timeGridWeek,timeGridDay,listWeek"
    },
    "initialView": "dayGridMonth"
})

# 일정 목록 표시
st.subheader("일정 목록")
st.dataframe(df[['title', 'start', 'end']])