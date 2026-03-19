import streamlit as st
from datetime import datetime, date, timedelta
import json
import os

st.set_page_config(page_title="Meus Cortes", layout="centered", page_icon="✂️")

# ====== CSS ======
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600&display=swap');

*, body, .stApp {
    background-color: #0f0f0f;
    color: #f5f5f0;
}

h1, h2, h3 {
    font-family: 'Bebas Neue', sans-serif !important;
    letter-spacing: 2px !important;
    color: #f5f5f0 !important;
}

p, span, div, label, .stWrite {
    font-family: 'DM Sans', sans-serif !important;
}

.topo {
    text-align: center;
    padding: 20px 0 10px;
}

.topo-titulo {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 64px;
    line-height: 1;
    color: #f5f5f0;
    letter-spacing: 4px;
}

.topo-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: #666;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
}

.semana-badge {
    display: inline-block;
    background: #1a1a1a;
    border: 1px solid #2a2a2a;
    padding: 6px 18px;
    border-radius: 50px;
    font-size: 12px;
    color: #888;
    font-family: 'DM Sans', sans-serif;
    letter-spacing: 1px;
    margin-top: 10px;
}

.total-card {
    background: linear-gradient(135deg, #1c1c1c, #242424);
    border: 1px solid #2e2e2e;
    border-radius: 16px;
    padding: 28px 32px;
    margin: 16px 0;
    position: relative;
    overflow: hidden;
}

.total-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #c8a96e, #f0d080, #c8a96e);
}

.total-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #666;
    margin-bottom: 8px;
}

.total-valor {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 56px;
    color: #c8a96e;
    letter-spacing: 2px;
    line-height: 1;
}

.total-qtd {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: #555;
    margin-top: 8px;
}

.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: #1a1a1a !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 10px !important;
    color: #f5f5f0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    padding: 10px 14px !important;
    transition: border-color 0.2s ease !important;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: #c8a96e !important;
    box-shadow: 0 0 0 3px rgba(200, 169, 110, 0.1) !important;
}

.stTextInput label, .stNumberInput label {
    color: #888 !important;
    font-size: 12px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    font-family: 'DM Sans', sans-serif !important;
}

.stButton > button {
    background: #c8a96e !important;
    color: #0f0f0f !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 18px !important;
    letter-spacing: 2px !important;
    padding: 10px 28px !important;
    width: 100% !important;
    transition: transform 0.15s ease, filter 0.15s ease, box-shadow 0.15s ease !important;
    box-shadow: 0 4px 20px rgba(200, 169, 110, 0.2) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    filter: brightness(1.1) !important;
    box-shadow: 0 8px 30px rgba(200, 169, 110, 0.35) !important;
}

.stButton > button:active {
    transform: scale(0.97) !important;
    filter: brightness(0.95) !important;
}

.corte-item {
    background: #1a1a1a;
    border: 1px solid #252525;
    border-radius: 12px;
    padding: 14px 18px;
    margin: 8px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'DM Sans', sans-serif;
}

.corte-nome {
    font-size: 15px;
    font-weight: 500;
    color: #e0e0e0;
}

.corte-hora {
    font-size: 11px;
    color: #555;
    margin-top: 3px;
}

.corte-valor {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 22px;
    color: #c8a96e;
    letter-spacing: 1px;
}

.corte-idx {
    font-size: 11px;
    color: #444;
    margin-right: 12px;
    font-family: 'Bebas Neue', sans-serif;
    letter-spacing: 1px;
}

.vazio {
    text-align: center;
    color: #444;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    padding: 32px 0;
    border: 1px dashed #2a2a2a;
    border-radius: 12px;
    margin: 8px 0;
}

hr {
    border-color: #1e1e1e !important;
    margin: 20px 0 !important;
}

.stAlert {
    background: #1a1a1a !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 10px !important;
    color: #888 !important;
}

.zerar > button {
    background: transparent !important;
    color: #555 !important;
    border: 1px solid #2a2a2a !important;
    font-size: 13px !important;
    letter-spacing: 1px !important;
    box-shadow: none !important;
    font-family: 'DM Sans', sans-serif !important;
    padding: 6px 20px !important;
}

.zerar > button:hover {
    border-color: #e05555 !important;
    color: #e05555 !important;
    transform: none !important;
    filter: none !important;
    box-shadow: none !important;
}

.stTabs [data-baseweb="tab-list"] {
    background: #1a1a1a !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 4px !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 8px !important;
    color: #666 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    letter-spacing: 1px !important;
}

.stTabs [aria-selected="true"] {
    background: #c8a96e !important;
    color: #0f0f0f !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)


ARQUIVO = "cortes.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_dados(cortes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(cortes, f, ensure_ascii=False, indent=2)

def fmt_valor(valor):
    return f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

# ====== CARREGAR NA SESSION STATE ======
if "cortes" not in st.session_state:
    st.session_state.cortes = carregar_dados()

# ====== SEMANA ATUAL ======
hoje = date.today()
inicio_semana = hoje - timedelta(days=hoje.weekday())
fim_semana = inicio_semana + timedelta(days=6)

def e_da_semana_atual(corte):
    try:
        dia = datetime.strptime(corte["data_completa"], "%Y-%m-%d").date()
        return inicio_semana <= dia <= fim_semana
    except:
        return False

cortes_semana = [c for c in st.session_state.cortes if e_da_semana_atual(c)]

# ====== TOPO ======
st.markdown("""
<div class="topo">
    <div class="topo-titulo">✂ GEIS CORTES</div>
    <div class="topo-sub">Controle semanal de atendimentos</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style="text-align:center">
    <span class="semana-badge">📅 Semana: {inicio_semana.strftime('%d/%m')} — {fim_semana.strftime('%d/%m/%Y')}</span>
</div>
<br>
""", unsafe_allow_html=True)

# ====== TOTAL DA SEMANA ======
total = sum(c["valor"] for c in cortes_semana)
qtd = len(cortes_semana)

st.markdown(f"""
<div class="total-card">
    <div class="total-label">💰 Total da semana</div>
    <div class="total-valor">R$ {fmt_valor(total)}</div>
    <div class="total-qtd">{qtd} corte{"s" if qtd != 1 else ""} registrado{"s" if qtd != 1 else ""} essa semana</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ====== ABAS ======
aba1, aba2 = st.tabs(["✂️  Semana Atual", "📋  Histórico Completo"])

# ====== ABA 1: SEMANA ATUAL ======
with aba1:
    st.markdown("### ADICIONAR CORTE")

    col1, col2 = st.columns([2, 1])
    with col1:
        nome = st.text_input("Nome do cliente", placeholder="Ex: João Silva")
    with col2:
        valor = st.number_input("Valor (R$)", min_value=0.0, step=0.50, format="%.2f")

    if st.button("＋  REGISTRAR CORTE", key="adicionar"):
        if nome.strip() == "":
            st.warning("⚠️ Digite o nome do cliente.")
        elif valor <= 0:
            st.warning("⚠️ Digite um valor maior que zero.")
        else:
            novo = {
                "nome": nome.strip(),
                "valor": valor,
                "hora": datetime.now().strftime("%H:%M"),
                "dia": datetime.now().strftime("%d/%m"),
                "data_completa": date.today().isoformat()
            }
            st.session_state.cortes.append(novo)
            salvar_dados(st.session_state.cortes)
            st.rerun()

    st.divider()
    st.markdown("### CORTES DA SEMANA")

    cortes_semana_reverso = list(reversed(cortes_semana))

    if not cortes_semana_reverso:
        st.markdown('<div class="vazio">Nenhum corte registrado essa semana.<br>Adicione o primeiro acima ✂️</div>', unsafe_allow_html=True)
    else:
        for i, corte in enumerate(cortes_semana_reverso):
            idx = len(cortes_semana) - i
            st.markdown(f"""
            <div class="corte-item">
                <div style="display:flex; align-items:center;">
                    <span class="corte-idx">#{idx:02d}</span>
                    <div>
                        <div class="corte-nome">{corte['nome']}</div>
                        <div class="corte-hora">✂ {corte['dia']} às {corte['hora']}</div>
                    </div>
                </div>
                <div class="corte-valor">R$ {fmt_valor(corte['valor'])}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="zerar">', unsafe_allow_html=True)
        if st.button("🗑  Zerar semana atual", key="zerar"):
            st.session_state.cortes = [c for c in st.session_state.cortes if not e_da_semana_atual(c)]
            salvar_dados(st.session_state.cortes)
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ====== ABA 2: HISTÓRICO ======
with aba2:
    st.markdown("### HISTÓRICO COMPLETO")

    if not st.session_state.cortes:
        st.markdown('<div class="vazio">Nenhum corte registrado ainda.</div>', unsafe_allow_html=True)
    else:
        # Agrupar por semana
        semanas = {}
        for corte in st.session_state.cortes:
            try:
                d = datetime.strptime(corte["data_completa"], "%Y-%m-%d").date()
                seg = d - timedelta(days=d.weekday())
                chave = seg.isoformat()
                if chave not in semanas:
                    semanas[chave] = []
                semanas[chave].append(corte)
            except:
                pass

        for chave in sorted(semanas.keys(), reverse=True):
            grupo = semanas[chave]
            seg = date.fromisoformat(chave)
            dom = seg + timedelta(days=6)
            total_sem = sum(c["valor"] for c in grupo)
            label = "— SEMANA ATUAL" if seg == inicio_semana else ""

            st.markdown(f"""
            <div style="margin: 20px 0 8px; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-family:'Bebas Neue',sans-serif; font-size:16px; color:#666; letter-spacing:2px;">
                    📅 {seg.strftime('%d/%m')} – {dom.strftime('%d/%m/%Y')} {label}
                </span>
                <span style="font-family:'Bebas Neue',sans-serif; font-size:20px; color:#c8a96e;">
                    R$ {fmt_valor(total_sem)}
                </span>
            </div>
            """, unsafe_allow_html=True)

            for corte in reversed(grupo):
                st.markdown(f"""
                <div class="corte-item">
                    <div>
                        <div class="corte-nome">{corte['nome']}</div>
                        <div class="corte-hora">✂ {corte['dia']} às {corte['hora']}</div>
                    </div>
                    <div class="corte-valor">R$ {fmt_valor(corte['valor'])}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="zerar">', unsafe_allow_html=True)
        if st.button("🗑  Apagar TODO o histórico", key="apagar_tudo"):
            st.session_state.cortes = []
            salvar_dados([])
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
