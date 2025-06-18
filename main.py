import streamlit as st

# 원소 데이터 (간단히 몇 개만 넣었어요, 실제론 더 추가 가능)
elements = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "weight": 1.008, "category": "Nonmetal", "description": "Hydrogen is the lightest element."},
    "He": {"name": "Helium", "atomic_number": 2, "weight": 4.0026, "category": "Noble Gas", "description": "Helium is a colorless, inert gas."},
    "Li": {"name": "Lithium", "atomic_number": 3, "weight": 6.94, "category": "Alkali Metal", "description": "Lithium is a soft, silvery metal."},
    "Be": {"name": "Beryllium", "atomic_number": 4, "weight": 9.0122, "category": "Alkaline Earth Metal", "description": "Beryllium is a hard, gray metal."},
    "B": {"name": "Boron", "atomic_number": 5, "weight": 10.81, "category": "Metalloid", "description": "Boron is a metalloid element."},
    "C": {"name": "Carbon", "atomic_number": 6, "weight": 12.011, "category": "Nonmetal", "description": "Carbon is the basis of organic life."},
    "N": {"name": "Nitrogen", "atomic_number": 7, "weight": 14.007, "category": "Nonmetal", "description": "Nitrogen makes up 78% of Earth's atmosphere."},
    "O": {"name": "Oxygen", "atomic_number": 8, "weight": 15.999, "category": "Nonmetal", "description": "Oxygen supports combustion and respiration."},
    "F": {"name": "Fluorine", "atomic_number": 9, "weight": 18.998, "category": "Halogen", "description": "Fluorine is a highly reactive gas."},
    "Ne": {"name": "Neon", "atomic_number": 10, "weight": 20.180, "category": "Noble Gas", "description": "Neon is used in glowing signs."},
}

# 주기율표 간단 레이아웃 (여기서는 2주기까지만 간단히)
periodic_table = [
    ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    ["Li", "Be", "", "", "", "", "", "", "", "", "", "", "B", "C", "N", "O", "F", "Ne"],
]

# 카테고리별 색상
category_colors = {
    "Nonmetal": "#4caf50",
    "Noble Gas": "#2196f3",
    "Alkali Metal": "#ff5722",
    "Alkaline Earth Metal": "#ff9800",
    "Metalloid": "#9c27b0",
    "Halogen": "#e91e63",
    "": "#eeeeee"
}

st.set_page_config(page_title="화려한 주기율표", layout="wide")

st.markdown("""
<style>
    .element {
        border-radius: 8px;
        width: 60px;
        height: 70px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin: 4px;
        cursor: pointer;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.2s ease-in-out;
    }
    .element:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 12px rgba(0,0,0,0.4);
    }
    .symbol {
        font-size: 24px;
        font-weight: bold;
    }
    .atomic-number {
        font-size: 12px;
        opacity: 0.7;
    }
    .element-container {
        display: flex;
        flex-wrap: nowrap;
        justify-content: center;
        margin-bottom: 4px;
    }
    .info-box {
        border-radius: 12px;
        padding: 24px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .info-title {
        font-size: 36px;
        font-weight: 900;
        margin-bottom: 8px;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .info-subtitle {
        font-size: 16px;
        margin-bottom: 16px;
        font-weight: 600;
        text-transform: uppercase;
        opacity: 0.8;
    }
    .info-description {
        font-size: 18px;
        line-height: 1.4;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔥 화려한 주기율표 🔥")
st.write("원소기호를 클릭하면 자세한 정보를 보여줍니다.")

col1, col2 = st.columns([2, 3])

with col1:
    for period in periodic_table:
        cols = st.columns(len(period))
        for i, symbol in enumerate(period):
            if symbol == "":
                cols[i].write("")
            else:
                element = elements.get(symbol)
                color = category_colors.get(element["category"], "#999999") if element else "#999999"
                if cols[i].button(f"{symbol}", key=symbol, help=element["name"] if element else ""):
                    st.session_state.selected = symbol

if "selected" not in st.session_state:
    st.session_state.selected = "H"

selected_element = elements.get(st.session_state.selected)

with col2:
    if selected_element:
        st.markdown(f"""
        <div class="info-box">
            <div class="info-title">{selected_element['name']} ({st.session_state.selected})</div>
            <div class="info-subtitle">Atomic Number: {selected_element['atomic_number']} | Atomic Weight: {selected_element['weight']} | Category: {selected_element['category']}</div>
            <div class="info-description">{selected_element['description']}</div>
        </div>
        """, unsafe_allow_html=True)
