import streamlit as st
import requests

# API Gateway URL (환경 변수나 설정 파일에서 가져오는 것이 좋습니다)
API_GATEWAY_URL = "https://your-api-gateway-url.com"

def send_request_to_api_gateway(endpoint, method="GET", data=None):
    url = f"{API_GATEWAY_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        # 다른 HTTP 메서드도 필요에 따라 추가
        
        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        return response.json()
    except requests.RequestException as e:
        st.error(f"API 요청 중 오류 발생: {e}")
        return None

# Streamlit UI
if st.button("데이터 가져오기"):
    result = send_request_to_api_gateway("/some-endpoint")
    if result:
        st.write(result)

# 데이터 전송 예시
if st.button("데이터 전송"):
    data_to_send = {"key": "value"}
    result = send_request_to_api_gateway("/another-endpoint", method="POST", data=data_to_send)
    if result:
        st.success("데이터 전송 성공!")