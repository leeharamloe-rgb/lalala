import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 페이지 제목
st.set_page_config(page_title="🌍 국가별 MBTI 비율 시각화", layout="centered")
st.title("🌍 국가별 MBTI 비율 분석 대시보드")
st.markdown("### 나라를 선택하면 해당 국가의 MBTI 비율을 인터랙티브하게 볼 수 있어요!")

# 국가 선택
selected_country = st.selectbox("국가를 선택하세요 👇", df["Country"].sort_values())

# 선택된 국가 데이터 추출
country_data = df[df["Country"] == selected_country].iloc[0, 1:]
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
}).sort_values("비율", ascending=False)

# 색상 처리 (1등 빨간색, 나머지 점점 옅어지는 그라데이션)
colors = ["#ff4d4d"] + px.colors.sequential.Blues_r[2:17]  # 빨강 + 파란 계열 그라데이션

# 그래프 그리기
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text="비율",
    color="MBTI",
    color_discrete_sequence=colors,
)

fig.update_traces(texttemplate="%{text:.2%}", textposition="outside")
fig.update_layout(
    title=f"🇨🇳 {selected_country}의 MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    showlegend=False,
    plot_bgcolor="white",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# 추가 설명
st.markdown("""
📊 **해석 Tip**  
- 빨간색은 해당 국가에서 가장 높은 비율의 MBTI 유형이에요.  
- 파란색 계열은 그 외의 유형들을 비율에 따라 표현했어요.  
""")
