import streamlit as st
from groq import Groq
from datetime import datetime, date
import json
import random

st.set_page_config(page_title="Conexão Magnética 2026", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    .stApp { background-color:#F8F9FA; font-family:'Inter',sans-serif; }
    [data-testid="stSidebar"] { display:none; }

    .stTextInput>div>div>input, .stTextArea>div>textarea,
    .stSelectbox>div>div>div, .stNumberInput>div>div>input {
        background-color:#FFFFFF !important; color:#1A1A2E !important;
        border:1px solid #CED4DA !important; font-family:'Inter',sans-serif !important;
    }

    .stButton>button {
        width:100%; border-radius:10px; height:3.2em;
        background:linear-gradient(135deg,#495057,#343A40) !important; color:white !important;
        font-weight:600; border:none; box-shadow:2px 2px 8px rgba(0,0,0,0.1);
        font-family:'Inter',sans-serif !important; transition:all 0.2s ease;
    }
    .stButton>button:hover { background:linear-gradient(135deg,#343A40,#212529) !important; transform:translateY(-1px); }
    .stApp .stButton>button, .stApp .stButton>button p,
    .stApp .stButton>button span, .stApp .stButton>button div { color:white !important; }

    .stApp h1, .stApp h2, .stApp h3 { color:#1A1A2E !important; font-family:'Inter',sans-serif !important; font-weight:700 !important; }

    .card { background:linear-gradient(135deg,#F1F3F5,#E9ECEF); padding:20px; border-radius:14px; border:1px solid #CED4DA; margin-bottom:14px; white-space:normal; word-wrap:break-word; }
    .stApp .card, .stApp .card p, .stApp .card span, .stApp .card div, .stApp .card strong, .stApp .card em { color:#1A1A2E !important; }

    .card-dark { background:linear-gradient(135deg,#E9ECEF,#DEE2E6); padding:20px; border-radius:14px; border:1px solid #ADB5BD; margin-bottom:14px; white-space:normal; word-wrap:break-word; }
    .stApp .card-dark, .stApp .card-dark p, .stApp .card-dark span, .stApp .card-dark div, .stApp .card-dark strong { color:#1A1A2E !important; }

    .card-green { background:linear-gradient(135deg,#F0FDF4,#DCFCE7); padding:20px; border-radius:14px; border:1px solid #86EFAC; margin-bottom:14px; white-space:normal; word-wrap:break-word; }
    .stApp .card-green, .stApp .card-green p, .stApp .card-green span, .stApp .card-green div { color:#14532D !important; }

    .card-blue { background:linear-gradient(135deg,#EFF6FF,#DBEAFE); padding:20px; border-radius:14px; border:1px solid #93C5FD; margin-bottom:14px; white-space:normal; word-wrap:break-word; }
    .stApp .card-blue, .stApp .card-blue p, .stApp .card-blue span, .stApp .card-blue div { color:#1E3A8A !important; }

    .card-red { background:linear-gradient(135deg,#FFF5F5,#FEE2E2); padding:20px; border-radius:14px; border:1px solid #FECACA; margin-bottom:14px; white-space:normal; word-wrap:break-word; }
    .stApp .card-red, .stApp .card-red p, .stApp .card-red span, .stApp .card-red div { color:#7F1D1D !important; }

    .card-yellow { background:linear-gradient(135deg,#FFFBEB,#FEF3C7); padding:18px; border-radius:12px; border:1px solid #FCD34D; margin-bottom:12px; white-space:normal; word-wrap:break-word; }
    .stApp .card-yellow, .stApp .card-yellow p, .stApp .card-yellow span, .stApp .card-yellow div { color:#78350F !important; }

    .stat-box { background:#FFFFFF; border-radius:12px; padding:16px; text-align:center; border:1px solid #CED4DA; }
    .stApp .stat-box div, .stApp .stat-box span, .stApp .stat-box p { color:#1A1A2E !important; }
    .stApp .stat-numero, .stat-numero { font-size:2em; font-weight:700; color:#495057 !important; }

    .hist-item { background:#FFFFFF; border-radius:10px; padding:12px 16px; margin-bottom:8px; border-left:4px solid #CED4DA; }
    .stApp .hist-item, .stApp .hist-item p, .stApp .hist-item span, .stApp .hist-item div, .stApp .hist-item small { color:#1A1A2E !important; }

    .badge { background:#495057; color:white !important; padding:4px 12px; border-radius:20px; font-size:0.78em; font-weight:600; display:inline-block; margin:2px; }
    .badge-verde { background:#059669; color:white !important; padding:4px 12px; border-radius:20px; font-size:0.78em; font-weight:600; display:inline-block; margin:2px; }
    .badge-amarelo { background:#B45309; color:white !important; padding:4px 12px; border-radius:20px; font-size:0.78em; font-weight:600; display:inline-block; margin:2px; }
    .badge-azul { background:#1D4ED8; color:white !important; padding:4px 12px; border-radius:20px; font-size:0.78em; font-weight:600; display:inline-block; margin:2px; }
    .badge-roxo { background:#6D28D9; color:white !important; padding:4px 12px; border-radius:20px; font-size:0.78em; font-weight:600; display:inline-block; margin:2px; }

    .divider { border:none; height:1px; background:linear-gradient(to right,transparent,#CED4DA,transparent); margin:18px 0; }

    .chat-user { background:#FFFFFF; border:1px solid #CED4DA; border-radius:12px 12px 4px 12px; padding:12px 16px; margin:8px 0; }
    .stApp .chat-user, .stApp .chat-user p, .stApp .chat-user span, .stApp .chat-user div { color:#1A1A2E !important; }

    .chat-persona { background:#F8F9FA; border:1px solid #CED4DA; border-radius:4px 12px 12px 12px; padding:12px 16px; margin:8px 0; }
    .stApp .chat-persona, .stApp .chat-persona p, .stApp .chat-persona span, .stApp .chat-persona div { color:#1A1A2E !important; }

    .questao-box { background:#FFFFFF; border:2px solid #CED4DA; border-radius:12px; padding:18px; margin-bottom:14px; }
    .stApp .questao-box, .stApp .questao-box p, .stApp .questao-box span, .stApp .questao-box div { color:#1A1A2E !important; }

    .avaliacao-box { background:#FFFFFF; border:2px solid #CED4DA; border-radius:14px; padding:18px; margin-bottom:12px; }
    .stApp .avaliacao-box, .stApp .avaliacao-box p, .stApp .avaliacao-box span, .stApp .avaliacao-box div { color:#1A1A2E !important; }

    .meta-box { background:#FFFFFF; border:2px solid #CED4DA; border-radius:12px; padding:16px; text-align:center; margin:10px 0; }
    .stApp .meta-box, .stApp .meta-box div, .stApp .meta-box span { color:#1A1A2E !important; }
    .stApp .meta-numero { font-size:2em; font-weight:700; color:#495057 !important; }

    .chat-scroll-container { max-height:40vh; overflow-y:auto; display:flex; flex-direction:column; scroll-behavior:smooth; padding-bottom:4px; }
    .chat-scroll-container > * { flex-shrink:0; }
    

    </style>
""", unsafe_allow_html=True)

# ─── CACHE ───
@st.cache_resource
def get_cache():
    return {"perfis": {}}
_cache = get_cache()

# ─── FAIXAS DA ARTE DA LÁBIA ───
FAIXAS = [
    (1, "⚪ Faixa Branca",  "🌱 O Invisível",    "Recebe ajuda direta. Personagem facilitador."),
    (2, "🟡 Faixa Amarela", "🟢 O Quebra-Gelo",  "Aprende a captar ganchos. Ajuda reduzida."),
    (3, "🟠 Faixa Laranja", "🟡 O Interessante", "Lida com silêncio e improvisação. Sem ajuda direta."),
    (4, "🟢 Faixa Verde",   "🟠 O Inabalável",   "Provocações e pressão social."),
    (5, "🔵 Faixa Azul",    "🔴 O Desafiador",   "Respostas frias e pouca reciprocidade."),
    (6, "🟤 Faixa Marrom",  "⚫ O Sedutor",       "Oscilação e imprevisibilidade."),
    (7, "⚫ Faixa Preta",   "👑 Don Juan",        "Conversa livre. Zero rede de proteção."),
]

CONQUISTAS_DEF = [
    ("primeira_analise",   "🔍 Primeira Análise",        "Realizou sua primeira análise de conversa"),
    ("primeiro_treino",    "🎭 Primeiro Treino",          "Completou o primeiro roleplay"),
    ("cinco_analises",     "📊 5 Conversas",              "5 conversas analisadas"),
    ("dez_mensagens",      "✨ 10 Mensagens",             "10 mensagens aprimoradas"),
    ("primeira_carta",     "🃏 Primeira Carta",           "Usou a Carta na Manga pela primeira vez"),
    ("cinco_cartas",       "🎴 5 Cartas",                 "5 Cartas na Manga utilizadas"),
    ("plano_7dias",        "🗓️ Plano 7 Dias",            "Concluiu o plano de 7 dias"),
    ("primeiro_passo",     "🌱 Primeiro Passo",           "Concluiu a primeira conversa na Arte da Lábia"),
    ("cacador_ganchos",    "🧩 Caçador de Ganchos",      "Aproveitou 10 ganchos em conversas"),
    ("resposta_relampago", "⚡ Resposta Relâmpago",       "Respondeu 10 situações dentro do tempo"),
    ("sem_roteiro",        "🧠 Sem Roteiro",              "Completou uma conversa sem ajuda"),
    ("inabalavel",         "🛡️ Inabalável",              "Superou 5 provocações com naturalidade"),
    ("resgatador",         "🔥 Resgatador",               "Recuperou 5 conversas esfriando"),
    ("camaleao",           "🦎 Camaleão",                 "Adaptou-se a 10 personalidades diferentes"),
    ("don_juan",           "👑 Don Juan",                 "Concluiu o Nível 7 — Don Juan"),
]

CHAVES_SALVAR = [
    'usuario', 'historico', 'biblioteca', 'resumo_semanal',
    'plano_conquista', 'plano_pessoa',
    'conversas_analisadas', 'mensagens_aprimoradas', 'analises_realizadas',
    'cartas_usadas', 'treinos_realizados', 'favoritos_total',
    'clareza', 'naturalidade', 'reciprocidade', 'confianca', 'escuta',
    'conquistas', 'faixa_atual', 'historico_personagens',
    'labia_nivel', 'labia_chat', 'labia_personagem', 'labia_falha_anterior',
    'objetivos_usuario',
]

def gerar_json():
    dados = {k: st.session_state.get(k) for k in CHAVES_SALVAR}
    dados['salvo_em'] = datetime.now().strftime('%d/%m/%Y %H:%M')
    return json.dumps(dados, ensure_ascii=False, indent=2, default=str)

def carregar_json(dados):
    for k in CHAVES_SALVAR:
        if k in dados:
            st.session_state[k] = dados[k]

def salvar_cache(u):
    _cache["perfis"][u] = {k: st.session_state.get(k) for k in CHAVES_SALVAR}

def perfis_salvos():
    return list(_cache["perfis"].keys())

def carregar_cache(u):
    return _cache["perfis"].get(u)

def salvar_historico(tipo, tema, conteudo):
    st.session_state.historico.append({
        'data': datetime.now().strftime('%d/%m %H:%M'),
        'tipo': tipo, 'tema': tema, 'conteudo': conteudo,
    })

def verificar_conquistas():
    c = st.session_state.get('conquistas', [])
    novas = []
    checks = [
        ("primeira_analise",   st.session_state.analises_realizadas >= 1),
        ("primeiro_treino",    st.session_state.treinos_realizados >= 1),
        ("cinco_analises",     st.session_state.conversas_analisadas >= 5),
        ("dez_mensagens",      st.session_state.mensagens_aprimoradas >= 10),
        ("primeira_carta",     st.session_state.cartas_usadas >= 1),
        ("cinco_cartas",       st.session_state.cartas_usadas >= 5),
    ]
    for chave, cond in checks:
        if cond and chave not in c:
            c.append(chave); novas.append(chave)
    st.session_state['conquistas'] = c
    return novas

defaults = {
    'etapa': 'Login', 'usuario': '', 'api_key': '', 'pagina': 'Home',
    'historico': [], 'biblioteca': [], 'resumo_semanal': '',
    'plano_conquista': '', 'plano_pessoa': '',
    'conversas_analisadas': 0, 'mensagens_aprimoradas': 0,
    'analises_realizadas': 0, 'cartas_usadas': 0,
    'treinos_realizados': 0, 'favoritos_total': 0,
    'clareza': 0, 'naturalidade': 0, 'reciprocidade': 0,
    'confianca': 0, 'escuta': 0,
    'conquistas': [], 'faixa_atual': 1,
    'historico_personagens': [],
    'labia_nivel': 1, 'labia_chat': [], 'labia_personagem': None,
    'labia_falha_anterior': None, 'objetivos_usuario': [],
    'labia_inicio': 0, 'labia_duracao': 180, 'labia_encerrado': False,
    # Mestre da Lábia
    'lj_fase': 1, 'lj_personagem_sel': 'Rafaela',
    'lj_ativo': False, 'lj_chat': [], 'lj_conexo': 100,
    'lj_atributos': {'interesse':50,'atracao':50,'conexao':50,'confianca':50,'naturalidade':50,'curiosidade':50,'tensao':20},
    'lj_inicio': 0, 'lj_duracao': 300,
    'lj_missao': '', 'lj_missao_cumprida': False,
    'lj_aval': None, 'lj_arranques': [],
    'lj_historico_cenarios': [], 'lj_historico_aberturas': [],
    'lj_ts_persona': 0, 'lj_ts_usuario': 0, 'lj_silencio_total': 0,
    'lj_combo': 0,
    'lj_fases_concluidas': 0,
    'lj_titulo': 'Paquerador',
    'lj_personagens_desbloqueadas': ['Rafaela'],
    'lj_perfil_estilo': None,
    'lj_historico_partidas': [],
    'lj_desbloqueado': False,
    'lj_ficha': {}, 'lj_ficha_resumo': '',
    'lj_nome_persona': '', 'lj_dados_persona': {},
    'lj_cenario': '', 'lj_cenario_label': '',

    'lj_fases_ok': '',
    'lj_hist_partidas': [],
    'lj_personagens_ok': None,
    'ml_aberturas_usadas': None,
    'ml_cenario': '',
    'ml_character': None,
    'ml_connexometer': None,
    'ml_current_rank': None,
    'ml_estagio': None,
    'ml_historico': [],
    'ml_interaction_scores': None,
    'ml_last_result': None,
    'ml_messages': None,
    'ml_phase_coachings': None,
    'ml_phase_index': None,
    'ml_phase_message_start': None,
    'ml_phase_results': None,
    'ml_phase_start': None,
    'ml_response_since': None,
    'roleplay_cenario': '',
    'roleplay_system': None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ─── IA ───
def conexa_ia(prompt, system_extra=""):
    try:
        client = Groq(api_key=st.session_state.api_key)
        system = (
            "Você é o Conexão Magnética 2026 — sistema de inteligência para comunicação e conexões humanas. "
            "Você ajuda pessoas a entender conversas, melhorar mensagens e desenvolver habilidades sociais. "
            "NUNCA afirme intenções ou sentimentos que não podem ser conhecidos. "
            "Trabalhe apenas com padrões observáveis. "
            "Seja direto, prático e baseado no contexto fornecido. "
            "Português do Brasil. " + system_extra
        )
        resp = client.chat.completions.create(
            messages=[{"role":"system","content":system},{"role":"user","content":prompt}],
            model="openai/gpt-oss-120b",
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"⚠️ Erro na API: {e}"

def barra_salvar():
    salvar_cache(st.session_state.usuario)
    nome_u = st.session_state.usuario.lower().replace(' ','_') or 'sessao'
    faixa_info = FAIXAS[min(st.session_state.faixa_atual-1, 6)]
    col_i, col_b = st.columns([4,2])
    with col_i:
        st.markdown(
            f"<div style='background:#FFF0F5;border:1px solid #FFB6C1;border-radius:10px;"
            f"padding:10px 14px;font-size:0.84em;color:#1A1A2E;line-height:1.6;'>"
            f"💾 <strong>Salve seus dados antes de sair.</strong><br>"
            f"<span style='color:#C2185B;font-size:0.88em;'>"
            f"{faixa_info[0]} {faixa_info[2]} · "
            f"{st.session_state.conversas_analisadas} análises · "
            f"{st.session_state.cartas_usadas} cartas usadas"
            f"</span></div>", unsafe_allow_html=True)
    with col_b:
        st.download_button("💾 SALVAR DADOS (.json)", data=gerar_json(),
            file_name=f"conexa_{nome_u}.json", mime="application/json", use_container_width=True, key="dl_conexa_1")
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("""<style>
    .dica-nav{font-size:0.72em;color:#94A3B8;text-align:center;padding:2px 0 6px;}
    .dica-mobile{display:none;}
    .dica-desktop{display:block;}
    @media(max-width:768px){.dica-mobile{display:block;}.dica-desktop{display:none;}}
    </style>
    <div class='dica-nav dica-mobile'>👆 Deslize o dedo para navegar entre as abas</div>
    <div class='dica-nav dica-desktop'>📋 Clique no ícone acima para abrir o menu completo</div>
    """, unsafe_allow_html=True)


# ============================================================
# LOGIN
# ============================================================
# ── CONSTANTES GLOBAIS ──
FASES_DEF_G = [
    # (num, nome,             mins, titulo,          min_conexao, min_natural, min_interesse)
    (1, "ATRACAO",           5,  "Paquerador",      70, 60, 65),
    (2, "CONEXAO EMOCIONAL", 7,  "Galanteador",     75, 70, 65),
    (3, "SEDUCAO",           10, "Mestre da Labia", 80, 75, 70),
]
# Índices: [0]=num [1]=nome [2]=mins [3]=titulo [4]=min_conexao [5]=min_natural [6]=min_interesse

def estado_conexo_g(val):
    if val >= 80: return "CONEXAO FORTE", "#DC2626"
    if val >= 60: return "BOA QUIMICA", "#F59E0B"
    if val >= 40: return "NEUTRO", "#64748B"
    if val >= 20: return "INTERESSE CAINDO", "#EA580C"
    if val >= 1:  return "ULTIMA CHANCE", "#7F1D1D"
    return "ELIMINADA", "#000000"

PERSONAGENS = {
    "Rafaela": {
        "emoji": "😊", "dificuldade": 2, "estrelas": "⭐⭐",
        "desc": "Simpática, inteligente, bem-humorada. Conversa naturalmente mas não demonstra interesse imediatamente.",
        "personalidade": "simpatica, inteligente, bem-humorada, curiosa, fala de forma leve e natural",
        "humor": 80, "receptividade": 70, "provocacao": 30, "exigencia": 40, "bloqueada": False,
    },
    "Camila": {
        "emoji": "😏", "dificuldade": 4, "estrelas": "⭐⭐⭐⭐",
        "desc": "Segura, provocadora, responde com ironia e testa a confiança do usuário.",
        "personalidade": "segura, ironica, provocadora, testa confianca, nao facilita",
        "humor": 70, "receptividade": 45, "provocacao": 80, "exigencia": 70, "bloqueada": True,
    },
    "Helena": {
        "emoji": "🧐", "dificuldade": 5, "estrelas": "⭐⭐⭐⭐⭐",
        "desc": "Sofisticada, seletiva, difícil de impressionar. Exige conversa mais inteligente.",
        "personalidade": "sofisticada, seletiva, intelectual, dificil de impressionar, exige profundidade",
        "humor": 55, "receptividade": 30, "provocacao": 60, "exigencia": 90, "bloqueada": True,
    },
}

MISSOES_POR_FASE = {
    1: ["Fazer ela fazer uma pergunta espontânea sobre você","Conseguir que ela demonstre curiosidade","Criar um momento de humor","Fazer ela contar algo pessoal"],
    2: ["Fazer ela lembrar algo que você disse antes","Conseguir que ela compartilhe um sonho","Criar um momento de empatia genuína","Fazer ela admitir algo que normalmente não diria"],
    3: ["Criar um momento de flerte natural","Fazer ela brincar com você","Criar uma brincadeira interna entre vocês","Fazer ela perguntar algo pessoal espontaneamente"],
}

CENARIOS_TODOS = [
    "cafeteria","parque","livraria","fila de evento","shopping","feira",
    "exposicao de arte","aeroporto","praca","academia","show de musica",
    "festa de aniversario","mercado","galeria","coworking","food court",
    "banca de jornal","pet shop","sebo de livros","farmacia","bancada de bar",
    "fila de banco","salao de beleza","loja de discos","jardim botanico",
    "estacao de metro","calcadao","praia","aluguel de bicicletas","museu"
]

PERFIS_ESTILO = {
    "O Confiante":     "Fala com segurança, mas às vezes avança rápido demais.",
    "O Estrategista":  "Faz boas perguntas e lê bem os sinais.",
    "O Divertido":     "Usa humor para criar conexão.",
    "O Conquistador":  "Cria conexão emocional rapidamente.",
    "O Reservado":     "Tem boas respostas, mas demonstra pouco interesse.",
}

def carregar_json_sessao(dados):
    _bloq = {'api_key','etapa','nome_login','chave_login','upload_login','btn_entrar_login'}
    _pref = (
        'btn_','sel_','ul_','dl_','cad_','_sub','_sm','_tab','_bsc',
        'ativo_','rem_','sel_pet_','ev_','prof_','hig_','prev_',
        'vac_','sint_','comp_','trad_','subs_','amb_','viag_','chat_',
        'duvida_','emerg_','peso_','data_','obs_','tipo_','vet_','desc_',
        'local_','prox_','alim','sit_emerg_','tc_','oraf','siau','agmag',
        'lv','mv','pt','pi','sh','wc','rv','rp','rc',
    )
    import re as _re
    for k, v in dados.items():
        if k in _bloq: continue
        if any(k.startswith(p) for p in _pref): continue
        if _re.match(r'.+_\d+$', k): continue
        st.session_state[k] = v

if 'lj_arranques' not in st.session_state: st.session_state['lj_arranques'] = []
if 'lj_cenario' not in st.session_state: st.session_state['lj_cenario'] = None
if 'lj_dados_persona' not in st.session_state: st.session_state['lj_dados_persona'] = {}
if 'lj_ficha' not in st.session_state: st.session_state['lj_ficha'] = {}
if 'lj_hist_partidas' not in st.session_state: st.session_state['lj_hist_partidas'] = []
if 'lj_inicio' not in st.session_state: st.session_state['lj_inicio'] = None

if 'lj_missao' not in st.session_state: st.session_state['lj_missao'] = ''
if 'lj_nome_persona' not in st.session_state: st.session_state['lj_nome_persona'] = ''
if 'lj_personagens_ok' not in st.session_state: st.session_state['lj_personagens_ok'] = []

if st.session_state.etapa == "Login":
    st.markdown("# 🧠 Conexão Magnética 2026")
    st.markdown("<div class=\'card\'><b>🔒 ACESSO RESTRITO A CLIENTES DO QUIZ COM PRÊMIOS</b><br>🔗 <a href='https://quizcompremios.com.br' target='_blank' style='color:#4F46E5;font-weight:700;text-decoration:underline;'>quizcompremios.com.br</a></div>", unsafe_allow_html=True)
    st.info("💻 **Dica:** Pela complexidade dos agentes, no computador a experiência é mais agradável.")
    with st.container():
        nome  = st.text_input("Seu Nome:", key="nome_login")
        chave = st.text_input("🔑 Sua Chave API da Groq:", type="password", key="chave_login")
        arq_j = st.file_uploader("📂 Carregar dados salvos (.json):", type=["json"], key="upload_login")
        dados_login = json.load(arq_j) if arq_j else None
        if st.button("✨ ENTRAR", key="btn_entrar_login"):
            if len(nome.strip()) < 2:
                st.warning("Digite um nome com pelo menos 2 caracteres.")
            elif chave.strip():
                st.session_state.usuario = nome.strip()
                st.session_state.api_key = chave
                if dados_login: carregar_json_sessao(dados_login)
                st.session_state.etapa = "App"
                st.rerun()
            else:
                st.warning("Preencha nome e chave API.")

elif st.session_state.etapa == "App":
    faixa = FAIXAS[min(st.session_state.faixa_atual-1, 6)]
    em_partida = st.session_state.get('pagina') == 'Dialogo'

    if not em_partida:
        pass
        # ── NAVBAR ──
        # NAVBAR
    _nav_pgs = ['Home', 'Rapida', 'Carta', 'Turbinar', 'Analisar', 'Roleplay', 'Labia', 'Biblioteca', 'Perfil', 'Comparar', 'Plano', 'Progresso', 'Resumo', 'Conquistas']
    _nav_ics = ['🏠', '⚡', '🃏', '💬', '🧠', '🎭', '💋', '📚', '📸', '⚔️', '🗓️', '📈', '📋', '🏆']
    _nav_lbs = ['Dashboard', 'Resposta Rápida', 'Carta na Manga', 'Turbinar Mensagem', 'Raio-X da Conversa', 'Simulador de Conversa', '💋 Mestre da Lábia ⭐', 'Biblioteca Inteligente', 'Leitor de Perfil', 'Comparar Conversas', 'Plano 7 Dias', 'Minha Evolução', 'Relatório Semanal', 'Conquistas']
    _nav_idx = _nav_pgs.index(st.session_state.pagina) if st.session_state.pagina in _nav_pgs else 0

    # ── NAVEGAÇÃO: selectbox limpo ──
    _opcoes_nav = [f"{ic} {lb}" for ic, lb in zip(_nav_ics, _nav_lbs)]
    _sel_nav = st.selectbox("📍 Navegar para:", _opcoes_nav,
        index=_nav_idx, key="nav_select", label_visibility="collapsed")
    _pg_escolhida = _nav_pgs[_opcoes_nav.index(_sel_nav)]
    if _pg_escolhida != st.session_state.pagina:
        st.session_state.pagina = _pg_escolhida; st.rerun()

    st.markdown(f"<div style='text-align:center;font-weight:700;font-size:1.1em;color:#1A1A2E;padding:4px 0;'>{_nav_ics[_nav_idx]} {_nav_lbs[_nav_idx]}</div>", unsafe_allow_html=True)
    st.markdown("<hr class='divider'>", unsafe_allow_html=True)


    if st.session_state.pagina == "Dialogo":
        import time as _t, json as _j, re as _r

        # Esconde TUDO do Streamlit — só o diálogo
        st.markdown("""
        <style>
        header[data-testid="stHeader"]{display:none!important;}
        #MainMenu{display:none!important;}
        [data-testid="stToolbar"]{display:none!important;}
        footer{display:none!important;}
        .block-container{padding:0.5rem 1rem!important;}
        [data-testid="stSidebar"]{display:none!important;}

        .chat-wrap{
            display:flex;flex-direction:column;
            height:calc(100vh - 180px);
            min-height:300px;
        }
        .chat-msgs{
            flex:1;overflow-y:auto;
            padding:10px 4px;
            display:flex;flex-direction:column;
            scroll-behavior:smooth;
        }
        .msg-p{
            background:#FFF0F5;border:1px solid #FFB6C1;
            border-radius:4px 16px 16px 16px;
            padding:10px 14px;margin:6px 0;
            font-size:0.95em;color:#1A1A2E;
            max-width:80%;align-self:flex-start;
        }
        .msg-u{
            background:#F0F4FF;border:1px solid #C7D2FE;
            border-radius:16px 16px 4px 16px;
            padding:10px 14px;margin:6px 0;
            font-size:0.95em;color:#1A1A2E;
            max-width:80%;align-self:flex-end;
        }
        .msg-arr{
            font-size:0.72em;color:#22C55E;font-weight:700;
            text-align:right;margin-bottom:2px;
        }
        .bar-wrap{
            background:#fff;border:2px solid #22C55E;
            border-radius:10px;padding:6px 12px;
            display:flex;align-items:center;gap:8px;
            margin-bottom:6px;
        }
        .input-wrap{
            display:flex;gap:8px;align-items:center;
            padding:6px 0;
        }
        </style>""", unsafe_allow_html=True)

        # Redireciona se não há partida
        if not st.session_state.get('lj_ativo') or not st.session_state.get('lj_nome_persona') or st.session_state.get('lj_inicio',0)==0:
            st.session_state.pagina="Labia"; st.rerun()

        chat     = st.session_state.lj_chat
        conexo   = st.session_state.lj_conexo
        fase_n   = st.session_state.lj_fase
        nome_p   = st.session_state.lj_nome_persona
        dados_p  = st.session_state.lj_dados_persona
        cenario  = st.session_state.lj_cenario
        ficha    = st.session_state.lj_ficha
        atribs   = st.session_state.lj_atributos

        FASES_D  = {1:(5,70,60,65,"🥉 Paquerador"),2:(7,75,70,65,"🥈 Galanteador"),3:(10,80,75,70,"👑 Mestre da Lábia")}
        fi       = FASES_D[fase_n]
        duracao  = fi[0]*60
        inicio   = st.session_state.lj_inicio
        decorrido= _t.time() - inicio
        restante = max(0, duracao - decorrido)
        mins_r   = int(restante//60); segs_r = int(restante%60)
        pct_t    = max(0.0, 1-decorrido/duracao)
        cor_c    = "#22C55E" if conexo>70 else ("#84CC16" if conexo>50 else ("#F59E0B" if conexo>30 else ("#EF4444" if conexo>10 else "#7F1D1D")))
        pulso    = "animation:pulso 0.8s ease-in-out infinite;" if conexo<=20 else ""
        cor_t    = "#22C55E" if pct_t>0.5 else ("#F59E0B" if pct_t>0.2 else "#EF4444")

        def estado(v):
            if v>=80: return "🔥 CONEXÃO FORTE"
            if v>=60: return "❤️ BOA QUÍMICA"
            if v>=40: return "😐 NEUTRO"
            if v>=20: return "⚠️ CAINDO"
            return "🚨 ÚLTIMA CHANCE"

        # ── CENÁRIO ──
        st.markdown(
            f"<div style='background:#FFF0F5;border:1px solid #FFB6C1;border-radius:8px;"
            f"padding:4px 14px;margin-bottom:4px;font-size:0.82em;color:#5C0F30;'>"
            f"📍 <b>{cenario.capitalize()}</b> — Você acaba de conhecer alguém.</div>",
            unsafe_allow_html=True)

        # ── CONEXÔMETRO + TIMER (numa linha) ──
        st.markdown(
            f"<style>@keyframes pulso{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}</style>"
            f"<div class='bar-wrap'>"
            f"<span style='font-size:0.7em;color:#64748B;font-weight:600;white-space:nowrap;'>❤️ CONEXÔMETRO</span>"
            f"<div style='flex:1;background:#F1F5F9;border-radius:999px;height:10px;overflow:hidden;'>"
            f"<div style='height:100%;border-radius:999px;background:{cor_c};width:{conexo}%;transition:width 0.4s;{pulso}'></div></div>"
            f"<span style='font-size:0.9em;font-weight:700;color:{cor_c};white-space:nowrap;'>{conexo} {estado(conexo)}</span>"
            f"<span style='border-left:1px solid #E2E8F0;padding-left:10px;font-size:0.7em;color:#94A3B8;'>⏱️</span>"
            f"<span style='font-size:1em;font-weight:700;color:{cor_t};'>{mins_r:02d}:{segs_r:02d}</span>"
            f"</div>", unsafe_allow_html=True)

        # ── ALERTAS ──
        if 0 < conexo <= 20:
            st.markdown("<div style='color:#B91C1C;font-weight:700;font-size:0.85em;text-align:center;'>🚨 ÚLTIMA CHANCE</div>", unsafe_allow_html=True)
        if st.session_state.lj_missao_cumprida:
            st.markdown("<div style='color:#22C55E;font-weight:700;font-size:0.8em;text-align:center;'>🎯 MISSÃO CUMPRIDA!</div>", unsafe_allow_html=True)
        # Alerta de silêncio
        if ts_p > 0 and ts_u < ts_p:
            inat_alerta = _t.time() - ts_p
            if inat_alerta > 25:
                emoji_alerta = "🔴" if inat_alerta > 45 else "🟡"
                st.markdown(f"<div style='color:#B45309;font-weight:700;font-size:0.82em;text-align:center;'>{emoji_alerta} {'RESPONDA AGORA — conexômetro caindo!' if inat_alerta>45 else 'Silêncio detectado — responda logo!'}</div>", unsafe_allow_html=True)

        # ── CHAT (ocupa toda a altura disponível) ──
        msgs_html = ""
        for msg in chat:
            if msg['role']=='user':
                msgs_html += f"<div class='msg-u'><b style='color:#7C3AED;'>Você:</b> {msg['content']}</div>"
            else:
                arr = msg.get('arranque','')
                if arr: msgs_html += f"<div class='msg-arr'>{arr}</div>"
                msgs_html += f"<div class='msg-p'><b style='color:#C2185B;'>😊 {nome_p}:</b> {msg['content']}</div>"

        turno_u = sum(1 for m in chat if m['role']=='user')
        if fase_n==1 and turno_u==0:
            msgs_html += f"<div style='font-size:0.75em;color:#94A3B8;border-left:2px solid #FFB6C1;padding:4px 10px;margin:4px 0;'>💡 Comente o que {nome_p} disse.</div>"

        st.markdown(
            f"<div class='chat-msgs' id='chat-c'>{msgs_html}<div id='cb'></div></div>"
            f"<script>setTimeout(()=>{{var c=document.getElementById('chat-c');if(c)c.scrollTop=c.scrollHeight;}},80);</script>",
            unsafe_allow_html=True)

        # ── INATIVIDADE — 25s calado = -25% fixo ──
        ts_p = st.session_state.lj_ts_persona; ts_u = st.session_state.lj_ts_usuario
        if ts_p > 0 and ts_u < ts_p:
            inat = _t.time() - ts_p
            # A cada 25s completos de silêncio, aplica -25%
            blocos = int(inat // 25)
            if blocos > st.session_state.get('lj_blocos_silencio', 0):
                st.session_state['lj_blocos_silencio'] = blocos
                novo_c = max(0, conexo - 25)
                st.session_state.lj_conexo = novo_c
                if novo_c!=conexo: st.session_state.lj_conexo=novo_c

        # ── FIM DE PARTIDA ──
        if restante<=0 or conexo<=0:
            hist_txt = "\n".join(f"{'Você' if m['role']=='user' else nome_p}: {m['content']}" for m in chat)
            n_arr = len(st.session_state.lj_arranques)
            mc,mn,mi,_,titulo_fase = fi[1],fi[2],fi[3],fi[0],fi[4]
            passou = (conexo>=mc and atribs.get('naturalidade',0)>=mn and atribs.get('interesse',0)>=mi and turno_u>=4 and restante<=0)
            prompt_av = (
                f"Avalie conversa — Fase {fase_n}.\n"
                f"Personagem:{nome_p}. Conexao:{conexo}. Arranques:{n_arr}. Turnos:{turno_u}.\n"
                f"Missao:'{st.session_state.lj_missao}' — cumprida:{st.session_state.lj_missao_cumprida}\n"
                f"Conversa:\n{hist_txt}\n\n"
                f"JSON sem markdown:\n"
                + '{"aprovado":false,"ponto_forte":"1 frase","melhorar":"1 frase","perfil":"O Confiante","missao_ok":false}'
            )
            with st.spinner("Avaliando..."):
                try:
                    from groq import Groq as _Groq
                    _cl = _Groq(api_key=st.session_state.api_key)
                    _r2 = _cl.chat.completions.create(messages=[{"role":"user","content":prompt_av}],model="openai/gpt-oss-120b",max_tokens=200)
                    jm = _r.search(r'\{.*\}',_r2.choices[0].message.content,_r.DOTALL)
                    av_d = _j.loads(jm.group(0)) if jm else {}
                except: av_d = {}
            aprovado = passou and av_d.get('aprovado',passou)
            if aprovado:
                st.session_state.lj_fases_ok = max(st.session_state.lj_fases_ok, fase_n)
                nomes_pers = ["Rafaela","Camila","Helena"]
                for i2 in range(min(fase_n,3)):
                    if nomes_pers[i2] not in st.session_state.lj_personagens_ok:
                        st.session_state.lj_personagens_ok.append(nomes_pers[i2])
                TITULOS = {1:"🥉 Paquerador",2:"🥈 Galanteador",3:"👑 Mestre da Lábia"}
                st.session_state.lj_titulo = TITULOS[fase_n]
            st.session_state.lj_aval = {
                'aprovado':aprovado,
                'titulo': f"FASE {fase_n} CONCLUÍDA! 🎉" if aprovado else "CONEXÃO PERDIDA 💥",
                'conexo_final':conexo,'n_arranques':n_arr,
                'missao_cumprida':av_d.get('missao_ok',False),
                'ponto_forte':av_d.get('ponto_forte','—'),
                'melhorar':av_d.get('melhorar','—'),
            }
            st.session_state.lj_hist_partidas.append({
                'fase':fase_n,'personagem':nome_p,'conexo_final':conexo,
                'aprovado':aprovado,'data':datetime.now().strftime('%d/%m %H:%M'),
                'ficha_resumo':st.session_state.get('lj_ficha_resumo',''),
            })
            st.session_state.lj_ativo=False; st.session_state.lj_chat=[]
            st.session_state.pagina="Labia"; st.rerun()

        else:
            # ── INPUT + BOTÕES ──
            msg_in = st.text_input("",key=f"lj_in_{len(chat)}",
                placeholder="O que você diz?",label_visibility="collapsed")
            col_e, col_s = st.columns([4,1])
            with col_e:
                if st.button("📤 ENVIAR",key="lj_env",use_container_width=True):
                    if msg_in.strip():
                        st.session_state.lj_ts_usuario = _t.time()
                        st.session_state['lj_blocos_silencio'] = 0  # reset silêncio
                        f2 = ficha
                        aviso_pes = ""
                        kws = ['aniversario','cidade','mora','trabalha','profissao','musica','hobby','medo','sonho']
                        if any(k in msg_in.lower() for k in kws):
                            aviso_pes = f"\nAVISO: Aniversario={f2.get('aniversario','?')}, Cidade={f2.get('cidade','?')}, Profissao={f2.get('profissao','?')}."
                        ultima = chat[-1]['content'] if chat else ''
                        sys_p = (
                            f"Você é {nome_p}, {f2.get('profissao','')}, {f2.get('cidade','')}.\n"
                            f"Personalidade: {dados_p.get('personalidade','')}.\n"
                            f"Cenário: {cenario}. Hoje: {f2.get('hoje','')}.\n"
                            f"Você disse '{ultima}', pessoa respondeu '{msg_in}'.\n"
                            f"Reaja a ISSO. Máximo 10 palavras. Estilo WhatsApp.\n"
                            f"Zero filosofia. Só reaja. NUNCA revele que é IA."
                            + aviso_pes
                        )
                        hist = [{"role":m["role"],"content":m["content"]} for m in chat[-6:]]
                        with st.spinner(""):
                            try:
                                from groq import Groq as _Groq2
                                _cl2 = _Groq2(api_key=st.session_state.api_key)
                                msgs_l = [{"role":"system","content":sys_p.encode("utf-8","ignore").decode("utf-8")}]+hist+[{"role":"user","content":msg_in}]
                                resp_l = _cl2.chat.completions.create(messages=msgs_l,model="openai/gpt-oss-120b",max_tokens=40)
                                resp_bruto = resp_l.choices[0].message.content.strip().split('\n')[0]
                                mc2 = _r.search(r'[.!?]',resp_bruto)
                                resp_txt = resp_bruto[:mc2.end()].strip() if mc2 else ' '.join(resp_bruto.split()[:10])
                                if not resp_txt.strip():
                                    resp_txt = "Interessante..."
                            except Exception as e:
                                resp_txt = "Hm, é mesmo?"
                        CRIT = {
                            1:"Fase 1: avalie curiosidade,humor,originalidade. Generoso. delta -15 a +20",
                            2:"Fase 2: avalie escuta,empatia,profundidade. Moderado. delta -15 a +18",
                            3:"Fase 3: avalie timing,tensao,confianca. Exigente. delta -15 a +20",
                        }
                        prompt_ev = (
                            f"Avaliador. Fase {fase_n}.\n"
                            f"Ela:'{ultima}' Usuario:'{msg_in}'\n"
                            f"{CRIT.get(fase_n,CRIT[1])}\n"
                            f"Missao:'{st.session_state.lj_missao}'\n"
                            f"JSON: {{\"delta\":0,\"interesse\":50,\"atracao\":50,\"conexao\":50,\"confianca\":50,\"naturalidade\":50,\"arranque\":\"\",\"missao_cumprida\":false}}"
                        )
                        with st.spinner(""):
                            try:
                                from groq import Groq as _Groq3
                                _cl3 = _Groq3(api_key=st.session_state.api_key)
                                ev_txt = _cl3.chat.completions.create(messages=[{"role":"user","content":prompt_ev.encode("utf-8","ignore").decode("utf-8")}],model="openai/gpt-oss-120b",max_tokens=150).choices[0].message.content
                                jm2 = _r.search(r'\{.*\}',ev_txt,_r.DOTALL)
                                ev_d = _j.loads(jm2.group(0)) if jm2 else {}
                            except: ev_d = {}
                        delta = ev_d.get('delta',0)
                        arranque = f"🚀 {ev_d.get('arranque', '')}" if ev_d.get('arranque') else ""
                        for k in ['interesse','atracao','conexao','confianca','naturalidade']:
                            if k in ev_d: atribs[k]=max(0,min(100,ev_d[k]))
                        st.session_state.lj_atributos = atribs
                        st.session_state.lj_conexo = max(0,min(100,conexo+delta))
                        if ev_d.get('missao_cumprida'): st.session_state.lj_missao_cumprida=True
                        st.session_state.lj_combo = st.session_state.lj_combo+1 if delta>5 else 0
                        if arranque: st.session_state.lj_arranques.append(arranque)
                        ph = st.empty()
                        palavras = resp_txt.split()
                        txt_ac = ""
                        for p_w in palavras:
                            txt_ac += ("" if txt_ac=="" else " ")+p_w
                            ph.markdown(f"<div class='msg-p'><b style='color:#C2185B;'>😊 {nome_p}:</b> {txt_ac}▌</div>",unsafe_allow_html=True)
                            _t.sleep(0.07)
                        ph.empty()
                        chat.append({"role":"user","content":msg_in,"ts":_t.time()})
                        chat.append({"role":"assistant","content":resp_txt,"ts":_t.time(),"arranque":arranque})
                        st.session_state.lj_chat=chat
                        st.session_state.lj_ts_persona=_t.time()
                        st.rerun()
            with col_s:
                if st.button("🚩 Sair",key="lj_sair",use_container_width=True):
                    st.session_state.lj_ativo=False; st.session_state.lj_chat=[]
                    st.session_state.pagina="Labia"; st.rerun()
            _t.sleep(0.8); st.rerun()

    # Bloco abaixo só executa quando NÃO está no Dialogo
    if em_partida:
        st.stop()

    if not em_partida:
        if st.session_state.pagina == "Home":
            col_u, col_r = st.columns([3,1])
            with col_u:
                st.title(f"💋 Olá, {st.session_state.usuario}!")
                st.markdown(f"<span class='badge-roxo'>{faixa[0]} {faixa[2]}</span>", unsafe_allow_html=True)
            with col_r:
                if st.button("🚪 Sair", key="conexaom3"):
                    for k in list(st.session_state.keys()): del st.session_state[k]
                    st.rerun()

        if not st.session_state.historico and not st.session_state.conversas_analisadas:
            arq_h = st.file_uploader("Restaurar dados (.json):", type=["json"], key="upload_home")
            if arq_h:
                try:
                    d = json.load(arq_h); carregar_json(d); salvar_cache(st.session_state.usuario)
                    st.success("✅ Dados restaurados!"); st.rerun()
                except: st.error("Arquivo inválido.")

        # PAINEL PRINCIPAL
        st.markdown(f"""
        <div class='painel-conexa'>
            <div style='font-size:0.82em;opacity:0.7;letter-spacing:2px;margin-bottom:12px;'>🧠 Conexão Magnética 2026 — PAINEL DE INTELIGÊNCIA</div>
            <div style='font-size:1.1em;opacity:0.6;margin-bottom:16px;'>A IA que ajuda você a entender a conversa — e saber o próximo passo.</div>
            <div style='display:grid;grid-template-columns:repeat(3,1fr);gap:14px;'>
                <div style='text-align:center;background:rgba(255,255,255,0.06);border-radius:12px;padding:14px;'>
                    <div style='font-size:0.7em;opacity:0.6;'>⚡ NÍVEL ATUAL</div>
                    <div style='font-size:1.3em;font-weight:700;'>{faixa[2]}</div>
                </div>
                <div style='text-align:center;background:rgba(255,255,255,0.06);border-radius:12px;padding:14px;'>
                    <div style='font-size:0.7em;opacity:0.6;'>💬 CONVERSAS</div>
                    <div style='font-size:1.6em;font-weight:700;'>{st.session_state.conversas_analisadas}</div>
                </div>
                <div style='text-align:center;background:rgba(255,255,255,0.06);border-radius:12px;padding:14px;'>
                    <div style='font-size:0.7em;opacity:0.6;'>🃏 CARTAS USADAS</div>
                    <div style='font-size:1.6em;font-weight:700;'>{st.session_state.cartas_usadas}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # DASHBOARD MÉTRICAS
        st.markdown("### 📊 Seu Desempenho")
        c1,c2,c3,c4,c5,c6 = st.columns(6)
        c1.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.conversas_analisadas}</div><div>Conversas</div></div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.mensagens_aprimoradas}</div><div>Turbinadas</div></div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.analises_realizadas}</div><div>Análises</div></div>", unsafe_allow_html=True)
        c4.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.cartas_usadas}</div><div>Cartas</div></div>", unsafe_allow_html=True)
        c5.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.treinos_realizados}</div><div>Treinos</div></div>", unsafe_allow_html=True)
        c6.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.favoritos_total}</div><div>Favoritos</div></div>", unsafe_allow_html=True)

        # EVOLUÇÃO
        st.markdown("### 📈 Evolução")
        metricas = [
            ("Clareza", st.session_state.clareza),
            ("Naturalidade", st.session_state.naturalidade),
            ("Reciprocidade", st.session_state.reciprocidade),
            ("Confiança", st.session_state.confianca),
            ("Escuta", st.session_state.escuta),
        ]
        for nome_m, val in metricas:
            cor = "#22C55E" if val >= 7 else ("#B45309" if val >= 4 else "#B91C1C")
            st.markdown(f"""
            <div style='margin-bottom:10px;'>
                <div style='display:flex;justify-content:space-between;font-size:0.88em;font-weight:600;color:#1A1A2E;'>
                    <span>{nome_m}</span><span style='color:{cor};'>{val}/10</span>
                </div>
                <div style='background:#F1F5F9;border-radius:999px;height:8px;overflow:hidden;margin-top:4px;'>
                    <div style='height:100%;border-radius:999px;background:{cor};width:{val*10}%;'></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # GUIA DE ABAS
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("### 🗺️ O que cada aba faz")
        guia = {
            "⚡ Resposta Rápida": "Cole uma mensagem e receba 3 opções de resposta com estratégia",
            "🃏 Carta na Manga": "Quando você não sabe o que dizer — a IA encontra uma nova possibilidade",
            "💬 Turbinar": "Melhore qualquer mensagem — clareza, tom e naturalidade",
            "🧠 Raio-X": "Análise completa de uma conversa — fluidez, reciprocidade e oportunidades",
            "🎭 Roleplay": "Simule conversas e receba avaliação detalhada",
            "🎭 Arte da Lábia": "Treinamento adaptativo em 7 faixas — do iniciante ao Don Juan",
            "📚 Biblioteca": "Suas melhores respostas organizadas por categoria",
            "📸 Leitor de Perfil": "Analisa informações públicas e sugere assuntos de conversa",
            "⚔️ Comparar": "Compare duas conversas e descubra qual tem melhor dinâmica",
            "🗓️ Plano 7 Dias": "Plano de desenvolvimento de comunicação personalizado",
            "📈 Progresso": "Sua evolução ao longo do tempo em todas as métricas",
            "📋 Relatório": "Resumo semanal gerado automaticamente pela IA",
        }
        for aba, desc in guia.items():
            st.markdown(f"**{aba}** — <span style='color:#4B5563;'>{desc}</span>", unsafe_allow_html=True)

        if st.session_state.historico:
            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            st.markdown("### 🕐 Últimas Atividades")
            for item in reversed(st.session_state.historico[-4:]):
                st.markdown(f"<div class='hist-item'><span class='badge'>{item['tipo']}</span> <small style='color:#888'>{item['data']}</small><br><small>{item.get('tema', '')[:80]}</small></div>", unsafe_allow_html=True)

        # ──────────────────────────────────────────
        # RESPOSTA RÁPIDA
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Rapida":
            st.header("⚡ Resposta Inteligente")
            st.markdown("Cole a mensagem recebida e receba 3 opções estratégicas de resposta.")

            msg_recebida = st.text_area("💬 Mensagem recebida:", height=100, placeholder="Cole a mensagem aqui...", key="conexaom4")
            col1, col2 = st.columns(2)
            with col1:
                quem = st.selectbox("Quem é essa pessoa?", ["Colega","Amigo","Pessoa nova","Interesse romântico","Familiar","Outro"], key="conexaom5")
            with col2:
                objetivo = st.selectbox("O que você quer fazer?", ["Continuar a conversa","Responder de forma natural","Esclarecer algo","Iniciar um assunto novo","Dar um passo à frente"], key="conexaom6")

        contexto_extra = st.text_input("Contexto adicional (opcional):", placeholder="ex: acabamos de nos conhecer, faz 2 dias que não falamos...", key="conexaom7")

        if st.button("⚡ ANALISAR E RESPONDER", key="conexaom8"):
            if msg_recebida.strip():
                with st.spinner("Analisando o contexto..."):
                    prompt = (
                        f"Analise esta mensagem e gere 3 opções estratégicas de resposta.\n"
                        f"Mensagem recebida: '{msg_recebida}'\n"
                        f"Quem enviou: {quem}. Objetivo: {objetivo}. Contexto: {contexto_extra or 'não informado'}.\n\n"
                        f"REGRAS:\n"
                        f"- NÃO afirme intenções ou sentimentos que não podem ser conhecidos\n"
                        f"- Trabalhe apenas com padrões observáveis na mensagem\n"
                        f"- Respostas devem soar naturais, não robóticas\n\n"
                        f"FORMATO:\n\n"
                        f"📊 LEITURA DO CONTEXTO:\n[O que é observável nessa mensagem — tom, abertura, oportunidades]\n\n"
                        f"💬 OPÇÃO 1 — NATURAL\n[resposta]\nPor quê: [explicação curta]\n\n"
                        f"💡 OPÇÃO 2 — INTERESSANTE\n[resposta]\nPor quê: [explicação curta]\n\n"
                        f"🎯 OPÇÃO 3 — DIRETA\n[resposta]\nPor quê: [explicação curta]\n\n"
                        f"⭐ RECOMENDAÇÃO:\n[qual das 3 é mais adequada para esse contexto e por quê]"
                    )
                    res = conexa_ia(prompt)
                    st.session_state.analises_realizadas += 1
                    st.session_state.conversas_analisadas += 1
                    verificar_conquistas()
                    salvar_historico("Resposta Rápida", msg_recebida[:60], res)
                    st.session_state['rapida_temp'] = res
            else:
                st.warning("Cole a mensagem antes de analisar.")

        if st.session_state.get('rapida_temp'):
            st.markdown(f"<div class='card'>{st.session_state['rapida_temp']}</div>", unsafe_allow_html=True)
            col_cp, col_fv, col_sv = st.columns(3)
            with col_cp:
                st.download_button("📋 Copiar (.txt)", data=st.session_state['rapida_temp'], file_name="resposta.txt", mime="text/plain", use_container_width=True, key="dl_conexa_3")
            with col_fv:
                if st.button("⭐ Favoritar", key="fav_rapida", use_container_width=True):
                    st.session_state.biblioteca.append({'categoria':'Respostas','conteudo':st.session_state['rapida_temp'],'data':datetime.now().strftime('%d/%m %H:%M')})
                    st.session_state.favoritos_total += 1
                    st.success("⭐ Salvo na biblioteca!")
            with col_sv:
                if st.button("🃏 Carta na Manga", key="carta_rapida", use_container_width=True):
                    st.session_state.pagina = "Carta"; st.rerun()

        # ──────────────────────────────────────────
        # CARTA NA MANGA
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Carta":
            st.header("🃏 Carta na Manga")
            st.markdown("Quando você não sabe mais o que dizer — a IA encontra uma nova possibilidade.")

            conversa_carta = st.text_area("💬 Cole a conversa completa:", height=180, placeholder="Cole aqui toda a conversa...", key="conexaom9")
            contexto_carta = st.text_input("Contexto (opcional):", placeholder="ex: amigo, interesse romântico, colega de trabalho...", key="conexaom10")

            if st.button("🃏 GERAR CARTAS NA MANGA", key="conexaom11"):
                if conversa_carta.strip():
                    with st.spinner("A IA está procurando novas possibilidades..."):
                        prompt = (
                        f"Analise esta conversa e gere 5 cartas na manga — novas possibilidades de interação.\n"
                        f"Conversa:\n{conversa_carta}\n"
                        f"Contexto: {contexto_carta or 'não informado'}\n\n"
                        f"REGRAS:\n"
                        f"- Trabalhe APENAS com o que está na conversa\n"
                        f"- NÃO fabrique fatos, interesses ou sentimentos\n"
                        f"- Cada carta deve ser genuinamente diferente das outras\n\n"
                        f"FORMATO:\n\n"
                        f"🃏 CARTA #01 — RESGATAR UM ASSUNTO\n"
                        f"[mensagem sugerida]\n"
                        f"Por que essa carta: [explicação]\n\n"
                        f"🃏 CARTA #02 — MUDAR O RUMO\n"
                        f"[mensagem sugerida]\n"
                        f"Por que essa carta: [explicação]\n\n"
                        f"🃏 CARTA #03 — PERGUNTA-CHAVE\n"
                        f"[pergunta aberta]\n"
                        f"Por que essa carta: [explicação]\n\n"
                        f"🃏 CARTA #04 — LEVEZA\n"
                        f"[abordagem descontraída]\n"
                        f"Por que essa carta: [explicação]\n\n"
                        f"🛡️ CARTA #05 — DAR ESPAÇO\n"
                        f"[avaliação de quando não insistir é o melhor caminho]\n\n"
                        f"⭐ CARTA RECOMENDADA: [número e por quê é a melhor agora]"
                    )
                    res = conexa_ia(prompt)
                    st.session_state.cartas_usadas += 1
                    verificar_conquistas()
                    salvar_historico("Carta na Manga", conversa_carta[:60], res)
                    st.session_state['carta_temp'] = res
            else:
                st.warning("Cole a conversa antes de gerar.")

        if st.session_state.get('carta_temp'):
            st.markdown(f"<div class='carta-box'>{st.session_state['carta_temp']}</div>", unsafe_allow_html=True)
            col_cp, col_fv = st.columns(2)
            with col_cp:
                st.download_button("📋 Baixar (.txt)", data=st.session_state['carta_temp'], file_name="carta_manga.txt", mime="text/plain", use_container_width=True, key="dl_conexa_4")
            with col_fv:
                if st.button("⭐ Favoritar cartas", key="fav_carta", use_container_width=True):
                    st.session_state.biblioteca.append({'categoria':'Cartas na Manga','conteudo':st.session_state['carta_temp'],'data':datetime.now().strftime('%d/%m %H:%M')})
                    st.session_state.favoritos_total += 1
                    st.success("⭐ Salvo!")

        # ──────────────────────────────────────────
        # TURBINAR
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Turbinar":
            st.header("💬 Turbinar Mensagem")
            st.markdown("Cole sua mensagem e a IA a aprimora — clareza, tom e naturalidade.")

            msg_orig = st.text_area("✍️ Sua mensagem:", height=100, placeholder="Cole sua mensagem aqui...", key="conexaom12")
            col1, col2 = st.columns(2)
            with col1:
                estilo = st.selectbox("Estilo desejado:", ["Natural","Leve","Confiante","Divertido","Direto","Empático"], key="conexaom13")
            with col2:
                contexto_turb = st.text_input("Contexto:", placeholder="ex: primeira mensagem, resposta após sumiço...", key="conexaom14")

        if st.button("💬 TURBINAR MENSAGEM", key="conexaom15"):
            if msg_orig.strip():
                with st.spinner("Aprimorando..."):
                    prompt = (
                        f"Avalie e melhore esta mensagem.\n"
                        f"Mensagem original: '{msg_orig}'\n"
                        f"Estilo desejado: {estilo}. Contexto: {contexto_turb or 'não informado'}.\n\n"
                        f"FORMATO:\n\n"
                        f"📊 AVALIAÇÃO DA MENSAGEM ORIGINAL:\n"
                        f"• Clareza: [nota]/10\n"
                        f"• Naturalidade: [nota]/10\n"
                        f"• Tom: [análise]\n"
                        f"• Reciprocidade: [abre espaço para o outro?]\n"
                        f"• Pressão: [há pressão excessiva?]\n\n"
                        f"❌ ANTES:\n{msg_orig}\n\n"
                        f"✅ DEPOIS — ESTILO {estilo.upper()}:\n[mensagem aprimorada]\n\n"
                        f"🧠 POR QUE MELHOROU:\n[explicação objetiva das mudanças]\n\n"
                        f"💡 VARIAÇÃO ALTERNATIVA:\n[outra versão em estilo diferente]"
                    )
                    res = conexa_ia(prompt)
                    st.session_state.mensagens_aprimoradas += 1
                    verificar_conquistas()
                    salvar_historico("Turbinar", msg_orig[:60], res)
                    st.session_state['turb_temp'] = res
            else:
                st.warning("Cole a mensagem antes de turbinar.")

        if st.session_state.get('turb_temp'):
            st.markdown(f"<div class='card'>{st.session_state['turb_temp']}</div>", unsafe_allow_html=True)
            if st.button("⭐ Favoritar", key="fav_turb"):
                st.session_state.biblioteca.append({'categoria':'Mensagens Turbinadas','conteudo':st.session_state['turb_temp'],'data':datetime.now().strftime('%d/%m %H:%M')})
                st.session_state.favoritos_total += 1
                st.success("⭐ Salvo!")

        # ──────────────────────────────────────────
        # RAIO-X DA CONVERSA
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Analisar":
            st.header("🧠 Raio-X da Conversa")
            st.markdown("Análise completa — fluidez, reciprocidade, qualidade e oportunidades.")

            conversa_rx = st.text_area("💬 Cole a conversa completa:", height=200, placeholder="Cole a conversa aqui...", key="conexaom16")

            if st.button("🧠 ANALISAR CONVERSA", key="conexaom17"):
                if conversa_rx.strip():
                    with st.spinner("Fazendo o raio-X..."):
                        prompt = (
                        f"Faça uma análise completa desta conversa.\n\n"
                        f"IMPORTANTE: NÃO afirme sentimentos ou intenções. Apresente APENAS padrões observáveis.\n\n"
                        f"Conversa:\n{conversa_rx}\n\n"
                        f"FORMATO:\n\n"
                        f"📊 01 — FLUIDEZ\n"
                        f"Status: [🟢 Fluindo / 🟡 Perdendo ritmo / 🔴 Travada]\n"
                        f"[análise observável]\n\n"
                        f"🤝 02 — RECIPROCIDADE\n"
                        f"[Quem inicia, tamanho das respostas, perguntas feitas, equilíbrio — sem afirmar sentimentos]\n\n"
                        f"💬 03 — QUALIDADE DA COMUNICAÇÃO\n"
                        f"• Clareza: [nota]/10\n• Naturalidade: [nota]/10\n• Escuta: [nota]/10\n"
                        f"• Perguntas: [quantidade e qualidade]\n• Pressão: [há?]\n\n"
                        f"🎯 04 — ASSUNTOS\n"
                        f"✅ Que funcionaram: [lista]\n"
                        f"💡 Que podem ser explorados: [lista]\n"
                        f"📉 Que perderam força: [lista]\n\n"
                        f"🚦 05 — RADAR\n"
                        f"[🟢 / 🟡 / 🔴 com justificativa baseada em padrões observáveis]\n\n"
                        f"🎯 06 — PRÓXIMO PASSO RECOMENDADO:\n[ação concreta]"
                    )
                    res = conexa_ia(prompt)
                    st.session_state.analises_realizadas += 1
                    st.session_state.conversas_analisadas += 1
                    verificar_conquistas()
                    salvar_historico("Raio-X", conversa_rx[:60], res)
                    st.session_state['rx_temp'] = res
            else:
                st.warning("Cole a conversa antes de analisar.")

        if st.session_state.get('rx_temp'):
            st.markdown(f"<div class='card'>{st.session_state['rx_temp']}</div>", unsafe_allow_html=True)
            col_dl, col_fv = st.columns(2)
            with col_dl:
                st.download_button("📋 Baixar (.txt)", data=st.session_state['rx_temp'], file_name="raio_x.txt", mime="text/plain", use_container_width=True, key="dl_conexa_5")
            with col_fv:
                if st.button("⭐ Favoritar", key="fav_rx", use_container_width=True):
                    st.session_state.biblioteca.append({'categoria':'Análises','conteudo':st.session_state['rx_temp'],'data':datetime.now().strftime('%d/%m %H:%M')})
                    st.session_state.favoritos_total += 1; st.success("⭐ Salvo!")

        # ──────────────────────────────────────────
        # ROLEPLAY
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Roleplay":
            st.header("🎭 Simulador de Conversa")
            st.markdown("Treine antes de enviar. A IA simula uma pessoa real em um cenário.")

            if 'roleplay_chat' not in st.session_state:
                st.session_state.roleplay_chat = []
        if 'roleplay_ativo' not in st.session_state:
            st.session_state.roleplay_ativo = False
        if 'roleplay_key' not in st.session_state:
            st.session_state.roleplay_key = 0

        if not st.session_state.roleplay_ativo:
            cenario = st.selectbox("Escolha o cenário:", [
                "🤝 Conhecer alguém novo","👥 Fazer amizade","🏫 Conversar com colega",
                "💼 Networking","🗣️ Conversa difícil","😬 Situação que causa nervosismo"])
            nivel_role = st.selectbox("Dificuldade:", ["Fácil — pessoa receptiva","Médio — pessoa neutra","Difícil — pessoa reservada"], key="conexaom18")

            if st.button("🎭 INICIAR SIMULAÇÃO", key="conexaom19"):
                with st.spinner("Criando o cenário..."):
                    system_role = (
                        f"Você é uma pessoa num simulador de conversa para treino de comunicação. "
                        f"Cenário: {cenario}. Dificuldade: {nivel_role}. "
                        f"Seja realista — não force perguntas, não salve a conversa artificialmente. "
                        f"Mantenha personalidade consistente. Responda como essa pessoa responderia, "
                        f"não como um assistente. Primeira mensagem: apresente o cenário brevemente e comece a interação."
                    )
                    resp = conexa_ia("Inicie o cenário com uma fala natural da personagem.", system_role)
                    st.session_state.roleplay_chat = [{"role":"assistant","content":resp,"system":system_role}]
                    st.session_state.roleplay_ativo = True
                    st.session_state.roleplay_cenario = cenario
                    st.session_state.roleplay_system = system_role
                    st.rerun()
        else:
            st.markdown(f"**Cenário:** {st.session_state.get('roleplay_cenario','')}")
            for msg in st.session_state.roleplay_chat:
                if msg['role'] == 'user':
                    st.markdown(f"<div class='chat-user'><b style='color:#C2185B;'>Você:</b> {msg['content']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='chat-persona'><b style='color:#1D4ED8;'>🎭 Personagem:</b> {msg['content']}</div>", unsafe_allow_html=True)

            msg_role = st.text_input("Sua resposta:", key=f"role_input_{st.session_state.roleplay_key}", placeholder="O que você diria?")

            col_e, col_f = st.columns([4,1])
            with col_e:
                if st.button("📤 ENVIAR", key="conexaom20"):
                    if msg_role.strip():
                        historico_msgs = [{"role":m["role"],"content":m["content"]} for m in st.session_state.roleplay_chat]
                        with st.spinner("..."):
                            try:
                                client = Groq(api_key=st.session_state.api_key)
                                msgs = [{"role":"system","content":st.session_state.roleplay_system}] + historico_msgs + [{"role":"user","content":msg_role}]
                                resp = client.chat.completions.create(messages=msgs, model="openai/gpt-oss-120b")
                                resp_txt = resp.choices[0].message.content
                                if resp_txt: st.session_state['res_cm_conexa1'] = str(resp_txt)
                            except Exception as e:
                                resp_txt = f"⚠️ Erro: {e}"
                        st.session_state.roleplay_chat.append({"role":"user","content":msg_role})
                        st.session_state.roleplay_chat.append({"role":"assistant","content":resp_txt})
                        st.session_state.roleplay_key += 1
                        st.rerun()
            with col_f:
                if st.button("🏁 Finalizar", key="conexaom21"):
                    with st.spinner("Avaliando sua performance..."):
                        hist_txt = "\n".join(f"{'Usuário' if m['role']=='user' else 'Personagem'}: {m['content']}" for m in st.session_state.roleplay_chat)
                        prompt_aval = (
                            f"Avalie a performance deste usuário na simulação de conversa.\n"
                            f"Cenário: {st.session_state.get('roleplay_cenario','')}\n\n"
                            f"Conversa:\n{hist_txt}\n\n"
                            f"FORMATO:\n\n"
                            f"🏆 AVALIAÇÃO DA SIMULAÇÃO\n\n"
                            f"| Competência | Nota |\n|---|---|\n"
                            f"| 🗣️ Naturalidade | [X]/10 |\n"
                            f"| 👂 Escuta | [X]/10 |\n"
                            f"| ❓ Qualidade das perguntas | [X]/10 |\n"
                            f"| 🔄 Adaptação | [X]/10 |\n"
                            f"| 🤝 Reciprocidade | [X]/10 |\n\n"
                            f"⭐ NOTA GERAL: [X]/10\n\n"
                            f"🟢 O QUE VOCÊ FEZ BEM:\n[feedback específico]\n\n"
                            f"🟡 O QUE PODE MELHORAR:\n[feedback específico]\n\n"
                            f"🎯 PRÓXIMO DESAFIO:\n[o que trabalhar na próxima simulação]"
                        )
                        aval = conexa_ia(prompt_aval)
                        st.session_state.treinos_realizados += 1
                        verificar_conquistas()
                        salvar_historico("Roleplay", st.session_state.get('roleplay_cenario',''), aval)
                        st.session_state['role_aval'] = aval
                        st.session_state.roleplay_ativo = False
                        st.session_state.roleplay_chat = []
                        st.rerun()

        if st.session_state.get('role_aval'):
            st.markdown(f"<div class='avaliacao-box'>{st.session_state['role_aval']}</div>", unsafe_allow_html=True)
            st.download_button("📋 Baixar avaliação (.txt)", data=st.session_state['role_aval'], file_name="avaliacao_roleplay.txt", mime="text/plain", key="dl_conexa_6")


        # ──────────────────────────────────────────
        # A ARTE DA LÁBIA — SISTEMA COMPLETO
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Labia":
            import time as _t, random as _rand, re as _re2

            PHASES_L = ["Atração", "Conexão", "Sedução"]
            PHASE_EMOJI_L = {"Atração":"🔥","Conexão":"💫","Sedução":"❤️"}
            PHASE_DIFFICULTY_L = {"Atração":"Paquerador","Conexão":"Galanteador","Sedução":"Mestre da Lábia"}
            RANK_ORDER_L = ["Aspirante","Paquerador","Galanteador","Mestre da Lábia"]
            RANK_AFTER_L = {"Atração":"Paquerador","Conexão":"Galanteador","Sedução":"Mestre da Lábia"}
            PASS_THRESHOLD_L = 60
            PHASE_SECONDS_L = 300
            CRITERIA_W = {"naturalidade":0.20,"confianca":0.20,"criatividade":0.15,"conexao":0.20,"humor":0.10,"conducao":0.15}
            CRITERIA_LBL = {"naturalidade":"🗣️ Naturalidade","confianca":"😎 Confiança","criatividade":"🎯 Criatividade","conexao":"🧲 Conexão","humor":"😂 Humor","conducao":"🧭 Condução"}

            CHARACTERS_L = {
                "Rafaela":{"emoji":"👩","estrelas":2,"unlock_rank":None,"pronome":"ela","descricao":"Inteligente, espontânea e seletiva.","bio":"31 anos, designer. Curte cerâmica, filme de terror e café coado. Irônica, direta."},
                "Camila":{"emoji":"👩‍🦰","estrelas":3,"unlock_rank":"Paquerador","pronome":"ela","descricao":"Segura, provocadora, testa confiança.","bio":"27 anos, advogada. Corre 10km, joga xadrez. Detecta puxa-saquismo na hora."},
                "Helena":{"emoji":"👩‍💼","estrelas":5,"unlock_rank":"Galanteador","pronome":"ela","descricao":"Sofisticada, só se abre com quem conquista.","bio":"34 anos, sommelier. Fala 3 idiomas. Fecha se sentir técnica de paquera."},
                "André":{"emoji":"👨","estrelas":2,"unlock_rank":None,"pronome":"ele","descricao":"Comunicativo, reage bem ao humor.","bio":"29 anos, fisioterapeuta. Nota quando alguém é forçado e esfria."},
                "Lucas":{"emoji":"🧑‍🎤","estrelas":3,"unlock_rank":"Paquerador","pronome":"ele","descricao":"Confiante, sarcástico — testa se aguenta provocação.","bio":"26 anos, baixista. Faz cara de tédio se sentir cantada decorada."},
                "Diego":{"emoji":"🕴️","estrelas":5,"unlock_rank":"Galanteador","pronome":"ele","descricao":"Extremamente seletivo, fala pouco mas repara em tudo.","bio":"33 anos, chef. Só reage a quem traz algo genuíno."},
            }

            CENARIOS_L = ["fila de um café badalado","festa de aniversário","sala de espera de workshop","parque","corredor de livraria","show ao ar livre","loja de discos","cozinha de workshop","elevador","mesa comunitária de bar"]

            RANK_STYLE_L = {"Aspirante":{"emoji":"⚪","badge":"badge"},"Paquerador":{"emoji":"🟢","badge":"badge-verde"},"Galanteador":{"emoji":"🟡","badge":"badge-amarelo"},"Mestre da Lábia":{"emoji":"🔴","badge":"badge-roxo"}}

            for k,v in [
                ('ml_estagio','home'),('ml_character',None),('ml_phase_index',0),
                ('ml_phase_start',None),('ml_connexometer',100),('ml_messages',[]),
                ('ml_interaction_scores',[]),('ml_phase_results',{}),
                ('ml_phase_message_start',0),('ml_phase_coachings',{}),
                ('ml_current_rank',"Aspirante"),('ml_cenario',None),
                ('ml_aberturas_usadas',[]),('ml_historico',[]),('ml_last_result',None),
                ('ml_response_since',None),
            ]:
                if k not in st.session_state: st.session_state[k] = v

            def ml_reset(keep_char=False):
                for k in ['ml_phase_index','ml_phase_start','ml_connexometer','ml_messages',
                          'ml_interaction_scores','ml_phase_results','ml_phase_message_start',
                          'ml_phase_coachings','ml_cenario','ml_last_result','ml_response_since']:
                    st.session_state[k] = {'ml_phase_index':0,'ml_phase_start':None,'ml_connexometer':100,
                        'ml_messages':[],'ml_interaction_scores':[],'ml_phase_results':{},
                        'ml_phase_message_start':0,'ml_phase_coachings':{},'ml_cenario':None,
                        'ml_last_result':None,'ml_response_since':None}[k]
                st.session_state.ml_current_rank = "Aspirante"
                if not keep_char: st.session_state.ml_character = None
                st.session_state.ml_estagio = "home"

            def ml_maior_rank():
                melhor = 0
                for h in st.session_state.ml_historico:
                    rk = h.get("rank_final","Aspirante")
                    if rk in RANK_ORDER_L: melhor = max(melhor, RANK_ORDER_L.index(rk))
                return RANK_ORDER_L[melhor]

            def ml_desbloqueado(nome):
                info = CHARACTERS_L[nome]
                if info["unlock_rank"] is None: return True
                return RANK_ORDER_L.index(ml_maior_rank()) >= RANK_ORDER_L.index(info["unlock_rank"])

            def ml_weighted(av):
                return sum(av[k]*CRITERIA_W[k] for k in CRITERIA_W)

            def ml_avg(lista):
                if not lista: return {k:60 for k in CRITERIA_W}
                return {k: sum(a[k] for a in lista)/len(lista) for k in CRITERIA_W}

            def ml_build_system(character, difficulty, phase):
                char = CHARACTERS_L[character]
                cenario = st.session_state.ml_cenario or "situação social casual"
                phase_ctx = {"Atração":f"FASE 1 — ATRAÇÃO. Vocês se conheceram em: {cenario}. Desperte interesse com leveza.","Conexão":"FASE 2 — CONEXÃO. Aprofunde: histórias, valores, personalidade.","Sedução":"FASE 3 — SEDUÇÃO. Tensão romântica sutil. Se grosseiro, recue."}[phase]
                diff_ctx = {"Paquerador":"Nível fácil: seja receptivo, ajude a conversa.","Galanteador":"Nível médio: seja seletivo, responda curto às vezes.","Mestre da Lábia":"Nível difícil: não facilite, teste a confiança."}[difficulty]
                return f"""Você é {character}. {char['descricao']}
BIOGRAFIA: {char['bio']}
{phase_ctx}
{diff_ctx}
REGRAS: Respostas CURTAS (1 frase). Use detalhes específicos da bio. NUNCA revele que é IA.
Após sua fala, avalie 0-100: naturalidade, confianca, criatividade, conexao, humor, conducao. Delta -15 a 15.
JSON: {{"resposta":"fala","avaliacao":{{"naturalidade":0,"confianca":0,"criatividade":0,"conexao":0,"humor":0,"conducao":0}},"delta_conexometro":0}}"""

            def ml_call_ai(character, difficulty, phase, history, user_msg=None, opening=False):
                from groq import Groq as _GrML
                client = _GrML(api_key=st.session_state.api_key)
                system = ml_build_system(character, difficulty, phase)
                cenario = st.session_state.ml_cenario or "situação social casual"
                bloq = ""
                if opening and st.session_state.ml_aberturas_usadas:
                    lista = " | ".join(f'"{a}"' for a in st.session_state.ml_aberturas_usadas[-5:])
                    bloq = f"NÃO repita: {lista}."
                opening_prompt = f"Gere sua fala de abertura no cenário: {cenario}. Curta, com personalidade. {bloq} JSON de sempre com zeros."
                msgs = [{"role":"system","content":system}]
                for m in history:
                    msgs.append({"role":"assistant" if m["role"]=="assistant" else "user","content":m["content"]})
                msgs.append({"role":"user","content":opening_prompt if opening else user_msg})
                for attempt in range(3):
                    try:
                        kwargs = dict(model="openai/gpt-oss-120b",messages=msgs,temperature=0.9,max_tokens=350)
                        if attempt==0: kwargs["response_format"]={"type":"json_object"}
                        resp = client.chat.completions.create(**kwargs)
                        raw = resp.choices[0].message.content
                        if raw: st.session_state['res_cm_conexa2'] = str(raw)
                        try: data = import_json_ml(raw)
                        except:
                            s,e2 = raw.find("{"),raw.rfind("}")
                            data = import_json_ml(raw[s:e2+1]) if s!=-1 and e2>s else {}
                        resposta = (data.get("resposta") or "").strip()
                        av = data.get("avaliacao",{})
                        for k in CRITERIA_W: av[k] = max(0,min(100,int(av.get(k,50))))
                        delta = max(-15,min(15,int(data.get("delta_conexometro",0))))
                        if len(resposta.strip(".\n"))<2: raise ValueError("vazia")
                        return resposta, av, delta
                    except: continue
                return "Opa, o que você ia dizer?", {k:50 for k in CRITERIA_W}, 0

            import json as import_json_ml_mod
            def import_json_ml(s): return import_json_ml_mod.loads(s)

            def ml_coaching(character, phase, phase_msgs, scores):
                if not phase_msgs: return "Você não respondeu nesta fase."
                conv = "\n".join(f"{'Você' if m['role']=='user' else character}: {m['content']}" for m in phase_msgs)
                fracos = ", ".join(f"{CRITERIA_LBL[k]} ({int(v)}/100)" for k,v in sorted(scores.items(),key=lambda x:x[1])[:3] if v<70)
                fortes = ", ".join(f"{CRITERIA_LBL[k]} ({int(v)}/100)" for k,v in sorted(scores.items(),key=lambda x:x[1],reverse=True)[:2])
                try:
                    from groq import Groq as _GrCo
                    client = _GrCo(api_key=st.session_state.api_key)
                    prompt = (f"Coach — fase '{phase}' com {character}.\nConversa:\n{conv}\n\nFracos:{fracos or 'nenhum'}\nFortes:{fortes}\n\n"
                             f"Feedback direto citando exemplos REAIS. Máx 180 palavras.\n🔴 O QUE NÃO FUNCIONOU:\n🟢 O QUE FUNCIONOU:\n💡 PARA SUBIR DE NÍVEL:")
                    r = client.chat.completions.create(model="openai/gpt-oss-120b",messages=[{"role":"user","content":prompt}],temperature=0.6,max_tokens=600)
                    return r.choices[0].message.content.strip()
                except: return "Não foi possível gerar feedback."

            estagio_l = st.session_state.ml_estagio

            # ── HOME ──
            if estagio_l == "home":
                st.markdown("## 👑 Mestre da Lábia")
                st.markdown("*Você não vai aprender o que dizer — vai aprender a conversar.*")
                st.markdown("""<div class='card'>
                🔥 <strong>Fase 1 — Atração</strong> → <span class='badge-verde'>🟢 Paquerador</span><br>
                💫 <strong>Fase 2 — Conexão</strong> → <span class='badge-amarelo'>🟡 Galanteador</span><br>
                ❤️ <strong>Fase 3 — Sedução</strong> → <span class='badge-roxo'>🔴 Mestre da Lábia</span>
                </div>""", unsafe_allow_html=True)
                if st.session_state.ml_historico:
                    st.markdown("### 🕐 Últimos treinos")
                    for item in reversed(st.session_state.ml_historico[-4:]):
                        rk2 = RANK_STYLE_L.get(item.get("rank_final","Aspirante"),RANK_STYLE_L["Aspirante"])
                        st.markdown(f"<div class='card'><span class='badge'>{item['personagem']}</span> <span class='{rk2["badge"]}'>{rk2['emoji']} {item.get('rank_final','Aspirante')}</span> <small style='color:#888'>{item['data']}</small> — <strong>{item.get('overall', 0)}/100</strong></div>",unsafe_allow_html=True)
                col_c = st.columns([1,2,1])[1]
                with col_c:
                    if st.button("🔥 COMEÇAR TREINAMENTO", use_container_width=True, key="ml_iniciar"):
                        ml_reset(); st.session_state.ml_estagio="character"; st.rerun()

            # ── ESCOLHA DE PERSONAGEM ──
            elif estagio_l == "character":
                st.markdown("### 🎭 Escolha sua personagem")
                rank_at = ml_maior_rank()
                rk_at = RANK_STYLE_L[rank_at]
                st.markdown(f"Seu maior rank: <span class='{rk_at["badge"]}'>{rk_at['emoji']} {rank_at}</span>",unsafe_allow_html=True)
                cols_p = st.columns(3)
                for i,(nome_p2,info_p) in enumerate(CHARACTERS_L.items()):
                    col_p = cols_p[i%3]
                    desbloq = ml_desbloqueado(nome_p2)
                    estrelas = "⭐"*info_p["estrelas"]+"☆"*(5-info_p["estrelas"])
                    with col_p:
                        if desbloq:
                            st.markdown(f"<div class='card' style='text-align:center;'><div style='font-size:2em;'>{info_p['emoji']}</div><div style='font-weight:700;'>{nome_p2}</div><div style='color:#F5C542;'>{estrelas}</div><div style='font-size:0.8em;'>{info_p['descricao']}</div></div>",unsafe_allow_html=True)
                            if st.button(f"Escolher {nome_p2}", key=f"ml_char_{nome_p2}", use_container_width=True):
                                st.session_state.ml_character = nome_p2
                                ml_reset(keep_char=True)
                                st.session_state.ml_cenario = _rand.choice(CENARIOS_L)
                                st.session_state.ml_estagio = "training"
                                st.rerun()
                        else:
                            unlock_rk2 = RANK_STYLE_L[info_p["unlock_rank"]]
                            st.markdown(f"<div class='card' style='text-align:center;opacity:.5;'><div style='font-size:2em;'>🔒</div><div style='font-weight:700;'>{nome_p2}</div><div style='color:#F5C542;'>{estrelas}</div><div style='font-size:0.8em;'>{info_p['descricao']}</div><div style='font-size:0.75em;'>Desbloqueia com <span class='{unlock_rk2["badge"]}'>{unlock_rk2['emoji']} {info_p['unlock_rank']}</span></div></div>",unsafe_allow_html=True)
                            st.button("🔒 Bloqueada", key=f"ml_locked_{nome_p2}", use_container_width=True, disabled=True)

            # ── TREINAMENTO ──
            elif estagio_l == "training":
                phase = PHASES_L[st.session_state.ml_phase_index]
                character = st.session_state.ml_character
                difficulty = PHASE_DIFFICULTY_L[phase]

                if st.session_state.ml_phase_start is None:
                    st.session_state.ml_phase_start = _t.time()
                    if phase=="Atração" and not st.session_state.ml_messages:
                        with st.spinner(f"{character} está chegando..."):
                            resp_op,_av_op,_d_op = ml_call_ai(character,difficulty,phase,[],opening=True)
                        st.session_state.ml_messages.append({"role":"assistant","content":resp_op})
                        st.session_state.ml_aberturas_usadas = (st.session_state.ml_aberturas_usadas+[resp_op])[-10:]
                        st.session_state.ml_response_since = _t.time()

                elapsed  = _t.time()-st.session_state.ml_phase_start
                remaining= max(0,PHASE_SECONDS_L-elapsed)
                mins_r   = int(remaining//60); segs_r=int(remaining%60)
                rk2 = RANK_STYLE_L[st.session_state.ml_current_rank]
                st.markdown(f"<h4>{PHASE_EMOJI_L[phase]} FASE {st.session_state.ml_phase_index+1} — {phase.upper()}</h4>",unsafe_allow_html=True)
                st.markdown(f"<span class='{rk2["badge"]}'>{rk2['emoji']} {st.session_state.ml_current_rank}</span> <span class='badge'>{CHARACTERS_L[character]['emoji']} {character}</span>",unsafe_allow_html=True)

                cx = st.session_state.ml_connexometer
                cor_cx = "#22C55E" if cx>70 else ("#84CC16" if cx>50 else ("#F59E0B" if cx>30 else "#EF4444"))
                pulso = "animation:pulso 0.8s ease-in-out infinite;" if cx<=20 else ""
                cor_t2 = "#22C55E" if remaining>60 else ("#F59E0B" if remaining>20 else "#EF4444")
                st.markdown(f"<style>@keyframes pulso{{0%,100%{{opacity:1}}50%{{opacity:.4}}}}</style><div style='display:flex;align-items:center;gap:10px;padding:8px 12px;background:#fff;border:2px solid #22C55E;border-radius:10px;margin-bottom:8px;'><span style='font-size:0.7em;color:#64748B;font-weight:600;'>❤️ CONEXÔMETRO</span><div style='flex:1;background:#F1F5F9;border-radius:999px;height:10px;'><div style='height:100%;border-radius:999px;background:{cor_cx};width:{cx}%;{pulso}'></div></div><span style='font-weight:700;color:{cor_cx};'>{cx}%</span><span style='border-left:1px solid #E2E8F0;padding-left:10px;font-weight:700;color:{cor_t2};'>⏱️ {mins_r:02d}:{segs_r:02d}</span></div>",unsafe_allow_html=True)

                for m in st.session_state.ml_messages:
                    css = "chat-persona" if m["role"]=="assistant" else "chat-user"
                    autor = f"{CHARACTERS_L[character]['emoji']} {character}" if m["role"]=="assistant" else "🙂 Você"
                    st.markdown(f"<div class='{css}'><strong>{autor}:</strong><br>{m['content']}</div>",unsafe_allow_html=True)

                if remaining<=0:
                    scores = st.session_state.ml_interaction_scores
                    avg = ml_avg(scores)
                    score = round(ml_weighted(avg))
                    passou = score>=PASS_THRESHOLD_L
                    st.session_state.ml_phase_results[phase]={"score":score,"scores":avg,"passou":passou}
                    phase_msgs = st.session_state.ml_messages[st.session_state.ml_phase_message_start:]
                    with st.spinner("Analisando..."):
                        coaching = ml_coaching(character,phase,phase_msgs,avg)
                    st.session_state.ml_phase_coachings[phase]=coaching
                    st.session_state.ml_interaction_scores=[]
                    st.session_state.ml_estagio="phase_end"; st.rerun()
                else:
                    msg_in = st.text_input("",key=f"ml_in_{len(st.session_state.ml_messages)}",placeholder="Digite sua resposta...",label_visibility="collapsed")
                    col_env2,col_sair2 = st.columns([4,1])
                    with col_env2:
                        if st.button("📤 ENVIAR", key="ml_env", use_container_width=True):
                            if msg_in.strip():
                                st.session_state.ml_messages.append({"role":"user","content":msg_in})
                                with st.spinner(f"{character} está digitando..."):
                                    resp2,av2,delta2 = ml_call_ai(character,difficulty,phase,st.session_state.ml_messages[:-1],user_msg=msg_in)
                                st.session_state.ml_messages.append({"role":"assistant","content":resp2})
                                st.session_state.ml_interaction_scores.append(av2)
                                resp_t = (_t.time()-st.session_state.ml_response_since) if st.session_state.ml_response_since else 0
                                pen = 12 if resp_t>45 else (8 if resp_t>30 else (4 if resp_t>15 else 0))
                                st.session_state.ml_connexometer = max(0,min(100,cx+delta2-pen))
                                # Penalidade de silêncio
                                blocos = int(resp_t//25) if resp_t else 0
                                if blocos>0:
                                    queda_sil = blocos*25
                                    st.session_state.ml_connexometer = max(0,st.session_state.ml_connexometer-queda_sil)
                                st.session_state.ml_response_since = _t.time()
                                st.rerun()
                    with col_sair2:
                        if st.button("🚩 Sair",key="ml_sair",use_container_width=True):
                            ml_reset(); st.rerun()
                    _t.sleep(1); st.rerun()

            # ── FIM DE FASE ──
            elif estagio_l == "phase_end":
                phase = PHASES_L[st.session_state.ml_phase_index]
                result = st.session_state.ml_phase_results.get(phase,{"score":0,"scores":{},"passou":False})
                score2,scores2,passou2 = result["score"],result["scores"],result["passou"]
                coaching2 = st.session_state.ml_phase_coachings.get(phase,"")
                st.markdown(f"<h3 style='text-align:center;'>{PHASE_EMOJI_L[phase]} {phase.upper()} — CONCLUÍDA</h3>",unsafe_allow_html=True)
                st.markdown(f"<h1 style='text-align:center;'>{score2}/100</h1>",unsafe_allow_html=True)
                st.caption(f"Nota de corte: {PASS_THRESHOLD_L}/100")
                if passou2:
                    novo_rank2 = RANK_AFTER_L[phase]
                    st.session_state.ml_current_rank = novo_rank2
                    rk3 = RANK_STYLE_L[novo_rank2]
                    st.markdown(f"<div class='card' style='text-align:center;'><h3>🎉 VOCÊ PASSOU!</h3><h2><span class='{rk3["badge"]}'>{rk3['emoji']} {novo_rank2.upper()}</span></h2></div>",unsafe_allow_html=True)
                else:
                    rk_at2 = RANK_STYLE_L[st.session_state.ml_current_rank]
                    st.markdown(f"<div class='card' style='text-align:center;'><h3>❌ NÃO PASSOU DESTA VEZ</h3><p>Você continua <span class='{rk_at2["badge"]}'>{rk_at2['emoji']} {st.session_state.ml_current_rank}</span></p></div>",unsafe_allow_html=True)
                if coaching2:
                    st.markdown(f"<div class='card'>{coaching2}</div>",unsafe_allow_html=True)
                st.markdown("<hr class='divider'>",unsafe_allow_html=True)
                is_last = st.session_state.ml_phase_index>=len(PHASES_L)-1
                encerrar = (not passou2) or is_last
                label_btn = "🏆 VER RESULTADO FINAL" if encerrar else f"{PHASE_EMOJI_L[PHASES_L[st.session_state.ml_phase_index+1]]} PRÓXIMA FASE"
                if st.button(label_btn, use_container_width=True, key="ml_prox"):
                    if encerrar:
                        all_scores2 = [r["scores"] for r in st.session_state.ml_phase_results.values()]
                        avg2 = ml_avg(all_scores2)
                        overall2 = round(ml_weighted(avg2))
                        entry2 = {"data":datetime.now().strftime("%d/%m/%Y %H:%M"),"personagem":st.session_state.ml_character,"rank_final":st.session_state.ml_current_rank,"treino_completo":passou2 and is_last,"overall":overall2,"fases":{p2:r2["score"] for p2,r2 in st.session_state.ml_phase_results.items()},"criterios":avg2}
                        st.session_state.ml_historico.append(entry2)
                        st.session_state.ml_last_result = entry2
                        st.session_state.ml_estagio = "final"
                    else:
                        st.session_state.ml_phase_index += 1
                        st.session_state.ml_phase_start = None
                        st.session_state.ml_phase_message_start = len(st.session_state.ml_messages)
                        st.session_state.ml_estagio = "training"
                    st.rerun()

            # ── RESULTADO FINAL ──
            elif estagio_l == "final":
                entry3 = st.session_state.ml_last_result
                if not entry3:
                    st.session_state.ml_estagio="home"; st.rerun()
                else:
                    rk4 = RANK_STYLE_L.get(entry3.get("rank_final","Aspirante"),RANK_STYLE_L["Aspirante"])
                    st.markdown(f"<h2 style='text-align:center;'>{'🏆 TREINO COMPLETO!' if entry3.get('treino_completo') else 'Resultado'}</h2>",unsafe_allow_html=True)
                    st.markdown(f"<h1 style='text-align:center;font-size:4em;'>{entry3['overall']}</h1>",unsafe_allow_html=True)
                    st.markdown(f"<h3 style='text-align:center;'><span class='{rk4["badge"]}'>{rk4['emoji']} {entry3['rank_final'].upper()}</span></h3>",unsafe_allow_html=True)
                    st.markdown("<hr class='divider'>",unsafe_allow_html=True)
                    c1f,c2f,c3f = st.columns(3)
                    c1f.metric("🔥 Atração",entry3["fases"].get("Atração","—"))
                    c2f.metric("💫 Conexão",entry3["fases"].get("Conexão","—"))
                    c3f.metric("❤️ Sedução",entry3["fases"].get("Sedução","—"))
                    col_r1,col_r2 = st.columns(2)
                    with col_r1:
                        if st.button("🔄 Jogar Novamente",use_container_width=True,key="ml_replay"):
                            ml_reset(); st.session_state.ml_estagio="character"; st.rerun()
                    with col_r2:
                        if st.button("🏠 Voltar",use_container_width=True,key="ml_home_final"):
                            ml_reset(); st.rerun()

        elif st.session_state.pagina == "Biblioteca":
            st.header("📚 Biblioteca Inteligente")
            categorias = ["Todas","Respostas","Cartas na Manga","Mensagens Turbinadas","Análises","Primeiras conversas","Amizade","Networking","Perguntas"]
            filtro = st.selectbox("Filtrar:", categorias, key="filtro_bib")
            bib = st.session_state.biblioteca
            if filtro != "Todas":
                bib = [b for b in bib if b.get('categoria','') == filtro]
            if not bib:
                st.info("Nenhum item salvo nesta categoria ainda.")
            else:
                st.markdown(f"**{len(bib)} item(ns) encontrado(s)**")
                for i, item in enumerate(reversed(bib)):
                    idx = len(st.session_state.biblioteca) - 1 - i
                    with st.expander(f"[{item.get('categoria','')}] {item['conteudo'][:60]}... — {item['data']}"):
                        st.markdown(f"<div class='card'>{item['conteudo']}</div>", unsafe_allow_html=True)
                        col_dl, col_del = st.columns([3,1])
                        with col_dl:
                            st.download_button("📋 Baixar", data=item['conteudo'], file_name="item_biblioteca.txt", mime="text/plain", key=f"dl_bib_{i}")
                        with col_del:
                            if st.button("🗑️", key=f"del_bib_{i}"):
                                st.session_state.biblioteca.pop(idx); st.rerun()

        # ──────────────────────────────────────────
        # LEITOR DE PERFIL
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Perfil":
            st.header("📸 Leitor de Perfil")
            st.markdown("*Analisa informações públicas e sugere assuntos de conversa.*")
            st.markdown("""<div class='card-yellow'>⚠️ <strong>Limite ético:</strong> A IA trabalha APENAS com informações fornecidas por você.
            Não determina personalidade por aparência. Não afirma intenções. Não diagnostica.
            Use apenas informações públicas.</div>""", unsafe_allow_html=True)

            bio_perfil = st.text_area("📋 Informações do perfil (bio, posts, interesses):", height=150, placeholder="ex: 'Viajante apaixonada. Fotógrafa nas horas vagas. Amo trilhas e café ☕'", key="conexaom22")
            nome_perfil = st.text_input("Nome (opcional):", placeholder="ex: Marina", key="conexaom23")
            contexto_perfil = st.text_input("Como vocês se conheceram:", placeholder="ex: seguimos um ao outro, colega de trabalho, amigo em comum...", key="conexaom24")

            if st.button("📸 ANALISAR PERFIL", key="conexaom25"):
                if bio_perfil.strip():
                    with st.spinner("Analisando..."):
                        prompt = (
                            f"Analise as informações públicas deste perfil e sugira assuntos para conversa.\n"
                            f"Nome: {nome_perfil or 'não informado'}. Bio/informações: {bio_perfil}. Contexto: {contexto_perfil or 'não informado'}.\n\n"
                            f"REGRAS ABSOLUTAS:\n"
                            f"- NÃO determine personalidade por aparência\n- NÃO afirme intenções ou sentimentos\n"
                            f"- Trabalhe APENAS com informações fornecidas\n\n"
                            f"FORMATO:\n\n"
                            f"🎯 INTERESSES IDENTIFICADOS:\n[o que é explicitamente visível nas informações]\n\n"
                            f"💬 ASSUNTOS PARA CONVERSA:\n[lista de 5-7 assuntos com base nos interesses]\n\n"
                            f"❓ PERGUNTAS NATURAIS:\n[3-5 perguntas abertas relacionadas aos interesses]\n\n"
                            f"🧩 ELEMENTOS DA BIO QUE PODEM GERAR ASSUNTO:\n[análise dos elementos específicos]\n\n"
                            f"💡 COMO INICIAR A CONVERSA:\n[2-3 aberturas naturais baseadas no perfil]"
                        )
                        res = conexa_ia(prompt)
                        salvar_historico("Leitor de Perfil", bio_perfil[:60], res)
                        st.session_state['perfil_temp'] = res
                else:
                    st.warning("Cole as informações do perfil.")

            if st.session_state.get('perfil_temp'):
                st.markdown(f"<div class='card'>{st.session_state['perfil_temp']}</div>", unsafe_allow_html=True)

        # ──────────────────────────────────────────
        # COMPARAR CONVERSAS
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Comparar":
            st.header("⚔️ Comparar Duas Conversas")
            col1, col2 = st.columns(2)
            with col1:
                conv_a = st.text_area("💬 Conversa A:", height=180, placeholder="Cole a primeira conversa...", key="conexaom26")
            with col2:
                conv_b = st.text_area("💬 Conversa B:", height=180, placeholder="Cole a segunda conversa...", key="conexaom27")

            if st.button("⚔️ COMPARAR", key="conexaom28"):
                if conv_a.strip() and conv_b.strip():
                    with st.spinner("Comparando..."):
                        prompt = (
                            f"Compare estas duas conversas.\n\nConversa A:\n{conv_a}\n\nConversa B:\n{conv_b}\n\n"
                            f"FORMATO:\n\n"
                            f"🧠 COMPARAÇÃO\n\n"
                            f"| Critério | A | B |\n|---|---|---|\n"
                            f"| Clareza | [nota] | [nota] |\n"
                            f"| Naturalidade | [nota] | [nota] |\n"
                            f"| Reciprocidade | [nota] | [nota] |\n"
                            f"| Fluidez | [nota] | [nota] |\n"
                            f"| Qualidade das perguntas | [nota] | [nota] |\n\n"
                            f"🏆 MELHOR DINÂMICA:\n[qual e por quê — baseado em padrões observáveis]\n\n"
                            f"💡 O QUE A MELHOR CONVERSA FEZ DIFERENTE:\n[lições práticas]"
                        )
                        res = conexa_ia(prompt)
                        salvar_historico("Comparação", "Conversa A vs B", res)
                        st.session_state['comp_temp'] = res
                else:
                    st.warning("Cole as duas conversas.")

            if st.session_state.get('comp_temp'):
                st.markdown(st.session_state['comp_temp'])

        # ──────────────────────────────────────────
        # PLANO 7 DIAS
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Plano":
            st.header("🗓️ Plano de Evolução — 7 Dias")

            foco_plano = st.text_input("Qual aspecto da comunicação você mais quer desenvolver?",
                placeholder="ex: fazer perguntas melhores, não travar no início da conversa, lidar com silêncio...")

            if st.button("🗓️ GERAR MEU PLANO", key="conexaom29"):
                with st.spinner("Criando seu plano personalizado..."):
                    prompt = (
                        f"Crie um plano de desenvolvimento de comunicação de 7 dias.\n"
                        f"Foco principal: {foco_plano or 'desenvolvimento geral'}.\n\n"
                        f"Para cada dia:\n\n"
                        f"📅 DIA [N] — [TEMA]\n"
                        f"🎯 Objetivo do dia: [o que desenvolver]\n"
                        f"📖 Conceito: [explicação simples]\n"
                        f"💪 Exercício prático: [tarefa concreta que pode ser feita hoje]\n"
                        f"⭐ Critério de sucesso: [como saber se conseguiu]\n\n"
                        f"[repita para 7 dias]\n\n"
                        f"🏆 DIA 7 — DESAFIO FINAL:\n[simulação completa integrando tudo]"
                    )
                    res = conexa_ia(prompt)
                    st.session_state.plano_conquista = res
                    salvar_historico("Plano 7 Dias", foco_plano[:60] if foco_plano else "Geral", res)
                    st.session_state['plano_temp'] = res

            if st.session_state.get('plano_temp'):
                st.markdown(f"<div class='card'>{st.session_state['plano_temp']}</div>", unsafe_allow_html=True)
                st.download_button("📋 Baixar plano (.txt)", data=st.session_state['plano_temp'], file_name="plano_7dias.txt", mime="text/plain", key="dl_conexa_7")

        # ──────────────────────────────────────────
        # PROGRESSO
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Progresso":
            st.header("📈 Minha Evolução")

            # Atualizar métricas manualmente
            st.markdown("### 📊 Atualizar Evolução")
            st.markdown("*Após cada sessão de treino, atualize suas métricas.*")
            col1, col2 = st.columns(2)
            with col1:
                nova_clareza = st.slider("Clareza:", 0, 10, st.session_state.clareza)
                nova_naturalidade = st.slider("Naturalidade:", 0, 10, st.session_state.naturalidade)
                nova_reciprocidade = st.slider("Reciprocidade:", 0, 10, st.session_state.reciprocidade)
            with col2:
                nova_confianca = st.slider("Confiança:", 0, 10, st.session_state.confianca)
                nova_escuta = st.slider("Escuta:", 0, 10, st.session_state.escuta)

            if st.button("💾 SALVAR EVOLUÇÃO", key="conexaom30"):
                st.session_state.clareza = nova_clareza
                st.session_state.naturalidade = nova_naturalidade
                st.session_state.reciprocidade = nova_reciprocidade
                st.session_state.confianca = nova_confianca
                st.session_state.escuta = nova_escuta
                salvar_cache(st.session_state.usuario)
                st.success("✅ Evolução salva!")

            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            st.markdown("### 📊 Desempenho Geral")
            c1,c2,c3,c4,c5 = st.columns(5)
            for col, nome_m, val in [(c1,"Clareza",st.session_state.clareza),(c2,"Naturalidade",st.session_state.naturalidade),(c3,"Reciprocidade",st.session_state.reciprocidade),(c4,"Confiança",st.session_state.confianca),(c5,"Escuta",st.session_state.escuta)]:
                col.markdown(f"<div class='stat-box'><div class='stat-numero'>{val}</div><div>{nome_m}</div></div>", unsafe_allow_html=True)

            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            col_a, col_b, col_c = st.columns(3)
            col_a.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.conversas_analisadas}</div><div>Conversas analisadas</div></div>", unsafe_allow_html=True)
            col_b.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.treinos_realizados}</div><div>Treinos realizados</div></div>", unsafe_allow_html=True)
            col_c.markdown(f"<div class='stat-box'><div class='stat-numero'>{st.session_state.labia_nivel}</div><div>Nível Arte da Lábia</div></div>", unsafe_allow_html=True)

        # ──────────────────────────────────────────
        # RESUMO SEMANAL
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Resumo":
            st.header("📋 Relatório Semanal")

            if st.button("📋 GERAR RELATÓRIO", key="conexaom31"):
                with st.spinner("Gerando relatório..."):
                    prompt = (
                        f"Crie um relatório semanal de evolução em comunicação.\n"
                        f"Dados: {st.session_state.conversas_analisadas} conversas analisadas, "
                        f"{st.session_state.mensagens_aprimoradas} mensagens turbinadas, "
                        f"{st.session_state.treinos_realizados} treinos, "
                        f"{st.session_state.cartas_usadas} cartas usadas.\n"
                        f"Métricas: Clareza {st.session_state.clareza}/10, Naturalidade {st.session_state.naturalidade}/10, "
                        f"Reciprocidade {st.session_state.reciprocidade}/10, Confiança {st.session_state.confianca}/10, Escuta {st.session_state.escuta}/10.\n"
                        f"Nível Arte da Lábia: {st.session_state.labia_nivel}/7.\n\n"
                        f"FORMATO:\n\n"
                        f"📋 RELATÓRIO SEMANAL — {st.session_state.usuario.upper()}\n\n"
                        f"🧠 O QUE A IA PERCEBEU:\n"
                        f"Maior avanço: [gerado automaticamente]\n"
                        f"Ponto de atenção: [gerado automaticamente]\n"
                        f"Comportamento funcionando: [gerado automaticamente]\n"
                        f"Próximo desafio: [gerado automaticamente]\n\n"
                        f"💡 INSIGHT DA SEMANA:\n[frase personalizada baseada nos dados]\n\n"
                        f"🎯 OBJETIVOS PARA A PRÓXIMA SEMANA:\n[3 metas específicas]"
                    )
                    res = conexa_ia(prompt)
                    st.session_state.resumo_semanal = res
                    salvar_historico("Resumo Semanal", "Relatório automático", res)
                    st.session_state['resumo_temp'] = res

            if st.session_state.get('resumo_temp') or st.session_state.resumo_semanal:
                txt = st.session_state.get('resumo_temp') or st.session_state.resumo_semanal
                st.markdown(f"<div class='card'>{txt}</div>", unsafe_allow_html=True)
                st.download_button("📋 Baixar relatório (.txt)", data=txt, file_name="relatorio_semanal.txt", mime="text/plain", key="dl_conexa_10")

        # ──────────────────────────────────────────
        # CONQUISTAS
        # ──────────────────────────────────────────
        elif st.session_state.pagina == "Conquistas":
            st.header("🏆 Conquistas")
            conquistadas = st.session_state.get('conquistas', [], key="dl_conexa_12")
            total = len(CONQUISTAS_DEF, key="dl_conexa_13")
            obtidas = len(conquistadas, key="dl_conexa_14")
            st.markdown(f"**{obtidas} de {total} conquistas desbloqueadas**")
            st.progress(obtidas / total if total > 0 else 0)

            novas = verificar_conquistas()
            if novas:
                for nc in novas:
                    nome_c = next((n for ch,n,_ in CONQUISTAS_DEF if ch==nc), nc)
                    st.success(f"🏆 Nova conquista: {nome_c}!")

            cols_c = st.columns(3)
            for i, (chave, nome, desc) in enumerate(CONQUISTAS_DEF):
                obtida = chave in conquistadas
                estilo = "border:2px solid #FF69B4;" if obtida else "opacity:0.4;border:1px solid #E2E8F0;"
                icon = "🏆" if obtida else "🔒"
                with cols_c[i % 3]:
                    st.markdown(f"<div class='conquista-item' style='{estilo}'>"
                        f"<div style='font-size:1.3em;'>{icon}</div>"
                        f"<div style='font-weight:700;font-size:0.88em;color:#1A1A2E;'>{nome}</div>"
                        f"<div style='font-size:0.75em;color:#6B7280;'>{desc}</div>"
                        f"</div>", unsafe_allow_html=True)

# --- RODAPÉ ---
st.markdown(
    "<div style='text-align:center;color:#999;font-size:0.8em;margin-top:60px;'>"
    "© 2026 Conexão Magnética 2026 — Inteligência para Conversas · Quiz Com Prêmios"
    "</div>", unsafe_allow_html=True
)

# --- RODAPÉ ---
st.markdown(
    "<div style='text-align:center;color:#999;font-size:0.8em;margin-top:60px;'>"
    "</div>", unsafe_allow_html=True
)

# --- RODAPÉ ---
st.markdown(
    "<div style='text-align:center;color:#999;font-size:0.8em;margin-top:60px;'>"
    "</div>", unsafe_allow_html=True
)

# --- RODAPÉ ---
st.markdown(
    "<div style='text-align:center;color:#999;font-size:0.8em;margin-top:60px;'>"
    "</div>", unsafe_allow_html=True
)
