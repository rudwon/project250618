import streamlit as st

# 원소 상세 데이터 일부 예시 (필요시 더 확장 가능)
detailed_info = {
    "H": {"name": "수소", "number": 1, "weight": 1.008, "desc": "우주에서 가장 가벼운 원소로, 연료 및 화학 반응에 중요합니다."},
    "He": {"name": "헬륨", "number": 2, "weight": 4.0026, "desc": "비활성 기체로 풍선과 냉각에 사용됩니다."},
    "Fe": {"name": "철", "number": 26, "weight": 55.845, "desc": "건축과 공학에 많이 사용되는 금속입니다."},
    "Au": {"name": "금", "number": 79, "weight": 196.97, "desc": "귀금속으로, 장신구와 전자제품에 사용됩니다."},
    "O": {"name": "산소", "number": 8, "weight": 15.999, "desc": "호흡에 필수적인 원소로, 대기 중 약 21%를 차지합니다."},
}

def get_element_info(symbol):
    if symbol in detailed_info:
        return detailed_info[symbol]
    else:
        return {
            "name": f"원소 {symbol}",
            "number": "N/A",
            "weight": "N/A",
            "desc": f"{symbol} 원소에 대한 상세 정보가 준비 중입니다."
        }

# 주기율표 배치 (1~7주기, 18족)
# 빈 칸은 빈 문자열 "" 로 채움
periodic_table = [
    # 1주기
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    # 2주기
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
    # 3주기
    ["Na", "Mg", "", "", "", "", "", "", "", "", "", "", "Al", "Si", "P", "S", "Cl", "Ar"],
    # 4주기
    ["K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr"],
    # 5주기
    ["Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe"],
    # 6주기
    ["Cs", "Ba", "La", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn"],
    # 7주기
    ["Fr", "Ra", "Ac", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"],
]

# 란타넘족과 악티늄족은 따로 표시 (주기 6,7 아래)
lanthanides = ["Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu"]
actinides  = ["Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]

st.set_page_config(page_title="주기율표 원소 소개", layout="wide")

st.title("🌟 주기율표 원소 소개 🌟")
st.write("원소 기호를 눌러 상세 정보를 확인하세요!")

selected_element = None

# 주기율표 표시
for period in periodic_table:
    cols = st.columns(len(period))
    for i, symbol in enumerate(period):
        if symbol == "":
            cols[i].write("")  # 빈 칸
        else:
            if cols[i].button(symbol):
                selected_element = symbol

st.write("---")
# 란타넘족과 악티늄족 별도 표시
st.write("### 란타넘족 (Lanthanides)")
cols = st.columns(len(lanthanides))
for i, sym in enumerate(lanthanides):
    if cols[i].button(sym):
        selected_element = sym

st.write("### 악티늄족 (Actinides)")
cols = st.columns(len(actinides))
for i, sym in enumerate(actinides):
    if cols[i].button(sym):
        selected_element = sym

# 클릭한 원소 정보 출력
if selected_element:
    info = get_element_info(selected_element)
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
                    border-radius: 15px; padding: 20px; margin-top: 20px;
                    box-shadow: 0 8px 16px rgba(0,0,0,0.3); color: white;">
            <h2 style="text-align:center;">{info['name']} ({selected_element})</h2>
            <h4 style="text-align:center;">원자번호: {info['number']} | 원자량: {info['weight']}</h4>
            <p style="font-size:18px; text-align:center;">{info['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
