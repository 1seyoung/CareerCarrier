import streamlit as st

st.set_page_config(page_title="개발자 취업 플래너", layout="wide")

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# 캐릭터 정보 초기화
if 'character' not in st.session_state:
    st.session_state.character = {
        'name': '코딩 마스터',
        'level': 1,
        'exp': 20,
        'mood': 70,
        'image': 'https://place-hold.it/300x300.png&text=Coding%20Master&fontsize=23'  # 실제 캐릭터 이미지 URL로 교체 필요
    }

# 레벨별 필요 경험치 계산 함수
def exp_to_next_level(level):
    return level * 100

st.title("개발자 성장 시뮬레이터")

# 캐릭터 정보 표시
col1, col2 = st.columns([1, 2])
with col1:
    st.image(st.session_state.character['image'], caption=st.session_state.character['name'])
with col2:
    st.subheader("캐릭터 상태")
    
    # 경험치 표시
    current_exp = st.session_state.character['exp']
    max_exp = exp_to_next_level(st.session_state.character['level'])
    exp_percentage = (current_exp / max_exp) * 100
    st.metric("경험치", f"{current_exp}/{max_exp} ({exp_percentage:.1f}%)")
    
    # 기분 표시
    mood_percentage = st.session_state.character['mood']
    st.metric("기분", f"{mood_percentage}%")
    
    # 레벨 표시
    st.metric("레벨", st.session_state.character['level'])

# 캐릭터 돌보기
st.header("캐릭터 돌보기")
col_action1, col_action2 = st.columns(2)
if col_action1.button("간식 주기 🍪"):
    st.session_state.character['mood'] = min(100, st.session_state.character['mood'] + 10)
    st.success(f"맛있는 간식을 주었습니다! 기분이 {st.session_state.character['mood']}%가 되었어요.")

if col_action2.button("응원하기 👏"):
    st.session_state.character['mood'] = min(100, st.session_state.character['mood'] + 5)
    st.session_state.character['exp'] += 10
    st.success(f"열렬히 응원했습니다! 기분이 {st.session_state.character['mood']}%가 되었어요. 경험치도 10 올랐습니다!")

# 오늘의 개발 활동
st.header("오늘의 개발 활동")
today = datetime.now()
col_dev1, col_dev2, col_dev3 = st.columns(3)
col_dev1.metric("코딩 시간", f"{random.randint(1, 8)}시간")
col_dev2.metric("커밋 수", random.randint(1, 10))
col_dev3.metric("완료한 작업", random.randint(1, 5))

# 주간 개발 활동 그래프
st.header("주간 개발 활동")
dates = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
coding_hours = [random.randint(1, 8) for _ in range(7)]
commits = [random.randint(1, 10) for _ in range(7)]
tasks = [random.randint(1, 5) for _ in range(7)]

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=coding_hours, mode='lines+markers', name='코딩 시간'))
fig.add_trace(go.Scatter(x=dates, y=commits, mode='lines+markers', name='커밋 수'))
fig.add_trace(go.Scatter(x=dates, y=tasks, mode='lines+markers', name='완료한 작업'))
fig.update_layout(title='주간 개발 활동', xaxis_title='날짜', yaxis_title='수치')
st.plotly_chart(fig)

# 랜덤 이벤트
if random.random() < 0.1:  # 10% 확률로 이벤트 발생
    events = [
        "갑자기 영감이 떠올랐다! 코딩 속도 2배 증가!",
        "선배 개발자의 조언을 들었다. 문제 해결 능력이 상승!",
        "오픈 소스 프로젝트에 기여했다. 명성이 올랐다!"
    ]
    st.success(random.choice(events))

# 레벨업 체크
if st.session_state.character['exp'] >= exp_to_next_level(st.session_state.character['level']):
    st.session_state.character['level'] += 1
    st.session_state.character['exp'] = 0  # 경험치 초기화
    st.balloons()
    st.success(f"축하합니다! 레벨 {st.session_state.character['level']}로 올랐습니다!")

# 개발 팁
tips = [
    "규칙적인 휴식은 생산성을 높입니다.",
    "새로운 기술을 꾸준히 학습하세요.",
    "코드 리뷰는 실력 향상의 지름길입니다.",
    "문서화는 미래의 자신을 위한 선물입니다.",
    "버전 관리 시스템을 적극 활용하세요."
]
st.sidebar.title("오늘의 개발 팁")
st.sidebar.info(random.choice(tips))
st.sidebar.markdown("---")