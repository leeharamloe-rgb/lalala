import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="🌍 국가별 MBTI 비율 시각화", layout="centered")

# ---------------------------
# plotly import 시도 (안전하게 처리)
# ---------------------------
use_plotly_express = False
use_plotly_go = False
try:
    import plotly.express as px
    use_plotly_express = True
except Exception:
    try:
        import plotly.graph_objects as go  # fallback
        use_plotly_go = True
    except Exception:
        px = None
        go = None

# ---------------------------
# 색상 도우미 (hex <-> rgb 및 그라데이션 생성)
# ---------------------------
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*[int(max(0, min(255, v))) for v in rgb])

def interpolate_color(c1, c2, t):
    return tuple(c1[i] + (c2[i] - c1[i]) * t for i in range(3))

def gradient_colors(top_hex, start_hex, end_hex, n):
    """
    top_hex: 가장 큰 값(1등)에 사용할 색
    start_hex, end_hex: 나머지 n-1개를 위한 그라데이션(시작 색 -> 끝 색)
    n: 전체 막대 개수 (포함하여)
    """
    if n <= 1:
        return [top_hex]
    top_rgb = hex_to_rgb(top_hex)
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    # 나머지 수
    m = n - 1
    grads = []
    for i in range(m):
        t = i / max(1, m - 1)
        rgb = interpolate_color(start_rgb, end_rgb, t)
        grads.append(rgb_to_hex(rgb))
    return [top_hex] + grads

# ---------------------------
# 데이터 로드
# ---------------------------
@st.cache_data
def load_data(path="countriesMBTI_16types.csv"):
    p = Path(path)
    if not p.exists():
        st.error(f"데이터 파일이 존재하지 않습니다: {path}\n→ 앱 폴더에 `countriesMBTI_16types.csv` 를 업로드 해주세요.")
        return None
    df = pd.read_csv(p)
    return df

df = load_data()
if df is None:
    st.stop()

# 기본 체크
expected_cols = ["Country"]
mbti_cols = [c for c in df.columns if c != "Country"]
if len(mbti_cols) != 16:
    st.warning("경고: MBTI 유형 열이 16개가 아닙니다. 현재 발견된 MBTI 열:")
    st.write(df.columns.tolist())

# ---------------------------
# UI
# ---------------------------
st.title("🌍 국가별 MBTI 비율 분석 대시보드")
st.markdown("나라를 선택하면 그 나라의 MBTI 16유형 비율을 인터랙티브한 막대그래프로 보여줍니다.")

selected_country = st.selectbox("국가를 선택하세요 👇", df["Country"].sort_values())

# 선택 국가 데이터 준비
row = df[df["Country"] == selected_country]
if row.empty:
    st.error("선택한 국가의 데이터가 없습니다.")
    st.stop()

country_series = row.iloc[0].drop(labels=["Country"])  # MBTI 값들
country_df = pd.DataFrame({
    "MBTI": country_series.index,
    "비율": country_series.values.astype(float)
}).sort_values("비율", ascending=False).reset_index(drop=True)

# 색상 생성: 1등 빨강, 나머지는 블루 그라데이션 (원하면 변경 가능)
top_color = "#ff4d4d"   # 1등 빨강
grad_start = "#d0e7ff"  # 연한 파랑
grad_end = "#2b6cb0"    # 진한 파랑
colors = gradient_colors(top_color, grad_start, grad_end, len(country_df))

# 만약 plotly가 아예 없으면 안내와 표 출력
if not (use_plotly_express or use_plotly_go):
    st.error("plotly가 설치되어 있지 않아 그래프를 표시할 수 없습니다.\n\n`requirements.txt`에 `plotly`를 추가한 뒤 다시 배포해주세요.")
    st.markdown("대신 표로 데이터를 보여드립니다.")
    st.dataframe(country_df.style.format({"비율": "{:.4f}"}))
    st.stop()

# ---------------------------
# 그래프 생성 (plotly.express 우선, 없으면 graph_objects 사용)
# ---------------------------
title_text = f"{selected_country}의 MBTI 비율 (Top: {country_df.loc[0,'MBTI']})"

if use_plotly_express:
    fig = px.bar(
        country_df,
        x="MBTI",
        y="비율",
        text="비율",
        color="MBTI",
        color_discrete_sequence=colors,
        labels={"비율": "비율 (비율값)", "MBTI": "MBTI 유형"},
    )
    fig.update_traces(texttemplate="%{text:.2%}", textposition="outside", marker_line_width=0.2)
    fig.update_layout(
        title=title_text,
        xaxis_title="MBTI 유형",
        yaxis_title="비율",
        showlegend=False,
        plot_bgcolor="white",
        title_x=0.5,
        margin=dict(t=70, b=40, l=40, r=20),
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    # graph_objects로 그리기
    import plotly.graph_objects as go
    fig = go.Figure(data=[
        go.Bar(
            x=country_df["MBTI"],
            y=country_df["비율"],
            marker=dict(color=colors, line=dict(width=0.2, color="#333333")),
            text=[f"{v:.2%}" for v in country_df["비율"]],
            textposition="outside",
        )
    ])
    fig.update_layout(
        title=title_text,
        xaxis_title="MBTI 유형",
        yaxis_title="비율",
        showlegend=False,
        plot_bgcolor="white",
        title_x=0.5,
        margin=dict(t=70, b=40, l=40, r=20),
    )
    st.plotly_chart(fig, use_container_width=True)

# 추가 정보
st.markdown("""
📌 **설명**
- 막대의 높이는 해당 국가에서 관측된 각 MBTI 유형의 비율을 의미합니다.
- 가장 높은 유형(1등)은 빨간색으로 강조되어 있고, 나머지는 파랑 계열의 그라데이션으로 표현됩니다.
""")
