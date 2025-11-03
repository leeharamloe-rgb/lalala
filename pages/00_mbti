# app.py
import streamlit as st
import textwrap
from datetime import datetime

st.set_page_config(page_title="MBTI별 진로 추천 🎯", layout="centered")

st.title("✨ MBTI로 찾는 내 진로 추천기")
st.caption("친근하게, 쓱 골라볼래? 😄 (설치 불필요 — Streamlit만 있으면 OK)")

mbti_list = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 추천 데이터: 각 MBTI -> 두 개의 진로(이모지 포함), 적합 학과, 어울리는 성격
recommendations = {
    "ISTJ": [
        {"job": "회계사 📊", "majors": ["세무·회계학과", "경영학과"], "personality": "정확하고 책임감 있는 사람. 규칙과 절차를 잘 지켜요."},
        {"job": "공무원 🏛️", "majors": ["행정학과", "법학과"], "personality": "안정적이고 성실한 성향. 꾸준함이 강점이에요."}
    ],
    "ISFJ": [
        {"job": "간호사 🩺", "majors": ["간호학과"], "personality": "세심하고 타인을 돌보는 걸 좋아하는 사람."},
        {"job": "사회복지사 🤝", "majors": ["사회복지학과"], "personality": "따뜻한 공감력과 봉사정신이 있어요."}
    ],
    "INFJ": [
        {"job": "상담심리사 🧠", "majors": ["심리학과", "상담심리학과"], "personality": "사람의 내면을 이해하려는 통찰력이 있어요."},
        {"job": "작가 / 콘텐츠 창작자 ✍️", "majors": ["문예창작과", "국어국문학과"], "personality": "가치 지향적이고 표현력이 풍부해요."}
    ],
    "INTJ": [
        {"job": "연구원 🔬", "majors": ["전공(자연·공학·인문) 중 심화"], "personality": "논리적이고 계획적으로 문제를 해결해요."},
        {"job": "전략 컨설턴트 ♟️", "majors": ["경영학과", "통계·수학"], "personality": "전략적 사고와 독립적인 판단을 잘 해요."}
    ],
    "ISTP": [
        {"job": "기계·설비 엔지니어 ⚙️", "majors": ["기계공학과", "산업공학과"], "personality": "실습과 손으로 직접 해결하는 걸 잘해요."},
        {"job": "산업디자이너 / 제작자 🛠️", "majors": ["산업디자인과", "시각디자인과"], "personality": "실용적 감각과 문제해결 능력이 뛰어나요."}
    ],
    "ISFP": [
        {"job": "그래픽/패션 디자이너 🎨", "majors": ["디자인계열(시각/패션)"], "personality": "감성적이고 미적 감각이 뛰어나요."},
        {"job": "셰프 / 제과제빵사 🍰", "majors": ["조리·제과제빵학과"], "personality": "손으로 표현하는 걸 즐기고 섬세해요."}
    ],
    "INFP": [
        {"job": "작가 / 크리에이터 📝", "majors": ["문예창작과", "커뮤니케이션"], "personality": "이상과 감성을 표현하는 걸 좋아해요."},
        {"job": "예술치료사 / 상담가 💬", "majors": ["심리학과", "미술치료 관련"], "personality": "타인의 성장에 공감하고 돕는 걸 즐겨요."}
    ],
    "INTP": [
        {"job": "소프트웨어 개발자 💻", "majors": ["컴퓨터공학과", "정보통신"], "personality": "호기심이 많고 논리적 분석을 즐겨요."},
        {"job": "연구·분석가 📚", "majors": ["수학/통계/과학 계열"], "personality": "복잡한 문제를 깊게 파고드는 걸 좋아해요."}
    ],
    "ESTP": [
        {"job": "영업/마케팅 담당자 🚀", "majors": ["경영학과", "광고홍보학과"], "personality": "즉흥적이지만 사람을 끌어당기는 에너지가 있어요."},
        {"job": "이벤트 기획자 🎪", "majors": ["관광·레저학과", "커뮤니케이션"], "personality": "현장 중심으로 빠르게 처리하는 능력이 뛰어나요."}
    ],
    "ESFP": [
        {"job": "공연예술가 (연기·음악) 🎭", "majors": ["공연예술계열"], "personality": "활발하고 사람 앞에서 빛나는 타입이에요."},
        {"job": "이벤트/서비스 매니저 🎉", "majors": ["관광경영학과", "서비스경영"], "personality": "사교성이 좋아서 고객 응대가 탁월해요."}
    ],
    "ENFP": [
        {"job": "콘텐츠 크리에이터 / 창작자 📱", "majors": ["커뮤니케이션", "디자인"], "personality": "아이디어가 많고 사람을 즐겁게 해요."},
        {"job": "창업가 / 스타트업 운영자 🚀", "majors": ["경영학과", "융합전공"], "personality": "도전적이고 새로운 걸 시도하는 걸 좋아해요."}
    ],
    "ENTP": [
        {"job": "스타트업 창업자 / 기획자 🧠", "majors": ["경영학과", "컴퓨터공학"], "personality": "아이디어와 토론을 즐기며 빠른 피드백을 잘받아요."},
        {"job": "전략기획 / 제품매니저 (PM) 📈", "majors": ["경영학과", "IT계열"], "personality": "다방면 지식으로 연결고리를 잘 찾아요."}
    ],
    "ESTJ": [
        {"job": "기업 관리자 / 운영 매니저 🧾", "majors": ["경영학과", "회계학과"], "personality": "조직 운영과 규율을 잘 세우는 편이에요."},
        {"job": "교사 / 교육행정가 🎓", "majors": ["교육학과"], "personality": "체계적이고 지도력을 발휘하는 타입."}
    ],
    "ESFJ": [
        {"job": "초등교사 / 상담교사 🏫", "majors": ["교육학과", "아동학"], "personality": "사람 돌보는 걸 좋아하고 협동심이 높아요."},
        {"job": "홍보·고객관리 (PR/CS) 💌", "majors": ["커뮤니케이션", "경영학"], "personality": "친절하고 타인을 잘 챙겨요."}
    ],
    "ENFJ": [
        {"job": "HR / 조직개발 담당자 👥", "majors": ["심리학과", "경영학"], "personality": "사람을 이끄는 능력과 공감능력이 뛰어나요."},
        {"job": "코치 / 강연자 🎤", "majors": ["심리학과", "교육학"], "personality": "타인의 성장에 에너지를 쏟는 타입."}
    ],
    "ENTJ": [
        {"job": "CEO / 기업 경영자 🦁", "majors": ["경영학과", "경제학과"], "personality": "목표지향적이고 결단력이 있어요."},
        {"job": "변호사 / 정책분석가 ⚖️", "majors": ["법학과", "정치외교학과"], "personality": "논리적이며 큰 그림을 잘 보는 편."}
    ]
}

st.write("아래에서 너의 MBTI를 골라줘 ➡️")

col1, col2 = st.columns([2,1])
with col1:
    choice = st.selectbox("MBTI 선택", mbti_list, index=0)
with col2:
    # 작은 팁 박스
    st.write("💡 팁: MBTI 모르면 'ENFP' 눌러서 테스트 느낌으로 해봐!")

st.markdown("---")

if choice:
    st.header(f"너의 유형: {choice}  ✨")
    st.write("두 가지 진로를 추천해줄게 — 각각 펼쳐서 자세히 볼 수 있어요.")

    recs = recommendations.get(choice, [])
    all_text_parts = []
    for i, r in enumerate(recs, start=1):
        title = f"{i}. {r['job']}"
        with st.expander(title, expanded=(i==1)):
            st.markdown(f"**어울리는 전공(학과)**: {', '.join(r['majors'])}")
            st.markdown(f"**어울리는 성격**: {r['personality']}")
            # 친근한 조언 한 줄
            advice = {
                1: "작게라도 직접 체험해보면 생각이 확실해져요 — 동아리, 체험수업, 인턴 등 추천! 😉",
                2: "관련 책이나 유튜브로 미리 맛보기 해보면 진로 선택에 큰 도움이 돼요. 📚"
            }.get(i, "체험해보는 걸 권해요!")
            st.info(advice)

            # 텍스트 요약을 위해 합치기
            part = textwrap.dedent(f"""
            {title}
            전공: {', '.join(r['majors'])}
            성격특징: {r['personality']}
            """).strip()
            all_text_parts.append(part)

    # 전체 요약 텍스트 생성 (다운로드용)
    summary_txt = f"MBTI: {choice}\n추천일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    summary_txt += "\n\n".join(all_text_parts)
    summary_txt += "\n\n(이 정보는 참고용이에요! 너의 흥미와 경험이 제일 중요해요 😊)"

    st.markdown("---")
    st.subheader("요약 다운로드 💾")
    st.write("추천 내용을 파일로 저장해서 나중에 보자구!")
    st.download_button("📥 추천 결과 내려받기 (txt)", data=summary_txt, file_name=f"mbti_{choice}_recommendation.txt", mime="text/plain")

    st.markdown("---")
    st.write("마지막으로 한 마디 🤗")
    st.success("진로는 고정된 정답이 아니에요 — 다양한 경험을 통해 관심을 키우면 돼요. 궁금하면 또 같이 정리해줄게!")
