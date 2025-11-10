import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("📊 지역별 나이대 인구분포 시각화")
st.markdown("Plotly로 인터랙티브하게 지역별 인구를 비교해보세요!")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("population.csv", encoding="cp949")
    return df

df = load_data()

# 데이터 확인
if df is not None:
    st.success("데이터 불러오기 성공 ✅")
    st.write("데이터 미리보기 👇")
    st.dataframe(df.head())
else:
    st.error("데이터를 불러올 수 없습니다 😢")
    st.stop()

# 사용자 입력: 지역 선택
regions = df["지역"].unique()
selected_region = st.selectbox("📍 지역을 선택하세요:", regions)

# 선택한 지역의 데이터 필터링
filtered_df = df[df["지역"] == selected_region]

# Plotly 그래프 그리기
fig = px.line(
    filtered_df,
    x="나이",
    y="인구수",
    title=f"📈 {selected_region} 지역의 나이별 인구분포",
    markers=True,
    template="plotly_white",
    line_shape="spline"
)

fig.update_layout(
    xaxis_title="나이",
    yaxis_title="인구수",
    title_x=0.3,
    font=dict(size=14)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("💡 파일: population.csv | 시각화 라이브러리: Plotly | 만든이: 이하람")
