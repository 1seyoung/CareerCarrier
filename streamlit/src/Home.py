import streamlit as st

st.set_page_config(page_title="개발자 취업 플래너", layout="wide")

st.title("개발자 취업 플래너에 오신 것을 환영합니다!")
st.write("이 애플리케이션은 당신의 개발자 취업 준비를 도와줍니다.")
st.write("왼쪽 사이드바에서 원하는 메뉴를 선택하세요.")

st.sidebar.markdown("---")
st.sidebar.info("© 2023 개발자 취업 플래너")