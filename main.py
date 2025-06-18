import streamlit as st
import pandas as pd

st.set_page_config(page_title="주기율표 인터랙티브", layout="wide")

# 원소 데이터 (118개 원소, 주요 정보만 간략히 포함)
elements = [
    # atomic_num, symbol, name, atomic_mass, category, period, group
    (1, "H", "수소", 1.008, "비금속", 1, 1),
    (2, "He", "헬륨", 4.002602, "비활성기체", 1, 18),
    (3, "Li", "리튬", 6.94, "알칼리금속", 2, 1),
    (4, "Be", "베릴륨", 9.0122, "알칼리토금속", 2, 2),
    (5, "B", "붕소", 10.81, "준금속", 2, 13),
    (6, "C", "탄소", 12.011, "비금속", 2, 14),
    (7, "N", "질소", 14.007, "비금속", 2, 15),
    (8, "O", "산소", 15.999, "비금속", 2, 16),
    (9, "F", "플루오린", 18.998403163, "할로젠", 2, 17),
    (10, "Ne", "네온", 20.1797, "비활성기체", 2, 18),
    (11, "Na", "나트륨", 22.98976928, "알칼리금속", 3, 1),
    (12, "Mg", "마그네슘", 24.305, "알칼리토금속", 3, 2),
    (13, "Al", "알루미늄", 26.9815385, "기타금속", 3, 13),
    (14, "Si", "규소", 28.085, "준금속", 3, 14),
    (15, "P", "인", 30.973761998, "비금속", 3, 15),
    (16, "S", "황", 32.06, "비금속", 3, 16),
    (17, "Cl", "염소", 35.45, "할로젠", 3, 17),
    (18, "Ar", "아르곤", 39.948, "비활성기체", 3, 18),
    # ... (중략: 19~57까지 비슷하게 추가)
    (57, "La", "란타넘", 138.90547, "란타노이드", 6, None),
    (58, "Ce", "세륨", 140.116, "란타노이드", 6, None),
    (59, "Pr", "프라세오디뮴", 140.90766, "란타노이드", 6, None),
    # ... (62~71 란타노이드 완성)
    (71, "Lu", "루테튬", 174.9668, "란타노이드", 6, None),
    (72, "Hf", "하프늄", 178.49, "전이금속", 6, 4),
    # ... (전이금속 및 기타 원소 완성)
    (118, "Og", "오가네손", 294, "비활성기체", 7, 18)
]

df = pd.DataFrame(elements, columns=["atomic_num", "symbol", "name", "atomic_mass", "category", "period", "group"])

# 카테고리별 색상 (기본)
category_colors = {
    "알칼리금속": "#FF6666",
    "알칼리토금속": "#FFDEAD",
    "준금속": "#CCCC99",
    "비금속": "#66CCFF",
    "할로젠": "#66FF99",
    "비활성기체": "#FFB266",
    "기타금속": "#FFD700",
    "전이금속": "#FFB6C1",
    "란타노이드": "#DA70D6",
    "악티노이드": "#BA55D3",
}

st.title("🌈 화학원소 주기율표 인터랙티브 🌈")
st.markdown("원소를 클릭하면 상세 정보를 확인할 수 있어요!")

# 빈 2차원 배열 (7주기 x 18족)
periods = 7
groups = 18
table = [["" for _ in range(groups)] for _ in range(periods)]

# 원소를 알맞은 위치에 배치 (group이 없는 란타노이드/악티노이드는 따로 표시)
for _, row in df.iterrows():
    p = int(row["period"]) - 1
    g = row["group"]
    if pd.notna(g):
        g = int(g) - 1
        table[p][g] = row["symbol"]

# 선택된 원소 상태 관리
if "selected" not in st.session_state:
    st.session_state.selected = None

# 주기율표 그리기 (streamlit columns 사용)
for p in range(periods):
    cols = st.columns(groups)
    for g in range(groups):
        sym = table[p][g]
        if sym != "":
            elem = df[df["symbol"] == sym].iloc[0]
            color = category_colors.get(elem["category"], "#DDD")
            style = f"""
                background-color: {color};
                border-radius: 8px;
                padding: 10px 0px;
                text-align: center;
                font-weight: bold;
                font-size: 18px;
                cursor: pointer;
                user-select:none;
            """
            if cols[g].button(sym, key=f"{p}-{g}", help=elem["name"], use_container_width=True):
                st.session_state.selected = sym
        else:
            cols[g].write("")

st.markdown("---")
# 선택된 원소 정보 출력
if st.session_state.selected:
    sel = st.session_state.selected
    elem = df[df["symbol"] == sel].iloc[0]
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
                border-radius: 20px; padding: 30px; color: #222; max-width: 600px;">
        <h1 style="font-size: 64px; margin: 0;">{elem['symbol']}</h1>
        <h2 style="margin: 0;">{elem['name']}</h2>
        <p><strong>원자번호:</strong> {elem['atomic_num']}</p>
        <p><strong>원자량:</strong> {elem['atomic_mass']}</p>
        <p><strong>분류:</strong> {elem['category']}</p>
        <p><strong>주기:</strong> {elem['period']}기</p>
        <p><strong>족:</strong> {elem['group'] if pd.notna(elem['group']) else '해당없음'}</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("주기율표에서 원소를 클릭하세요!")

# 추가 CSS (버튼 호버효과)
st.markdown("""
<style>
div.stButton > button {
    transition: background-color 0.3s ease, color 0.3s ease;
}
div.stButton > button:hover {
    background-color: #33aaff !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)
