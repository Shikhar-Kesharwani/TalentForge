import os
from dotenv import load_dotenv
import streamlit as st
from src.query_pipeline import retrieve, answer

load_dotenv()

st.set_page_config(page_title="HireSense", page_icon="🔮", layout="wide")

# ══════════════════════════════════════════════════════════════════════════════
#  ULTRA PREMIUM CSS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg:           #05050a;
    --surface:      rgba(255,255,255,0.02);
    --surface-h:    rgba(255,255,255,0.04);
    --glass:        rgba(12,12,22,0.7);
    --accent:       #8b7cf7;
    --accent2:      #00e5b0;
    --accent3:      #f472b6;
    --accent4:      #fbbf24;
    --txt:          #ededf4;
    --txt2:         #5e5e78;
    --txt3:         #3a3a50;
    --border:       rgba(255,255,255,0.05);
    --border-h:     rgba(139,124,247,0.2);
    --glow:         rgba(139,124,247,0.12);
    --r:            14px;
    --r-lg:         22px;
    --r-xl:         28px;
    --shadow:       0 4px 24px rgba(0,0,0,0.4);
    --shadow-lg:    0 16px 64px rgba(0,0,0,0.5);
}

*, *::before, *::after { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body, .stApp, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--txt);
    background: var(--bg);
}

.stApp {
    background: var(--bg) !important;
    min-height: 100vh;
    overflow-x: hidden;
}

.block-container {
    padding: 1.5rem 2rem 3rem !important;
    max-width: 1140px !important;
    margin: 0 auto !important;
}

header[data-testid="stHeader"],
header[data-testid="stHeader"] *,
.stApp > header,
.stApp > div[data-testid="stDecoration"],
div[data-testid="stStatus"],
.stApp [data-testid="stToolbar"],
.stApp [data-testid="stHeaderActionElements"],
#MainMenu,
footer,
.stDeployButton,
.stApp [aria-label="Main menu"] {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    height: 0 !important;
    max-height: 0 !important;
    overflow: hidden !important;
    margin: 0 !important;
    padding: 0 !important;
}

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 20px; }

/* ═══════════════ AMBIENT BACKGROUND ═══════════════ */
.ambient {
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    overflow: hidden;
}
.ambient::before {
    content: '';
    position: absolute;
    width: 900px; height: 900px;
    top: -300px; left: -200px;
    background: radial-gradient(circle, rgba(139,124,247,0.07) 0%, transparent 70%);
    animation: drift1 20s ease-in-out infinite alternate;
}
.ambient::after {
    content: '';
    position: absolute;
    width: 700px; height: 700px;
    bottom: -200px; right: -150px;
    background: radial-gradient(circle, rgba(0,229,176,0.05) 0%, transparent 70%);
    animation: drift2 25s ease-in-out infinite alternate;
}
@keyframes drift1 { 0%{transform:translate(0,0)} 100%{transform:translate(80px,60px)} }
@keyframes drift2 { 0%{transform:translate(0,0)} 100%{transform:translate(-60px,-40px)} }

#particle-canvas {
    position: fixed; inset: 0; width: 100%; height: 100%;
    pointer-events: none; z-index: 0;
}

/* ═══════════════ GRID NOISE TEXTURE ═══════════════ */
.noise-overlay {
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    opacity: 0.015;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* ═══════════════ TOP NAV BAR ═══════════════ */
.topbar {
    display: flex; justify-content: space-between; align-items: center;
    padding: 20px 0; border-bottom: 1px solid var(--border);
    margin-bottom: 0;
}
.topbar-brand {
    display: flex; align-items: center; gap: 12px;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700; font-size: 1.25rem; color: var(--txt);
    text-decoration: none;
}
.topbar-brand .glyph {
    font-size: 1.6rem;
    filter: drop-shadow(0 0 12px rgba(139,124,247,0.4));
}
.topbar-links {
    display: flex; gap: 8px;
}
.topbar-link {
    padding: 8px 16px; border-radius: 10px;
    font-size: 0.82rem; font-weight: 500; color: var(--txt2);
    background: transparent; border: 1px solid transparent;
    cursor: pointer; transition: all 0.25s ease;
    text-decoration: none; display: inline-flex; align-items: center; gap: 6px;
}
.topbar-link:hover {
    color: var(--txt); background: var(--surface);
    border-color: var(--border);
}
.topbar-link.primary {
    background: rgba(139,124,247,0.1); border-color: rgba(139,124,247,0.2);
    color: var(--accent);
}
.topbar-link.primary:hover {
    background: rgba(139,124,247,0.15);
    box-shadow: 0 0 20px rgba(139,124,247,0.1);
}

/* ═══════════════ HERO ═══════════════ */
.hero {
    text-align: center;
    padding: 72px 0 40px;
    position: relative;
}
.hero-glow {
    position: absolute;
    width: 500px; height: 500px;
    top: -100px; left: 50%; transform: translateX(-50%);
    background: radial-gradient(circle, rgba(139,124,247,0.08) 0%, transparent 70%);
    pointer-events: none;
    animation: heroGlow 8s ease-in-out infinite alternate;
}
@keyframes heroGlow {
    0%{opacity:0.5;transform:translateX(-50%) scale(1)}
    100%{opacity:1;transform:translateX(-50%) scale(1.15)}
}
.hero-chips {
    display: flex; justify-content: center; gap: 8px;
    margin-bottom: 24px; flex-wrap: wrap;
}
.hero-chip {
    padding: 6px 14px; border-radius: 999px;
    font-size: 0.72rem; font-weight: 500; letter-spacing: 0.3px;
    border: 1px solid var(--border); color: var(--txt2);
    background: var(--surface);
    display: inline-flex; align-items: center; gap: 6px;
    animation: chipIn 0.5s ease both;
}
.hero-chip:nth-child(1){animation-delay:0.1s}
.hero-chip:nth-child(2){animation-delay:0.2s}
.hero-chip:nth-child(3){animation-delay:0.3s}
@keyframes chipIn {
    0%{opacity:0;transform:translateY(8px)}
    100%{opacity:1;transform:translateY(0)}
}
.hero-chip .dot {
    width: 6px; height: 6px; border-radius: 50%;
}
.hero-chip .dot.g { background: var(--accent2); }
.hero-chip .dot.p { background: var(--accent); }
.hero-chip .dot.r { background: var(--accent3); }

.hero-icon {
    font-size: 64px; display: inline-block;
    margin-bottom: 16px;
    animation: iconFloat 5s ease-in-out infinite;
    filter: drop-shadow(0 0 30px rgba(139,124,247,0.3));
}
@keyframes iconFloat {
    0%,100%{transform:translateY(0) rotate(0deg)}
    50%{transform:translateY(-10px) rotate(4deg)}
}

.hero-h {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.8rem, 6vw, 4.2rem);
    font-weight: 800; letter-spacing: -3px; line-height: 1;
    margin: 0 0 16px;
    background: linear-gradient(135deg, #fff 0%, #c4b5fd 30%, var(--accent2) 70%, var(--accent) 100%);
    background-size: 200% 200%;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradText 6s ease infinite;
}
@keyframes gradText {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}

.hero-sub {
    font-size: 1.08rem; color: var(--txt2); max-width: 520px;
    margin: 0 auto 28px; line-height: 1.7; font-weight: 300;
}

.hero-cta {
    display: inline-flex; align-items: center; gap: 10px;
    padding: 14px 32px; border-radius: 14px;
    background: linear-gradient(135deg, var(--accent), #a78bfa);
    color: #fff; font-family: 'Space Grotesk', sans-serif;
    font-weight: 600; font-size: 0.95rem;
    border: none; cursor: pointer;
    transition: all 0.35s cubic-bezier(0.25,0.46,0.45,0.94);
    text-decoration: none;
    box-shadow: 0 4px 20px rgba(139,124,247,0.3);
}
.hero-cta:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 40px rgba(139,124,247,0.4);
}

/* ═══════════════ FEATURES ROW ═══════════════ */
.features {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;
    margin: 0 0 48px;
}
.feat {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r-lg);
    padding: 28px 24px;
    transition: all 0.35s ease;
    position: relative; overflow: hidden;
}
.feat::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0; transition: opacity 0.3s;
}
.feat:hover::before { opacity: 1; }
.feat:hover {
    border-color: var(--border-h);
    transform: translateY(-4px);
    box-shadow: var(--shadow);
}
.feat-icon {
    font-size: 1.8rem; margin-bottom: 14px;
    width: 52px; height: 52px;
    display: flex; align-items: center; justify-content: center;
    border-radius: 14px;
    background: rgba(139,124,247,0.06);
    border: 1px solid rgba(139,124,247,0.1);
}
.feat h3 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem; font-weight: 600; margin: 0 0 8px;
    color: var(--txt);
}
.feat p {
    font-size: 0.84rem; color: var(--txt2); line-height: 1.6; margin: 0;
}

/* ═══════════════ SEARCH PANEL ═══════════════ */
[data-testid="stForm"] {
    background: var(--glass);
    backdrop-filter: blur(40px); -webkit-backdrop-filter: blur(40px);
    border: 1px solid var(--border);
    border-radius: var(--r-xl);
    padding: 32px 36px;
    margin-bottom: 12px;
    position: relative; overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
}
[data-testid="stForm"]::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.06) 50%, transparent 100%);
}
[data-testid="stForm"]::after {
    content: '';
    position: absolute; top: -1px; left: 30%; right: 30%;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    border-radius: 2px;
}
.sp-header {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 20px;
    text-align: center;
    justify-content: center;
}
.sp-icon {
    width: 40px; height: 40px; border-radius: 12px;
    background: rgba(139,124,247,0.08); border: 1px solid rgba(139,124,247,0.15);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
}
.sp-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem; font-weight: 600; color: var(--txt);
}
.sp-sub {
    font-size: 0.82rem; color: var(--txt2); margin-top: 2px;
}

[data-testid="stForm"] [data-testid="stHorizontalBlock"] {
    justify-content: center !important;
    width: 100% !important;
}

/* ═══════════════ FORM ═══════════════ */
.stTextArea textarea,
.stTextArea textarea:focus {
    background: rgba(0,0,0,0.25) !important;
    border: 1.5px solid rgba(255,255,255,0.06) !important;
    border-radius: var(--r) !important;
    color: var(--txt) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.92rem !important;
    padding: 18px 20px !important;
    min-height: 80px !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}
.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(139,124,247,0.08), 0 0 40px rgba(139,124,247,0.05) !important;
    outline: none !important;
    background: rgba(139,124,247,0.02) !important;
}
.stTextArea textarea::placeholder {
    color: var(--txt3) !important;
    font-style: italic;
}

.stFormSubmitButton > button,
.stFormSubmitButton > button:focus {
    background: linear-gradient(135deg, var(--accent) 0%, #a78bfa 50%, var(--accent2) 100%) !important;
    background-size: 200% 200% !important;
    border: none !important;
    border-radius: var(--r) !important;
    color: #fff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    height: 56px !important;
    min-width: 180px !important;
    padding: 0 28px !important;
    letter-spacing: 0.2px !important;
    animation: gradBtn 5s ease infinite !important;
    transition: all 0.35s ease !important;
    box-shadow: 0 4px 20px rgba(139,124,247,0.25) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 8px !important;
    white-space: nowrap !important;
}
@keyframes gradBtn {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}
.stFormSubmitButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 36px rgba(139,124,247,0.35) !important;
}

/* ═══════════════ RESULTS ═══════════════ */
.results {
    margin-top: 36px;
    animation: resultsIn 0.5s ease;
}
@keyframes resultsIn {
    0%{opacity:0;transform:translateY(16px)}
    100%{opacity:1;transform:translateY(0)}
}

.res-header {
    display: flex; align-items: center; justify-content: space-between;
    margin-top: 36px; margin-bottom: 24px; flex-wrap: wrap; gap: 12px;
}
.res-badge {
    display: inline-flex; align-items: center; gap: 10px;
    padding: 10px 24px; border-radius: 999px;
    background: linear-gradient(135deg, rgba(139,124,247,0.1), rgba(0,229,176,0.06));
    border: 1px solid rgba(139,124,247,0.2);
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600; font-size: 0.82rem;
    color: #b4a8ff; letter-spacing: 0.5px; text-transform: uppercase;
    animation: badgePop 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes badgePop {
    0%{opacity:0;transform:scale(0.8)}
    100%{opacity:1;transform:scale(1)}
}
.res-badge .b-icon { font-size: 1rem; }

/* ═══════════════ STATS ═══════════════ */
.stats-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;
    margin-bottom: 28px;
}
.sg-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 20px 16px;
    text-align: center;
    transition: all 0.3s ease;
    position: relative; overflow: hidden;
}
.sg-item::after {
    content: '';
    position: absolute; bottom: 0; left: 20%; right: 20%;
    height: 2px; border-radius: 2px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0; transition: opacity 0.3s;
}
.sg-item:hover::after { opacity: 1; }
.sg-item:hover {
    border-color: var(--border-h);
    transform: translateY(-2px);
}
.sg-val {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.8rem; font-weight: 700; line-height: 1;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.sg-label {
    font-size: 0.7rem; color: var(--txt2); margin-top: 8px;
    text-transform: uppercase; letter-spacing: 1px; font-weight: 500;
}

/* ═══════════════ TWO-COL LAYOUT ═══════════════ */
.two-col {
    display: grid; grid-template-columns: 1fr 1fr; gap: 24px;
    align-items: start;
}

/* ═══════════════ ANSWER ═══════════════ */
.ans-section {}
.sec-head {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700; font-size: 1.1rem;
    color: var(--txt); margin-bottom: 16px;
    display: flex; align-items: center; gap: 10px;
}
.sec-head .h-icon {
    width: 32px; height: 32px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.95rem;
}
.sec-head .h-icon.teal { background: rgba(0,229,176,0.08); border: 1px solid rgba(0,229,176,0.15); }
.sec-head .h-icon.purple { background: rgba(139,124,247,0.08); border: 1px solid rgba(139,124,247,0.15); }

.ans-box {
    background: linear-gradient(160deg, rgba(0,229,176,0.03) 0%, rgba(139,124,247,0.03) 100%);
    border: 1px solid rgba(0,229,176,0.1);
    border-radius: var(--r-lg);
    padding: 28px 30px;
    line-height: 1.8; font-size: 0.92rem;
    color: var(--txt);
    position: relative; overflow: hidden;
    animation: ansIn 0.5s ease;
}
.ans-box::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, var(--accent2), var(--accent));
    border-radius: 3px;
}
@keyframes ansIn {
    0%{opacity:0;transform:translateX(-12px)}
    100%{opacity:1;transform:translateX(0)}
}

/* ═══════════════ CANDIDATES ═══════════════ */
.docs-list {
    display: flex; flex-direction: column; gap: 12px;
}
.doc-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 20px 22px;
    margin-bottom: 12px;
    transition: all 0.35s cubic-bezier(0.25,0.46,0.45,0.94);
    position: relative; overflow: hidden;
    animation: docIn 0.4s ease both;
}
.doc-card::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, var(--accent), var(--accent2));
    opacity: 0; transition: opacity 0.3s;
}
.doc-card:hover::before { opacity: 1; }
.doc-card:hover {
    border-color: var(--border-h);
    box-shadow: var(--shadow);
    transform: translateY(-3px);
}
.doc-card:nth-child(1){animation-delay:0s}
.doc-card:nth-child(2){animation-delay:0.06s}
.doc-card:nth-child(3){animation-delay:0.12s}
.doc-card:nth-child(4){animation-delay:0.18s}
.doc-card:nth-child(5){animation-delay:0.24s}
@keyframes docIn {
    0%{opacity:0;transform:translateY(14px)}
    100%{opacity:1;transform:translateY(0)}
}

.dc-top {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 10px;
}
.dc-id {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.8rem; font-weight: 600;
    color: var(--accent);
    background: rgba(139,124,247,0.08);
    padding: 4px 12px; border-radius: 8px;
    letter-spacing: 0.3px;
}
.dc-rank {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.75rem; font-weight: 600;
    color: var(--txt3);
    width: 28px; height: 28px;
    display: flex; align-items: center; justify-content: center;
    border-radius: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
}
.dc-rank.top { color: var(--accent4); border-color: rgba(251,191,36,0.2); background: rgba(251,191,36,0.06); }

.dc-bar-wrap { margin: 6px 0 10px; }
.dc-bar-lbl {
    display: flex; justify-content: space-between;
    font-size: 0.72rem; color: var(--txt2); margin-bottom: 4px;
}
.dc-bar {
    height: 4px; background: rgba(255,255,255,0.03);
    border-radius: 20px; overflow: hidden;
}
.dc-bar-fill {
    height: 100%; border-radius: 20px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    animation: fillBar 0.8s ease forwards;
}
@keyframes fillBar { 0%{width:0} }

.dc-text {
    font-size: 0.82rem; color: var(--txt2); line-height: 1.6;
    max-height: 80px; overflow: hidden; position: relative;
}
.dc-text::after {
    content: '';
    position: absolute; bottom: 0; left: 0; right: 0;
    height: 32px;
    background: linear-gradient(transparent, var(--bg));
    pointer-events: none;
}

/* ═══════════════ TRACE ═══════════════ */
.trace-section { margin-top: 36px; }
.trace-steps {
    display: flex; flex-direction: column; gap: 10px;
}
.ts-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 18px 22px;
    margin-bottom: 10px;
    position: relative;
    transition: all 0.3s ease;
    animation: tsIn 0.35s ease both;
}
.ts-item::before {
    content: '';
    position: absolute; left: 0; top: 0; bottom: 0;
    width: 3px; border-radius: 3px;
    background: linear-gradient(180deg, var(--accent), var(--accent2));
}
.ts-item:hover {
    border-color: var(--border-h);
    background: var(--surface-h);
}
.ts-item:nth-child(1){animation-delay:0.05s}
.ts-item:nth-child(2){animation-delay:0.10s}
.ts-item:nth-child(3){animation-delay:0.15s}
.ts-item:nth-child(4){animation-delay:0.20s}
@keyframes tsIn {
    0%{opacity:0;transform:translateX(-10px)}
    100%{opacity:1;transform:translateX(0)}
}
.ts-head {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600; font-size: 0.88rem; color: var(--txt);
    margin-bottom: 8px; display: flex; align-items: center; gap: 8px;
}
.ts-tags {
    display: flex; gap: 12px; flex-wrap: wrap;
}
.ts-tag {
    display: inline-flex; align-items: center; gap: 5px;
    font-size: 0.75rem; color: var(--txt2);
}
.ts-tag .td {
    width: 5px; height: 5px; border-radius: 50%;
    background: var(--accent2);
}

/* ═══════════════ EXPANDER ═══════════════ */
details[data-testid="stExpander"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--r) !important;
}
details summary, details summary span {
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    color: var(--txt) !important;
    font-size: 0.88rem !important;
}

.stJson {
    background: rgba(0,0,0,0.25) !important;
    border-radius: 10px !important;
    border: 1px solid var(--border) !important;
}

/* ═══════════════ EMPTY STATE ═══════════════ */
.empty-state {
    text-align: center; padding: 60px 20px;
}
.es-icon {
    font-size: 3.5rem; margin-bottom: 16px;
    animation: esBob 3s ease-in-out infinite;
}
@keyframes esBob {
    0%,100%{transform:translateY(0)}
    50%{transform:translateY(-12px)}
}
.es-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem; font-weight: 600; color: var(--txt2);
    margin-bottom: 8px;
}
.es-sub { font-size: 0.85rem; color: var(--txt3); }

/* ═══════════════ LOADING ═══════════════ */
.load-center {
    display: flex; flex-direction: column; align-items: center;
    gap: 20px; padding: 72px 0;
}
.load-ring {
    width: 56px; height: 56px;
    border: 3px solid var(--border);
    border-top-color: var(--accent);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}
@keyframes spin { 100%{transform:rotate(360deg)} }
.load-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.9rem; color: var(--txt2);
    animation: loadPulse 1.5s ease infinite;
}
@keyframes loadPulse {
    0%,100%{opacity:0.4} 50%{opacity:1}
}
.load-steps {
    display: flex; gap: 24px; font-size: 0.78rem; color: var(--txt3);
}
.load-step {
    display: flex; align-items: center; gap: 6px;
}
.load-step .ld {
    width: 6px; height: 6px; border-radius: 50%;
    animation: ldBounce 1.2s ease infinite;
}
.load-step:nth-child(1) .ld { background: var(--accent); animation-delay: 0s; }
.load-step:nth-child(2) .ld { background: var(--accent2); animation-delay: 0.2s; }
.load-step:nth-child(3) .ld { background: var(--accent3); animation-delay: 0.4s; }
.load-step:nth-child(4) .ld { background: var(--accent4); animation-delay: 0.6s; }
@keyframes ldBounce {
    0%,80%,100%{transform:scale(0.6);opacity:0.3}
    40%{transform:scale(1.2);opacity:1}
}

/* ═══════════════ FOOTER ═══════════════ */
.footer {
    margin-top: 64px; padding: 32px 0;
    border-top: 1px solid var(--border);
    display: flex; justify-content: space-between; align-items: center;
    font-size: 0.78rem; color: var(--txt3);
}
.footer a { color: var(--accent); text-decoration: none; }
.footer a:hover { color: var(--accent2); }
.footer-brand {
    display: flex; align-items: center; gap: 8px;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600; color: var(--txt2);
}

/* ═══════════════ RESPONSIVE ═══════════════ */
@media (max-width: 900px) {
    .main-wrap { padding: 0 16px; }
    .features { grid-template-columns: 1fr; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .two-col { grid-template-columns: 1fr; }
    .hero-h { font-size: 2.4rem; letter-spacing: -1.5px; }
    .topbar { flex-direction: column; gap: 12px; }
    .footer { flex-direction: column; gap: 12px; text-align: center; }
}
</style>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  BACKGROUND
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="ambient"></div>
<div class="noise-overlay"></div>
<canvas id="particle-canvas"></canvas>
<script>
(function(){
    const c = document.getElementById('particle-canvas');
    if(!c) return;
    const ctx = c.getContext('2d');
    let W, H;
    function resize(){ W=c.width=window.innerWidth; H=c.height=window.innerHeight; }
    resize(); window.addEventListener('resize', resize);

    const N = 60;
    const cols = ['rgba(139,124,247,','rgba(0,229,176,','rgba(244,114,182,'];
    const ps = Array.from({length:N}, ()=>({
        x: Math.random()*3000, y: Math.random()*3000,
        r: Math.random()*1.5+0.3,
        vx: (Math.random()-0.5)*0.18,
        vy: (Math.random()-0.5)*0.18,
        col: cols[Math.random()*3|0],
        a: Math.random()*0.35+0.05
    }));

    function frame(){
        ctx.clearRect(0,0,W,H);
        for(const p of ps){
            p.x+=p.vx; p.y+=p.vy;
            if(p.x<-10)p.x=W+10; if(p.x>W+10)p.x=-10;
            if(p.y<-10)p.y=H+10; if(p.y>H+10)p.y=-10;
            ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
            ctx.fillStyle=p.col+p.a+')'; ctx.fill();
        }
        for(let i=0;i<N;i++) for(let j=i+1;j<N;j++){
            const dx=ps[i].x-ps[j].x, dy=ps[i].y-ps[j].y;
            const d=Math.sqrt(dx*dx+dy*dy);
            if(d<140){
                ctx.beginPath();
                ctx.moveTo(ps[i].x,ps[i].y);
                ctx.lineTo(ps[j].x,ps[j].y);
                ctx.strokeStyle='rgba(139,124,247,'+(0.05*(1-d/140))+')';
                ctx.lineWidth=0.3; ctx.stroke();
            }
        }
        requestAnimationFrame(frame);
    }
    frame();
})();
</script>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
#  TOPBAR
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="topbar">
    <a class="topbar-brand" href="#">
        <span class="glyph">🔮</span> HireSense
    </a>
    <div class="topbar-links">
        <a class="topbar-link" href="#">Docs</a>
        <a class="topbar-link" href="#">API</a>
        <a class="topbar-link primary" href="https://github.com/GaurPeeyush/HireSense" target="_blank">⭐ GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ──── HERO ────
st.markdown("""
<div class="hero">
    <div class="hero-glow"></div>
    <div class="hero-chips">
        <span class="hero-chip"><span class="dot g"></span> Semantic Search</span>
        <span class="hero-chip"><span class="dot p"></span> AI Classification</span>
        <span class="hero-chip"><span class="dot r"></span> Smart Matching</span>
    </div>
    <div class="hero-icon">🔮</div>
    <h1 class="hero-h">HireSense</h1>
    <p class="hero-sub">Ask anything about your candidates. Our AI classifies your query, performs semantic search across resumes, and delivers precise, actionable answers in seconds.</p>
    <a class="hero-cta" href="#search">✨ Start Searching</a>
</div>
""", unsafe_allow_html=True)


# ──── FEATURES ────
st.markdown("""
<div class="features">
    <div class="feat">
        <div class="feat-icon">🧠</div>
        <h3>AI Classification</h3>
        <p>Automatically categorizes queries into 24 professional domains for precise filtering.</p>
    </div>
    <div class="feat">
        <div class="feat-icon">⚡</div>
        <h3>Semantic Search</h3>
        <p>Vector embeddings understand meaning, not just keywords. Find the right talent.</p>
    </div>
    <div class="feat">
        <div class="feat-icon">🎯</div>
        <h3>Precise Matching</h3>
        <p>Metadata-filtered retrieval with cosine similarity for highly relevant results.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ──── SEARCH ────
with st.form("query_form", clear_on_submit=False):
    st.markdown("""
    <div class="sp-header" id="search">
        <div class="sp-icon">🔍</div>
        <div>
            <div class="sp-title">Search Candidates</div>
            <div class="sp-sub">Describe what you're looking for — the AI handles the rest</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    q_col, b_col = st.columns([4, 1], vertical_alignment="bottom", gap="small")
    user_query = q_col.text_area(
        " ", height=96,
        placeholder="e.g.  Senior React developers with 5+ years experience in fintech",
        label_visibility="collapsed",
    )
    submitted = b_col.form_submit_button("🚀 Search", use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
#  RESULTS
# ══════════════════════════════════════════════════════════════════════════════
if submitted and user_query.strip():

    ld = st.empty()
    ld.markdown("""
    <div class="load-center">
        <div class="load-ring"></div>
        <div class="load-label">Processing your query</div>
        <div class="load-steps">
            <span class="load-step"><span class="ld"></span> Classify</span>
            <span class="load-step"><span class="ld"></span> Embed</span>
            <span class="load-step"><span class="ld"></span> Search</span>
            <span class="load-step"><span class="ld"></span> Generate</span>
        </div>
    </div>""", unsafe_allow_html=True)

    retrieved = retrieve(user_query)
    category  = retrieved.get("category")
    docs      = retrieved.get("docs", [])
    ld.empty()

    # header + badge
    st.markdown(f"""
    <div class="res-header">
        <div class="res-badge"><span class="b-icon">🏷️</span> {category}</div>
    </div>""", unsafe_allow_html=True)

    # stats
    total_ms = sum(s.get("duration_ms", 0) for s in retrieved.get("trace", []))
    st.markdown(f"""
    <div class="stats-grid">
        <div class="sg-item"><div class="sg-val">{len(docs)}</div><div class="sg-label">Candidates</div></div>
        <div class="sg-item"><div class="sg-val">{len(retrieved.get('trace',[]))}</div><div class="sg-label">Steps</div></div>
        <div class="sg-item"><div class="sg-val">{total_ms}<span style="font-size:0.5em">ms</span></div><div class="sg-label">Latency</div></div>
        <div class="sg-item"><div class="sg-val">5</div><div class="sg-label">Top K</div></div>
    </div>""", unsafe_allow_html=True)

    # two-column results: answer + candidates
    left_col, right_col = st.columns(2, gap="large", vertical_alignment="top")

    with left_col:
        st.markdown("""
        <div class="sec-head"><span class="h-icon teal">💡</span> AI Answer</div>""", unsafe_allow_html=True)
        ans = answer(user_query, retrieved)
        st.markdown(f'<div class="ans-box">{ans.get("answer","")}</div>', unsafe_allow_html=True)

    with right_col:
        st.markdown("""
        <div class="sec-head"><span class="h-icon purple">👥</span> Top Candidates</div>""", unsafe_allow_html=True)
        if not docs:
            st.markdown("""
            <div class="empty-state">
                <div class="es-icon">📭</div>
                <div class="es-title">No candidates found</div>
                <div class="es-sub">Try a different query or broaden your search</div>
            </div>""", unsafe_allow_html=True)
        else:
            for i, d in enumerate(docs[:5], 1):
                sc = d.get("score", 0) or 0
                sp = round(sc * 100, 1)
                ss = f"{sc:.4f}"
                txt = d.get("text", "")[:160]
                if len(d.get("text", "")) > 160: txt += "..."
                rank_cls = "top" if i == 1 else ""
                st.markdown(f"""
                <div class="doc-card">
                    <div class="dc-top">
                        <div class="dc-id">{d['id']}</div>
                        <div class="dc-rank {rank_cls}">#{i}</div>
                    </div>
                    <div class="dc-bar-wrap">
                        <div class="dc-bar-lbl"><span>Relevance</span><span>{ss}</span></div>
                        <div class="dc-bar"><div class="dc-bar-fill" style="width:{sp}%"></div></div>
                    </div>
                    <div class="dc-text">{txt}</div>
                </div>""", unsafe_allow_html=True)

    # ──── TRACE ────
    st.markdown("""
    <div class="trace-section">
        <div class="sec-head"><span class="h-icon purple">🔬</span> Processing Trace</div>
    </div>""", unsafe_allow_html=True)

    with st.expander("View detailed pipeline steps", expanded=False):
        for step in retrieved.get("trace", []):
            sn = step.get("step", "")
            tl = step.get("tool", "")
            md = step.get("model", "")
            ms = step.get("duration_ms", "")
            tags = []
            if tl: tags.append(f'<span class="ts-tag"><span class="td"></span>Tool: {tl}</span>')
            if md: tags.append(f'<span class="ts-tag"><span class="td"></span>Model: {md}</span>')
            if ms: tags.append(f'<span class="ts-tag"><span class="td"></span>{ms}ms</span>')
            thtml = '<div class="ts-tags">' + "".join(tags) + '</div>' if tags else ''
            st.markdown(f"""
            <div class="ts-item">
                <div class="ts-head">📌 {sn}</div>
                {thtml}
            </div>""", unsafe_allow_html=True)
            st.json(step)

        st.markdown("""
        <div class="ts-item">
            <div class="ts-head">📌 LLM Answer Generation</div>
            <div class="ts-tags">
                <span class="ts-tag"><span class="td"></span>Tool: OpenAI Chat</span>
                <span class="ts-tag"><span class="td"></span>Model: gpt-4o-mini</span>
            </div>
        </div>""", unsafe_allow_html=True)
        st.json(ans.get("trace", {}))


# ──── FOOTER ────
st.markdown("""
<div class="footer">
    <div class="footer-brand">🔮 HireSense</div>
    <div>Built with Streamlit · OpenAI · Pinecone &nbsp;│&nbsp; <a href="https://github.com/GaurPeeyush/HireSense" target="_blank">View Source</a></div>
</div>
""", unsafe_allow_html=True)
