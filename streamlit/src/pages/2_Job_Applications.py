import streamlit as st
import pandas as pd
import plotly.express as px

st.title("취업 지원 현황")

col1, col2 = st.columns(2)
with col1:
    company = st.text_input("회사명")
    position = st.text_input("지원 포지션")
    status = st.selectbox("상태", ["지원 예정", "지원 완료", "서류 통과", "면접 예정", "최종 합격", "불합격"])
    if st.button("추가"):
        st.success("지원 정보가 추가되었습니다!")

with col2:
    # 샘플 데이터로 차트 표시
    data = pd.DataFrame({
        "회사": ["A기업", "B스타트업", "C기업", "D테크"],
        "상태": ["서류 통과", "면접 예정", "지원 완료", "최종 합격"]
    })
    fig = px.bar(data, x="회사", y="상태", title="지원 현황")
    st.plotly_chart(fig)