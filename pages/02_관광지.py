# Streamlit 앱: 서울 외국인 인기 관광지 Top10 (Folium 지도)
# 파일명: streamlit_seoul_top10_app.py
# Streamlit Cloud에서 바로 실행 가능

import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="서울 인기 관광지 TOP10", layout="wide")

# 제목
st.title("🗺️ 서울 외국인 인기 관광지 TOP 10")
st.markdown("서울을 처음 방문하는 외국인들이 가장 좋아하는 명소 10곳을 한눈에 볼 수 있어요! 😊")

# 관광지 정보
PLACES = [
    {"name": "경복궁", "lat": 37.579617, "lon": 126.977041, "desc": "조선 왕조의 대표 궁궐로, 근정전과 교태전이 유명해요. 수문장 교대식도 꼭 보세요!"},
    {"name": "창덕궁과 후원", "lat": 37.5794, "lon": 126.9910, "desc": "유네스코 세계문화유산으로 지정된 아름다운 궁궐이에요. 비밀의 정원(후원)이 특히 유명하답니다."},
    {"name": "북촌 한옥마을", "lat": 37.5826, "lon": 126.9830, "desc": "전통 한옥이 모여 있는 마을로, 사진 찍기 좋은 명소예요."},
    {"name": "남산 서울타워", "lat": 37.5512, "lon": 126.9882, "desc": "서울을 한눈에 볼 수 있는 전망 명소! 야경이 특히 아름다워요."},
    {"name": "명동 쇼핑거리", "lat": 37.5
