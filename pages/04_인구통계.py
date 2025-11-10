import streamlit as st
import pandas as pd
import plotly.express as px

st.title("인구통계 시각화 앱")

# 데이터 불러오기
@st.cache_data
def load_data():
    try:
        # utf-8로 읽기, 실패하면 cp949 시도
        try:
            df = pd.read_csv("population.csv", encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv("population.csv", encoding="cp949", errors='replace')
        return df
    except FileNotFoundError:
        st.error("population.csv 파일이 없습니다. 파일 경로를 확인해주세요.")
        return pd.DataFrame()  # 빈 데이터프레임 반환

df = load_data()

# 컬럼명 확인
st.write("데이터 컬럼명:", df.columns.tolist())

# 필수 컬럼 체크
required_cols = ['지역', '나이', '인구수']
if all(col in df.columns for col in required_cols):
    # 지역 선택
    regions = df['지역'].unique()
    selected_region = st.selectbox("지역을 선택하세요", regions)

    # 선택한 지역 데이터 필터링
    region_data = df[df['지역'] == selected_region]

    # 나이별 인구 그래프
    fig = px.line(region_data, x='나이', y='인구수', title=f"{selected_region} 지역 나이별 인구")
    st.plotly_chart(fig)
else:
    st.error(f"CSV 파일에 필요한 컬럼이 없습니다. 최소한 {required_cols} 컬럼이 필요합니다.")
