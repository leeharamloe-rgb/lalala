# Streamlit app: Seoul Top10 tourist spots (Folium map)
# File: streamlit_seoul_top10_app.py
# Run on Streamlit Cloud as a single-file app.

import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Seoul Top10 — Folium Map", layout="wide")

st.title("🇰🇷 Seoul Top 10 Tourist Spots (외국인 인기) — Interactive Map")
st.markdown("Choose places on the left to show them on the map. Click markers for quick info!")

# Top 10 tourist spots (popular with foreign visitors)
PLACES = [
    {"name":"Gyeongbokgung Palace", "lat":37.579617, "lon":126.977041, "desc":"The main royal palace of the Joseon dynasty. Don't miss the changing of the guard."},
    {"name":"Changdeokgung Palace & Secret Garden", "lat":37.5794, "lon":126.9910, "desc":"A UNESCO World Heritage palace with the famous Secret Garden (Huwon)."},
    {"name":"Bukchon Hanok Village", "lat":37.5826, "lon":126.9830, "desc":"Traditional Korean hanok houses in a neighborhood setting — very photogenic."},
    {"name":"N Seoul Tower (Namsan)", "lat":37.5512, "lon":126.9882, "desc":"Observation tower with panoramic views of Seoul. Popular at sunset and night."},
    {"name":"Myeongdong Shopping Street", "lat":37.5609, "lon":126.9860, "desc":"Major shopping district for cosmetics, fashion, and street food."},
    {"name":"Insadong", "lat":37.5740, "lon":126.9849, "desc":"Cultural streets with galleries, craft shops and tea houses — great for souvenirs."},
    {"name":"Dongdaemun Design Plaza (DDP)", "lat":37.5663, "lon":127.0090, "desc":"Futuristic cultural complex and night market area, famous for fashion and design."},
    {"name":"Hongdae (Hongik University area)", "lat":37.5563, "lon":126.9230, "desc":"Youthful area known for indie music, cafes, street performances and nightlife."},
    {"name":"Gwangjang Market", "lat":37.5704, "lon":126.9998, "desc":"One of Korea's oldest traditional markets, famous for local street foods like bindaetteok and mayak kimbap."},
    {"name":"Lotte World Tower & Mall (Jamsil)", "lat":37.5131, "lon":127.1025, "desc":"Korea's tallest building with an observation deck, shopping center and aquarium."},
]

# Sidebar controls
st.sidebar.header("Map controls")
show_all = st.sidebar.checkbox("Show all top 10", value=True)
selected = []
if not show_all:
    choices = [p["name"] for p in PLACES]
    selected = st.sidebar.multiselect("Select places to display", choices, default=choices[:5])
else:
    selected = [p["name"] for p in PLACES]

zoom_to = st.sidebar.selectbox("Center map on...", ["Seoul (default)"] + [p["name"] for p in PLACES])

# Create folium map centered on Seoul
center = (37.5665, 126.9780)  # Seoul city center
m = folium.Map(location=center, zoom_start=12, control_scale=True)

# Add markers
for place in PLACES:
    if place["name"] in selected:
        folium.Marker(
            location=(place["lat"], place["lon"]),
            popup=f"<b>{place['name']}</b><br>{place['desc']}",
            tooltip=place["name"],
        ).add_to(m)

# If the user chose to zoom to a specific place, re-center and zoom
if zoom_to != "Seoul (default)":
    target = next((p for p in PLACES if p["name"] == zoom_to), None)
    if target:
        m.location = (target["lat"], target["lon"])
        m.zoom_start = 15

# Display map with streamlit-folium
st.subheader("Map")
st_data = st_folium(m, width=1000, height=600)

# Show a quick list of places and small info cards
st.subheader("Seoul Top 10 — Quick list")
cols = st.columns(2)
for i, p in enumerate(PLACES):
    with cols[i % 2]:
        st.markdown(f"**{i+1}. {p['name']}**")
        st.write(p['desc'])

st.markdown("---")
st.caption("Data sources: Korea tourism sites, TripAdvisor and travel guides (used to pick the top attractions). Coordinates are approximate.")

# Footer: small tips
st.info("Tip: click a marker on the map to open a popup, or use the sidebar to focus the map. 즐거운 여행 되세요! ✈️🇰🇷")


# Requirements text (for convenience, duplicated in requirements.txt file when you deploy)
# requirements.txt contents:
# streamlit
# folium
# streamlit-folium

# End of file
