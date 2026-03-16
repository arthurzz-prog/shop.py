import streamlit as st
import urllib.parse

st.set_page_config(page_title="Contas Fakes", layout="centered")

# ====== CSS SIMPLES ======
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Inter:wght@400;500&display=swap');

* {
    font-family: 'Sora', sans-serif;
}

body, .stApp {
    background-color: #0a0a0f;
    color: #f0f0f5;
}

.titulo {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(135deg, #00e5ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
    margin-bottom: 4px;
}

.subtitulo {
    text-align: center;
    font-size: 16px;
    color: #888;
    font-family: 'Inter', sans-serif;
}

.badge {
    display: inline-block;
    background: linear-gradient(135deg, #7b2ff7, #00e5ff);
    color: white;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 12px;
    border-radius: 50px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.card {
    background: linear-gradient(160deg, #13131f, #1a1a2e);
    border: 1px solid rgba(123, 47, 247, 0.25);
    padding: 28px 24px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 4px 30px rgba(0, 229, 255, 0.05), 0 1px 0 rgba(255,255,255,0.04) inset;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}

.card:hover {
    border-color: rgba(0, 229, 255, 0.45);
    box-shadow: 0 8px 40px rgba(0, 229, 255, 0.12);
}

.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #7b2ff7, #00e5ff);
    border-radius: 16px 16px 0 0;
}

.preco {
    font-size: 34px;
    font-weight: 800;
    background: linear-gradient(135deg, #00e5ff, #7b2ff7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 12px 0;
    line-height: 1;
}

.feature-item {
    font-size: 14px;
    color: #aaa;
    margin: 6px 0;
    font-family: 'Inter', sans-serif;
}

/* Botões do Streamlit */
.stButton > button {
    background: linear-gradient(135deg, #7b2ff7, #00e5ff) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.5px !important;
    padding: 10px 28px !important;
    width: 100% !important;
    transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease !important;
    box-shadow: 0 4px 20px rgba(123, 47, 247, 0.35) !important;
    cursor: pointer !important;
}

.stButton > button:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 8px 30px rgba(0, 229, 255, 0.4) !important;
    filter: brightness(1.1) !important;
}

.stButton > button:active {
    transform: translateY(0px) scale(0.98) !important;
    box-shadow: 0 2px 10px rgba(123, 47, 247, 0.3) !important;
    filter: brightness(0.95) !important;
}

/* Link buttons */
.stLinkButton > a {
    background: transparent !important;
    color: #00e5ff !important;
    border: 1px solid rgba(0, 229, 255, 0.4) !important;
    border-radius: 10px !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 10px 24px !important;
    width: 100% !important;
    transition: background 0.18s ease, border-color 0.18s ease, transform 0.18s ease !important;
}

.stLinkButton > a:hover {
    background: rgba(0, 229, 255, 0.08) !important;
    border-color: #00e5ff !important;
    transform: translateY(-2px) !important;
    color: white !important;
}

/* Input */
.stTextInput > div > div > input {
    background: #13131f !important;
    border: 1px solid rgba(123, 47, 247, 0.3) !important;
    border-radius: 10px !important;
    color: #f0f0f5 !important;
    font-family: 'Inter', sans-serif !important;
    padding: 10px 16px !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00e5ff !important;
    box-shadow: 0 0 0 3px rgba(0, 229, 255, 0.1) !important;
}

/* Info box */
.stAlert {
    background: rgba(123, 47, 247, 0.1) !important;
    border: 1px solid rgba(123, 47, 247, 0.3) !important;
    border-radius: 10px !important;
    color: #c9b3ff !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: #13131f !important;
    border: 1px solid rgba(123, 47, 247, 0.3) !important;
    border-radius: 10px !important;
    color: #f0f0f5 !important;
    font-family: 'Inter', sans-serif !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}

.stSelectbox > div > div:hover {
    border-color: rgba(0, 229, 255, 0.5) !important;
    box-shadow: 0 0 0 3px rgba(0, 229, 255, 0.08) !important;
}

.stSelectbox > div > div:focus-within {
    border-color: #00e5ff !important;
    box-shadow: 0 0 0 3px rgba(0, 229, 255, 0.1) !important;
}

.stSelectbox span, .stSelectbox svg {
    color: #c9b3ff !important;
    fill: #c9b3ff !important;
}

/* Dropdown list */
[data-baseweb="popover"] ul {
    background: #13131f !important;
    border: 1px solid rgba(123, 47, 247, 0.3) !important;
    border-radius: 10px !important;
    padding: 4px !important;
}

[data-baseweb="popover"] li {
    background: transparent !important;
    color: #f0f0f5 !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    transition: background 0.15s ease !important;
}

[data-baseweb="popover"] li:hover {
    background: rgba(123, 47, 247, 0.2) !important;
    color: #00e5ff !important;
}

[data-baseweb="popover"] li[aria-selected="true"] {
    background: rgba(0, 229, 255, 0.1) !important;
    color: #00e5ff !important;
}

/* Divider */
hr {
    border-color: rgba(123, 47, 247, 0.2) !important;
    margin: 24px 0 !important;
}

/* Headings */
h2, h3 {
    color: #f0f0f5 !important;
}

p, .stWrite {
    color: #bbb !important;
}

</style>
""", unsafe_allow_html=True)


# ====== TITULO ======

st.markdown('<p class="titulo">CONTAS FAKES</p>', unsafe_allow_html=True)

st.markdown(
'<p class="subtitulo">Jacarezin das contas fakes - o mais conhecido do hotel</p>',
unsafe_allow_html=True
)

st.divider()


# ====== SOBRE ======

st.markdown("### O que são contas fakes?")

st.write(
"""
Contas fakes são contas recém-criadas usadas para:

• reserva  
• depósitos  
• cartel  
"""
)

st.write(
"""
### O que vem nas contas?

• Sistema de trocas  
• Nick / Nome à sua escolha
"""
)

st.info("💰 Contas a partir de **R$3,00**")

st.divider()


# ====== PRODUTOS ======

st.markdown("## Comprar")

col1, col2 = st.columns(2)


with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Conta Fake Simples")
    st.write("✔ Trocas")
    st.write("✔ Nick/Nome a sua escolha")

    st.markdown('<p class="preco">R$ 3,00</p>', unsafe_allow_html=True)
    nome = st.selectbox(
            "Nome/Nick",
            ["Amora", "Arthur"]
        )
    st.session_state.nome = nome
    if st.button("Comprar", key="c1"):
        mensagem = f"Olá, quero comprar a Conta Fake Simples com o nick: {st.session_state.nome}"
        mensagem_codificada = urllib.parse.quote(mensagem)
        link = f"https://wa.me/5533998256653?text={mensagem_codificada}"
        st.link_button("Ir para WhatsApp", link)

    st.markdown('</div>', unsafe_allow_html=True)


with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Conta Fake Encomendada")
    st.write("✔ Trocas")
    st.write("✔ Nick/Nome aleatório")

    st.markdown('<p class="preco">R$ 2,50</p>', unsafe_allow_html=True)

    st.info("Disponível em quantidade")

    if st.button("Comprar", key="c2"):
        mensagem = "Olá, quero comprar a Conta Fake Encomendada"
        mensagem_codificada = urllib.parse.quote(mensagem)
        link = f"https://wa.me/5533998256653?text={mensagem_codificada}"
        st.link_button("Ir para WhatsApp", link)

    st.markdown('</div>', unsafe_allow_html=True)


st.divider()


# ====== DUVIDAS ======

st.markdown("## Dúvidas")

duvida = st.text_input("Digite sua dúvida")

mensagem = f"Olá, tenho uma dúvida: {duvida}"
mensagem_codificada = urllib.parse.quote(mensagem)

link_whatsapp = f"https://wa.me/5533998256653?text={mensagem_codificada}"

st.link_button("Tirar dúvida no WhatsApp 💬", link_whatsapp)
