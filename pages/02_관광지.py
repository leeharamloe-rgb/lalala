# Streamlit 앱: 서울 외국인 인기 관광지 TOP10 (Folium 지도)
# 파일명: streamlit_seoul_top10_app.py
# Streamlit Cloud에서 실행 가능

import streamlit as st
import folium
from streamlit_folium import st_folium

def main():
    # 페이지 기본 설정
    st.set_page_config(page_title="서울 인기 관광지 TOP10", layout="wide")

    # 제목
    st.title("🗺️ 서울 외국인 인기 관광지 TOP 10")
    st.markdown("서울을 처음 방문하는 외국인들이 가장 좋아하는 명소 10곳을 한눈에 볼 수 있어요!")

    # 관광지 데이터
    PLACES = [
        { "name": "경복궁", "lat": 37.579617, "lon": 126.977041,
          "desc": "조선 왕조의 대표 궁궐로, 수문장 교대식이 유명합니다." },
        { "name": "창덕궁과 후원", "lat": 37.5794, "lon": 126.9910,
          "desc": "유네스코 세계문화유산. 후원(비밀의 정원)이 특히 아름답습니다." },
        { "name": "북촌 한옥마을", "lat": 37.5826, "lon": 126.9830,
          "desc": "전통 한옥들이 모여 있어 사진 찍기 좋은 곳입니다." },
        { "name": "남산 서울타워", "lat": 37.5512, "lon": 126.9882,
          "desc": "서울 전망 명소. 특히 일몰과 야경이 멋집니다." },
        { "name": "명동 쇼핑거리", "lat": 37.5609, "lon": 126.9860,
          "desc": "화장품과 패션, 길거리 음식이 유명한 쇼핑 거리입니다." },
        { "name": "인사동", "lat": 37.5740, "lon": 126.9849,
          "desc": "전통 공예품과 찻집이 많은 문화 거리로 기념품 사기 좋습니다." },
        { "name": "동대문디자인플라자(DDP)", "lat": 37.5663, "lon": 127.0090,
          "desc": "미래적인 건축물이 인상적인 복합문화공간입니다." },
        { "name": "홍대 거리", "lat": 37.5563, "lon": 126.9230,
          "desc": "젊음의 거리로 버스킹과 카페, 스트리트 문화가 활발합니다." },
        { "name": "광장시장", "lat": 37.5704, "lon": 126.9998,
          "desc": "한국 전통 길거리 음식을 다양하게 맛볼 수 있습니다." },
        { "name": "롯데월드타워 & 몰", "lat": 37.5131, "lon": 127.1025,
          "desc": "한국에서 가장 높은 타워와 대형 쇼핑 몰, 전망대가 있습니다." },
    ]

    # 사이드바
    st.sidebar.header("🧭 지도 설정")
    show_all = st.sidebar.checkbox("모두 표시", value=True)

    if show_all:
        selected_names = [p["name"] for p in PLACES]
    else:
        choices = [p["name"] for p in PLACES]
        selected_names = st.sidebar.multiselect("표시할 장소 선택", choices, default=choices[:5])

    zoom_choice = st.sidebar.selectbox("지도 중심 위치", ["서울 전체 보기"] + [p["name"] for p in PLACES])

    # Folium 지도 생성 (서울 중심)
    seoul_center = (37.5665, 126.9780)
    folium_map = folium.Map(location=seoul_center, zoom_start=12, control_scale=True)

    # 마커 추가 (선택된 장소만)
    for place in PLACES:
        if place["name"] in selected_names:
            popup_html = "<b>{}</b><br>{}".format(place["name"], place["desc"])
            popup = folium.Popup(popup_html, max_width=300)
            folium.Marker(
                location=(place["lat"], place["lon"]),
                popup=popup,
                tooltip=place["name"],
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(folium_map)

    # 특정 장소로 확대
    if zoom_choice != "서울 전체 보기":
        target = next((p for p in PLACES if p["name"] == zoom_choice), None)
        if target:
            folium_map.location = (target["lat"], target["lon"])
            folium_map.zoom_start = 15

    # 지도 표시
    st.subheader("🗺️ 지도")
    st_folium(folium_map, width=1000, height=600)

    # 간단한 리스트 표시
    st.subheader("📍 관광지 간단 정보")
    cols = st.columns(2)
    for i, place in enumerate(PLACES):
        with cols[i % 2]:
            st.markdown("**{}. {}**".format(i+1, place["name"]))
            st.write(place["desc"])

    st.markdown("---")
    st.caption("출처: 한국관광공사 및 여행 가이드들(좌표는 참고용입니다).")
    st.info("팁: 지도에서 마커를 클릭하면 설명이 나옵니다. 사이드바로 표시할 장소를 선택해보세요!")

if __name__ == "__main__":
    main()
