import streamlit as st
import pandas as pd

st.title("문제 관리 시스템")

# 탭 생성
tab1, tab2 = st.tabs(["📝 문제 제출", "📊 로그 확인"])

# 문제 제출 탭
with tab1:
    st.header("문제 제출")

    # 문제명 입력
    problem_name = st.text_input("문제명", value="버섯 농장")

    # 분류와 난이도를 나란히 배치
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("분류", options=["BFS/DFS", "DP", "그리디", "구현"])
    with col2:
        difficulty = st.selectbox("난이도", options=["S1", "S2", "S3", "G1", "G2"])

    # 문제 보기 버튼
    st.button("문제 보기")

    # 제출할 링크 입력
    solution_link = st.text_input("제출할 링크", placeholder="e.g.) www.my-blog-solution-page.com")

    # 추가 정보
    st.markdown("• velog, github, tistory 등 멘토가 볼 수 있는 링크를 제출해주세요!")
    st.markdown("• notion 링크는 view 권한이 제대로 부여되었는지 꼭 확인 부탁드려요!")

    # 제출하기 버튼
    if st.button("제출하기", type="primary"):
        st.success("제출되었습니다!")

# 로그 확인 탭
with tab2:
    st.header("로그 확인")

    # 예시 로그 데이터
    log_data = [
        {"날짜": "2024-03-01", "문제명": "버섯 농장", "분류": "BFS/DFS", "난이도": "S1", "풀이 링크": "https://github.com/user/mushroom-farm-solution"},
        {"날짜": "2024-03-02", "문제명": "숫자 퍼즐", "분류": "DP", "난이도": "G2", "풀이 링크": "https://velog.io/@user/number-puzzle-solution"},
    ]
    
    # DataFrame으로 변환
    df = pd.DataFrame(log_data)
    
    # 풀이 링크를 클릭 가능한 형태로 변환
    df['풀이 링크'] = df['풀이 링크'].apply(lambda x: f'<a href="{x}" target="_blank">링크</a>')
    
    # HTML로 표시 (클릭 가능한 링크를 위해)
    st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)

    st.info("최근 제출한 문제들의 로그입니다. '풀이 링크'를 클릭하여 제출한 풀이를 확인할 수 있습니다.")