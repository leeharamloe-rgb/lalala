import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
@st.cache_data
def load_data():
    # encoding을 utf-8로 변경, 문제 발생 시 errors='replace' 옵션 추가
    try:
        df = pd.read_csv("population.csv", encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv("population.csv", encoding="utf-8", errors='replace')
    return df

df = load_data()

st.title("인구통계 시각화 앱")

# 지역 선택
regions = df['지역'].unique()
selected_region = st.selectbox("지역을 선택하세요", regions)

# 선택한 지역 데이터 필터링
region_data = df[df['지역'] == selected_region]

# 나이별 인구 그래프
fig = px.line(region_data, x='나이', y='인구수', title=f"{selected_region} 지역 나이별 인구")
st.plotly_chart(fig)
