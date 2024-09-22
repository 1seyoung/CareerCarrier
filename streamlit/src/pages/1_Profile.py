import streamlit as st

st.title("프로필")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("이름")
    email = st.text_input("이메일")
    github = st.text_input("GitHub 사용자명")
with col2:
    skills = st.multiselect("기술 스택", ["Python", "Java", "JavaScript", "React", "Node.js", "SQL"])
    experience = st.slider("경력 (년)", 0, 10, 0)

if st.button("저장"):
    st.success("프로필이 저장되었습니다!")