
"""
Rock • Paper • Scissors — Streamlit Edition
Made for Mohd Faizan Umani ♥
"""

import random
import time
import streamlit as st

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(
    page_title="RPS Battle | Mohd Faizan Umani",
    page_icon="🎮",
    layout="centered",
)

# ----------------------------- STYLES -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

* { box-sizing: border-box !important; }

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden !important;
}

.stApp {
    background: radial-gradient(circle at top, #1f1147 0%, #0b0620 60%, #05030f 100%);
    color: #f5f3ff;
    overflow-x: hidden !important;
}

/* Kill Streamlit's default side padding; responsive width instead of a hard cap */
.block-container {
    padding-left: clamp(0.8rem, 4vw, 2rem) !important;
    padding-right: clamp(0.8rem, 4vw, 2rem) !important;
    padding-top: 3.2rem !important;
    padding-bottom: 2rem !important;
    max-width: 680px !important;
    margin: 0 auto !important;
}

/* Streamlit's sticky top toolbar was overlapping the title — make it transparent
   and out of the way instead of hiding it, so menu/rerun controls still work */
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 2.5rem !important;
}

/* ---- Rock-solid 3-column grid (replaces Streamlit's fragile flex columns) ---- */
[data-testid="stHorizontalBlock"] {
    display: grid !important;
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    gap: 8px !important;
    width: 100% !important;
    max-width: 100% !important;
    align-items: stretch !important;
}
[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;
    flex: none !important;
}
/* Every nested wrapper Streamlit puts inside a column must stretch to fill it,
   otherwise the column collapses to content width and cards look tiny/misaligned */
[data-testid="stColumn"] div[data-testid="stVerticalBlock"],
[data-testid="stColumn"] div[data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stColumn"] div[data-testid="stElementContainer"],
[data-testid="stColumn"] div[data-testid="stMarkdown"],
[data-testid="stColumn"] div[data-testid="stMarkdownContainer"],
[data-testid="stColumn"] div[data-testid="stButton"] {
    width: 100% !important;
}
[data-testid="stColumn"] button {
    width: 100% !important;
}
[data-testid="stColumn"] * {
    max-width: 100% !important;
}

/* Title */
.title-box {
    text-align: center;
    padding: 6px 0 0 0;
    overflow: visible;
}
.title-box h1 {
    font-weight: 800;
    font-size: 1.5rem;
    background: linear-gradient(90deg, #ff6ec4, #7873f5, #4ade80);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
    line-height: 1.15;
}
.title-box p {
    color: #b8b3d9;
    margin-top: 4px;
    font-size: 0.78rem;
}

/* Scoreboard grid — plain CSS, not dependent on Streamlit's column DOM */
.score-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    width: 100%;
    margin: 6px 0 24px 0;
}
.score-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px;
    padding: 14px 4px;
    text-align: center;
    backdrop-filter: blur(6px);
    box-sizing: border-box;
}
.score-num {
    font-size: 1.7rem;
    font-weight: 800;
}
.score-label {
    font-size: 0.68rem;
    color: #b8b3d9;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    white-space: nowrap;
}
.you { color: #4ade80; }
.comp { color: #ff6ec4; }
.tie { color: #facc15; }

/* Choice buttons — mobile-first (small by default) */
.stButton>button {
    width: 100% !important;
    height: 58px;
    font-size: 0.95rem;
    border-radius: 14px;
    border: 2px solid rgba(255,255,255,0.15);
    background: rgba(255,255,255,0.05);
    transition: all 0.15s ease-in-out;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    padding: 0 6px !important;
}
.stButton>button:hover {
    transform: translateY(-4px) scale(1.03);
    border-color: #7873f5;
    box-shadow: 0 8px 24px rgba(120,115,245,0.45);
}

/* Result banner */
.result-banner {
    text-align: center;
    padding: 10px;
    border-radius: 14px;
    font-size: 0.9rem;
    font-weight: 800;
    margin: 14px 0;
    animation: pop 0.35s ease;
    width: 100%;
    overflow: hidden;
    box-sizing: border-box;
}
@keyframes pop {
    0% { transform: scale(0.85); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
.win  { background: rgba(74,222,128,0.15); color: #4ade80; border: 1px solid #4ade80; }
.lose { background: rgba(255,110,196,0.15); color: #ff6ec4; border: 1px solid #ff6ec4; }
.draw { background: rgba(250,204,21,0.15); color: #facc15; border: 1px solid #facc15; }

.battle-row {
    display: flex;
    justify-content: space-around;
    align-items: center;
    font-size: 2.2rem;
    margin: 10px 0;
}
.vs-text { font-size: 0.85rem; color: #b8b3d9; font-weight: 700; }

.streak-badge {
    display:inline-block;
    background: linear-gradient(90deg,#ff6ec4,#facc15);
    color:#1a1a1a;
    padding: 4px 14px;
    border-radius: 999px;
    font-weight:700;
    font-size: 0.68rem;
}

footer {visibility: hidden;}

/* Tighten default vertical spacing between Streamlit blocks */
[data-testid="stVerticalBlock"] {
    gap: 0.9rem !important;
}
div[data-testid="stMarkdownContainer"] p {
    margin-bottom: 0 !important;
}

/* ---- DESKTOP / WIDE SCREEN: make everything noticeably bigger ---- */
@media (min-width: 700px) {
    .title-box h1 { font-size: 2.8rem; }
    .title-box p { font-size: 1rem; }

    .score-grid { gap: 16px; margin: 10px 0 20px 0; }
    .score-card { padding: 22px 8px; border-radius: 18px; }
    .score-num { font-size: 2.6rem; }
    .score-label { font-size: 0.9rem; letter-spacing: 1px; }

    .stButton>button {
        height: 100px;
        font-size: 1.5rem;
        border-radius: 20px;
    }

    .battle-row { font-size: 4rem; }
    .vs-text { font-size: 1.3rem; }
    .result-banner { font-size: 1.4rem; padding: 16px; border-radius: 16px; }
    .streak-badge { font-size: 0.85rem; padding: 5px 16px; }
}
</style>
""", unsafe_allow_html=True)

# ----------------------------- STATE -----------------------------
defaults = {
    "player_score": 0,
    "comp_score": 0,
    "ties": 0,
    "history": [],
    "streak": 0,
    "best_streak": 0,
    "last_result": None,
    "rounds_played": 0,
    "match_over": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

EMOJI = {"r": "🪨", "p": "📄", "s": "✂️"}
NAME = {"r": "Rock", "p": "Paper", "s": "Scissors"}
WIN_TARGET = 3

# ----------------------------- HEADER -----------------------------
st.markdown("""
<div class="title-box">
    <h1>🎮 Rock · Paper · Scissors</h1>
    <p>Crafted with ♥ by <b>Mohd Faizan Umani</b> — first to 3 wins takes the match!</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ----------------------------- SCOREBOARD -----------------------------
st.markdown(f"""
<div class="score-grid">
    <div class="score-card">
        <div class="score-num you">{st.session_state.player_score}</div>
        <div class="score-label">You</div>
    </div>
    <div class="score-card">
        <div class="score-num tie">{st.session_state.ties}</div>
        <div class="score-label">Ties</div>
    </div>
    <div class="score-card">
        <div class="score-num comp">{st.session_state.comp_score}</div>
        <div class="score-label">Computer</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

if st.session_state.streak >= 2:
    st.markdown(
        f'<div style="text-align:center;margin:16px 0;">'
        f'<span class="streak-badge">🔥 {st.session_state.streak} Win Streak!</span></div>',
        unsafe_allow_html=True,
    )

# ----------------------------- GAME LOGIC -----------------------------
def play(choice):
    comp_choice = random.choice(list(EMOJI.keys()))
    st.session_state.rounds_played += 1

    if choice == comp_choice:
        result = "tie"
        st.session_state.ties += 1
        st.session_state.streak = 0
    elif (choice, comp_choice) in [("r", "s"), ("p", "r"), ("s", "p")]:
        result = "win"
        st.session_state.player_score += 1
        st.session_state.streak += 1
        st.session_state.best_streak = max(st.session_state.best_streak, st.session_state.streak)
    else:
        result = "lose"
        st.session_state.comp_score += 1
        st.session_state.streak = 0

    st.session_state.last_result = {
        "you": choice,
        "comp": comp_choice,
        "result": result,
    }
    st.session_state.history.insert(0, {
        "you": EMOJI[choice],
        "comp": EMOJI[comp_choice],
        "result": result,
    })
    st.session_state.history = st.session_state.history[:8]

    if st.session_state.player_score >= WIN_TARGET or st.session_state.comp_score >= WIN_TARGET:
        st.session_state.match_over = True


def reset_match():
    for k, v in defaults.items():
        st.session_state[k] = v


# ----------------------------- MATCH OVER -----------------------------
if st.session_state.match_over:
    if st.session_state.player_score > st.session_state.comp_score:
        st.markdown('<div class="result-banner win">🏆 MATCH WON! Great game</div>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown('<div class="result-banner lose">💀 MATCH LOST! Computer takes it this time.</div>', unsafe_allow_html=True)

    st.markdown(f"<p style='text-align:center;color:#b8b3d9;'>Best win streak this match: <b>{st.session_state.best_streak}</b> 🔥</p>", unsafe_allow_html=True)

    if st.button("🔁 Play Again", use_container_width=True):
        reset_match()
        st.rerun()

else:
    st.markdown("<p style='text-align:center;color:#b8b3d9;'>Choose your weapon:</p>", unsafe_allow_html=True)
    col_r, col_p, col_s = st.columns(3)
    with col_r:
        if st.button("🪨 Rock", key="rock", use_container_width=True):
            play("r")
            st.rerun()
    with col_p:
        if st.button("📄 Paper", key="paper", use_container_width=True):
            play("p")
            st.rerun()
    with col_s:
        if st.button("✂️ Scissors", key="scissors", use_container_width=True):
            play("s")
            st.rerun()

    # ----------------------------- LAST RESULT -----------------------------
    if st.session_state.last_result:
        lr = st.session_state.last_result
        st.write("")
        st.markdown(
            f"""<div class="battle-row">
                <div>{EMOJI[lr['you']]}</div>
                <div class="vs-text">VS</div>
                <div>{EMOJI[lr['comp']]}</div>
            </div>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<p style='text-align:center;color:#b8b3d9;'>You: {NAME[lr['you']]} &nbsp;|&nbsp; Computer: {NAME[lr['comp']]}</p>",
            unsafe_allow_html=True,
        )

        if lr["result"] == "win":
            st.markdown('<div class="result-banner win">✅ You Win This Round!</div>', unsafe_allow_html=True)
        elif lr["result"] == "lose":
            st.markdown('<div class="result-banner lose">❌ Computer Wins This Round!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-banner draw">🤝 It\'s a Tie!</div>', unsafe_allow_html=True)

    st.write("")
    if st.button("♻️ Reset Match", use_container_width=True):
        reset_match()
        st.rerun()

# ----------------------------- HISTORY -----------------------------
if st.session_state.history:
    st.write("---")
    st.markdown("<p style='text-align:center;color:#b8b3d9;font-weight:600;'>Recent Rounds</p>", unsafe_allow_html=True)
    hist_cols = st.columns(len(st.session_state.history))
    for col, h in zip(hist_cols, st.session_state.history):
        badge = {"win": "🟢", "lose": "🔴", "tie": "🟡"}[h["result"]]
        with col:
            st.markdown(
                f"<div style='text-align:center;'>{h['you']}<br>{h['comp']}<br>{badge}</div>",
                unsafe_allow_html=True,
            )

st.write("")
st.markdown(
    "<p style='text-align:center;color:#6b6690;font-size:0.8rem;'>Built with Streamlit • "
    "Fi-Amanillah ♥ — Mohd Faizan Umani</p>",
    unsafe_allow_html=True,
)
