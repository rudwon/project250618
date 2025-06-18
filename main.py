import streamlit as st

# 118개 원소 데이터 (필수 정보만 간략화)
elements = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "weight": 1.008, "category": "Nonmetal", "description": "The lightest and most abundant element in the universe."},
    "He": {"name": "Helium", "atomic_number": 2, "weight": 4.0026, "category": "Noble Gas", "description": "A colorless, odorless inert gas used in balloons."},
    "Li": {"name": "Lithium", "atomic_number": 3, "weight": 6.94, "category": "Alkali Metal", "description": "A soft, silvery metal used in batteries."},
    "Be": {"name": "Beryllium", "atomic_number": 4, "weight": 9.0122, "category": "Alkaline Earth Metal", "description": "A hard, gray metal used in aerospace materials."},
    "B": {"name": "Boron", "atomic_number": 5, "weight": 10.81, "category": "Metalloid", "description": "Used in glass and detergents."},
    "C": {"name": "Carbon", "atomic_number": 6, "weight": 12.011, "category": "Nonmetal", "description": "Basis of organic life."},
    "N": {"name": "Nitrogen", "atomic_number": 7, "weight": 14.007, "category": "Nonmetal", "description": "Makes up most of Earth’s atmosphere."},
    "O": {"name": "Oxygen", "atomic_number": 8, "weight": 15.999, "category": "Nonmetal", "description": "Essential for respiration."},
    "F": {"name": "Fluorine", "atomic_number": 9, "weight": 18.998, "category": "Halogen", "description": "A highly reactive gas."},
    "Ne": {"name": "Neon", "atomic_number": 10, "weight": 20.180, "category": "Noble Gas", "description": "Used in neon lights."},
    # ... 11부터 117까지는 예시 생략, 필요시 추가 가능 ...
    "Og": {"name": "Oganesson", "atomic_number": 118, "weight": 294, "category": "Noble Gas", "description": "A synthetic element, very unstable."}
}

# 주기율표의 원소 위치(가로: 18, 세로: 7)  
# 빈칸은 ""로 표시. 주기율표 배열은 7행 18열로 표준 주기율표 형태.
periodic_table_layout = [
    ["H",  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],
]

# 란타넘과 악티늄 족(내부전이족)
lanthanides = ["Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
actinides = ["Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

# 란타넘족과 악티늄족 위치 표시
lanth_row = ["", "", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "", ""]
actin_row = ["", "", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "", ""]

# 카테고리별 색상표
category_colors = {
    "Nonmetal": "#4caf50",
    "Noble Gas": "#2196f3",
    "Alkali Metal": "#ff5722",
    "Alkaline Earth Metal": "#ff9800",
    "Metalloid": "#9c27b0",
    "Halogen": "#e91e63",
    "Lanthanide": "#ffb300",
    "Actinide": "#ff6f00",
    "Transition Metal": "#009688",
    "Post-Transition Metal": "#607d8b",
    "": "#e0e0e0"
}

# 각 원소 카테고리 분류 (간단히 분류 - 더 세밀한 분류 가능)
transition_metals = ["Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn",
                     "Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd",
                     "Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
                     "Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn"]

post_transition_metals = ["Al","Ga","In","Sn","Tl","Pb","Bi","Nh","Fl","Mc","Lv"]

# 각 원소에 카테고리 자동 매핑
for el in elements.keys():
    if el in transition_metals:
        elements[el]["category"] = "Transition Metal"
    elif el in post_transition_metals:
        elements[el]["category"] = "Post-Transition Metal"
    elif el in lanthanides:
        elements[el]["category"] = "Lanthanide"
    elif el in actinides:
        elements[el]["category"] = "Actinide"
    elif el not in elements or "category" not in elements[el]:
        elements.setdefault(el, {"category": ""})

# 기본 세팅
st.set_page_config(page_title="✨화려한 주기율표✨", layout="wide")

# CSS 꾸미기 + 애니메이션
st.markdown("""
<style>
/* 기본 레이아웃 */
body {
    background: linear-gradient(120deg, #1f1c2c, #928dab);
    color: #eee;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    user-select: none;
}
h1 {
    text-align: center;
    margin-bottom: 10px;
    text-shadow: 3px 3px 8px #000;
}

/* 주기율표 컨테이너 */
.periodic-table {
    display: grid;
    grid-template-columns: repeat(18, 60px);
    gap: 6px;
    padding: 10px;
    background: rgba(255,255,255,0.1);
    border-radius: 16px;
    max-height: 600px;
    overflow-y: auto;
    box-shadow: 0 0 25px rgba(0,0,0,0.5);
}

/* 원소 박스 */
.element {
    border-radius: 10px;
    text-align: center;
    padding: 8px 4px;
    cursor: pointer;
    transition: all 0.3s ease;
    color: white;
    box-shadow: 0 3px 6px rgba(0,0,0,0.5);
    user-select: none;
}
.element:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 12px rgba(0,0,0,0.8);
    z-index: 10;
}

/* 선택된 원소 강조 */
.element.selected {
    box-shadow: 0 0 20px 4px #fff;
    transform: scale(1.15);
}

/* 원자번호 */
.atomic-number {
    font-size: 11px;
    font-weight: 600;
    opacity: 0.8;
}

/* 원소기호 */
.symbol {
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 1.5px;
}

/* 원소 이름 */
.name {
    font-size: 9px;
    margin-top: 2px;
    font-weight: 700;
    opacity: 0.85;
}

/* 상세정보 박스 */
.info-box {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 24px;
    padding: 30px;
    color: white;
    box-shadow: 0 0 25px rgba(0,0,0,0.6);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    user-select: text;
    max-height: 600px;
    overflow-y: auto;
}

/* 제목 */
.info-box h2 {
    margin-top: 0;
    font-size: 40px;
    letter-spacing: 3px;
    text-shadow: 3px 3px 8px rgba(0,0,0,0.7);
}

/* 부제목 */
.info-box .subtitle {
    font-size: 16px;
    margin-bottom: 20px;
    font-weight: 600;
    text-transform: uppercase;
    opacity: 0.8;
}

/* 설명 */
.info-box p {
    font-size: 18px;
    line-height: 1.5;
}

/* 스크롤바 꾸미기 */
.periodic-table::-webkit-scrollbar {
    width: 8px;
}
.periodic-table::-webkit-scrollbar-thumb {
    background-color: #764ba2;
    border-radius: 10px;
}
.periodic-table::-webkit-scrollbar-track {
    background-color: transparent;
}

/* 왼쪽 고정, 오른쪽 고정 */
.app-container {
    display: flex;
    gap: 24px;
    height: 650px;
}
.left-panel {
    flex: 1.2;
    max-width: 1200px;
}
.right-panel {
    flex: 1;
    min-width: 350px;
}
</style>
""", unsafe_allow_html=True)

st.title("✨ 화려한 주기율표 ✨")
st.write("원소기호를 클릭
