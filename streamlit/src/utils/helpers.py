import pandas as pd

def load_sample_data():
    # 샘플 데이터를 로드하는 함수
    # 실제 구현에서는 데이터베이스나 API에서 데이터를 가져올 수 있습니다
    return pd.DataFrame({
        "날짜": pd.date_range(start="2023-01-01", end="2023-12-31", freq="D"),
        "커밋 수": [i % 15 for i in range(365)]
    })