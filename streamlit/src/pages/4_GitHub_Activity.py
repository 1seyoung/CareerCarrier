import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd

def get_github_activity(username, token, days=7):
    # 현재 날짜에서 7일 전 날짜 계산
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    # GitHub API 엔드포인트
    url = f"https://api.github.com/users/{username}/events"
    
    # API 요청 헤더
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # API 요청
    response = requests.get(url, headers=headers)
    events = response.json()

    # 활동 요약
    activity_summary = {
        "PushEvent": 0,
        "PullRequestEvent": 0,
        "IssuesEvent": 0,
        "CreateEvent": 0
    }

    for event in events:
        event_date = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        if start_date <= event_date <= end_date:
            if event['type'] in activity_summary:
                activity_summary[event['type']] += 1

    return activity_summary

# Streamlit 앱
st.title("GitHub 활동 요약")

# GitHub 사용자명과 토큰 입력
github_username = st.text_input("GitHub 사용자명")
github_token = st.text_input("GitHub 개인 액세스 토큰", type="password")

if st.button("활동 요약 보기"):
    if github_username and github_token:
        activity = get_github_activity(github_username, github_token)
        
        st.subheader(f"{github_username}의 최근 7일 GitHub 활동")
        
        # 데이터프레임으로 변환하여 표시
        df = pd.DataFrame.from_dict(activity, orient='index', columns=['횟수'])
        df.index.name = '활동 유형'
        st.table(df)

        # 간단한 해석 추가
        total_activities = sum(activity.values())
        st.write(f"총 활동 횟수: {total_activities}")
        if total_activities > 0:
            most_frequent = max(activity, key=activity.get)
            st.write(f"가장 많이 한 활동: {most_frequent} ({activity[most_frequent]}회)")
        else:
            st.write("최근 7일간 GitHub 활동이 없습니다.")
    else:
        st.error("GitHub 사용자명과 개인 액세스 토큰을 입력해주세요.")