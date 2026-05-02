import streamlit as st
from datetime import date
from html import escape
import random

st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# DATA
# -----------------------------
today = date.today()
birthday_this_year = date(today.year, 6, 26)
next_birthday = birthday_this_year if today <= birthday_this_year else date(today.year + 1, 6, 26)
days_to_birthday = (next_birthday - today).days

wishes = [
    "สุขสันต์วันเกิดนะเธอ 🎂",
    "ขอให้วันนี้เป็นวันของเธอจริง ๆ",
    "ยิ้มเยอะ ๆ แล้วก็พักให้เต็มที่",
    "กินของอร่อยให้สุดไปเลย",
    "ขอให้ปีนี้มีแต่เรื่องที่ชอบ",
    "วันนี้ไม่ต้องคิดอะไรเยอะก็ได้",
    "ขอให้เรื่องหนัก ๆ เบาลงเยอะ ๆ",
    "ขอให้มีแต่เรื่องน่ารัก ๆ เข้ามา",
]

cake_bases = ["ช็อกโกแลต", "วานิลลา", "สตรอว์เบอร์รี"]
cake_creams = ["ชมพู", "ครีม", "ม่วง", "ฟ้า"]
cake_toppers = ["เชอร์รี", "สตรอว์เบอร์รี", "คุกกี้", "หัวใจ"]

gift_lines = [
    "ขอให้วันนี้ใจดีกับเธอมาก ๆ",
    "ขอให้เธอมีรอยยิ้มเต็มวัน",
    "ขอให้เรื่องดี ๆ วิ่งเข้ามาหาเอง",
    "ขอให้วันเกิดปีนี้น่าจำมากที่สุด",
]

memory_lines = [
    "วันที่คุยกันแล้วไม่อยากวางแชท",
    "วันที่งอนกันนิดหน่อย แต่สุดท้ายก็กลับมาคุย",
    "วันที่ธรรมดา แต่จำได้ชัด",
    "วันที่อยู่ด้วยแล้วสบายใจ",
    "วันที่รู้สึกว่าเธอสำคัญขึ้นเรื่อย ๆ",
]

tiny_lines = [
    "เธอทำให้วันธรรมดาดีขึ้น",
    "บางทีแค่มีเธอก็พอแล้ว",
    "วันนี้ขอให้ยิ้มเยอะ ๆ",
    "ของขวัญชิ้นนี้ตั้งใจทำมาก",
    "ไม่ต้องเยอะ แต่ต้องจริงใจ",
    "ถ้าวันนี้พิเศษ ก็ให้เป็นเธอ",
]

nav_pages = ["cover", "cake", "hunt", "heart", "letter"]
nav_icons = ["🎁", "🎂", "🎮", "💗", "💌"]

# -----------------------------
# STATE
# -----------------------------
defaults = {
    "page": "cover",
    "opened": False,
    "hearts": 0,
    "wish_index": 0,
    "memory_index": 0,
    "spark_count": 0,
    "candles": 4,
    "gift_opened": False,
    "secret_open": False,
    "mood": 62,
    "cake_base": "วานิลลา",
    "cake_cream": "ครีม",
    "cake_topper": "เชอร์รี",
    "hunt_round": 0,
    "hunt_target": random.randint(1, 9),
    "hunt_msg": "",
    "heart_round": 0,
    "heart_target": random.randint(1, 4),
    "heart_msg": "",
    "final_open": False,
    "note_text": "สุขสันต์วันเกิดนะเธอ ขอให้วันนี้เป็นวันที่ดีมาก ๆ แล้วก็มีแต่เรื่องที่ชอบ",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def goto(page_name: str):
    st.session_state.page = page_name
    st.rerun()

def add_heart(n: int = 1):
    st.session_state.hearts += n

def nav_bar():
    idx = nav_pages.index(st.session_state.page)
    cols = st.columns(5)
    for i, icon in enumerate(nav_icons):
        with cols[i]:
            if st.button(icon, key=f"nav_{nav_pages[i]}", use_container_width=True):
                goto(nav_pages[i])
    st.progress((idx + 1) / len(nav_pages))

def cake_html(base: str, cream: str, topper: str, candles: int) -> str:
    base_colors = {
        "ช็อกโกแลต": "#8d5a48",
        "วานิลลา": "#e2c38b",
        "สตรอว์เบอร์รี": "#ff86aa",
    }
    cream_colors = {
        "ชมพู": "#ffd1e2",
        "ครีม": "#fff1c2",
        "ม่วง": "#d8c9ff",
        "ฟ้า": "#d6efff",
    }
    topper_emoji = {
        "เชอร์รี": "🍒",
        "สตรอว์เบอร์รี": "🍓",
        "คุกกี้": "🍪",
        "หัวใจ": "💖",
    }
    candle_line = " ".join(["🕯️"] * candles) if candles > 0 else "🎂 ✨ 🎂"
    sprinkle_row = "✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧"
    return f"""
    <div class="cake-stage">
        <div class="plate"></div>
        <div class="cake" style="--base:{base_colors[base]}; --cream:{cream_colors[cream]};">
            <div class="cake-candles">{candle_line}</div>
            <div class="cake-sparkles">{sprinkle_row}</div>
            <div class="cake-topper">{topper_emoji[topper]}</div>

            <div class="cake-layer cake-top"></div>
            <div class="cake-layer cake-mid"></div>
            <div class="cake-layer cake-bottom"></div>

            <div class="cake-frost"></div>
            <div class="cake-label">{base} • {cream} • {topper}</div>
        </div>
    </div>
    """

# -----------------------------
# STYLE
# -----------------------------
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp{
        background:
            radial-gradient(circle at 12% 12%, rgba(255, 185, 210, 0.55), transparent 24%),
            radial-gradient(circle at 88% 14%, rgba(184, 160, 255, 0.45), transparent 22%),
            radial-gradient(circle at 50% 90%, rgba(255, 224, 169, 0.30), transparent 26%),
            linear-gradient(135deg, #fde9f1 0%, #f6efff 45%, #fff4df 100%);
        background-attachment: fixed;
    }

    .block-container{
        max-width: 1240px;
        padding-top: 1rem;
        padding-bottom: 2.5rem;
    }

    .card{
        background: rgba(255,255,255,0.80);
        border: 1px solid rgba(126, 89, 142, 0.10);
        border-radius: 28px;
        box-shadow: 0 18px 40px rgba(104, 70, 103, 0.10);
        padding: 22px;
        backdrop-filter: blur(10px);
    }

    .hero{
        text-align:center;
        margin-bottom: 18px;
    }

    .badge{
        display:inline-block;
        padding: 7px 14px;
        border-radius:999px;
        background: rgba(255,255,255,0.84);
        border: 1px solid rgba(126, 89, 142, 0.10);
        color:#8a5e8f;
        font-weight:800;
        font-size: 0.92rem;
        margin-bottom: 12px;
    }

    .title{
        font-size: clamp(2.2rem, 5vw, 4.4rem);
        font-weight: 900;
        margin: 0;
        color: #5a345f;
        letter-spacing: -0.03em;
    }

    .sub{
        max-width: 860px;
        margin: 12px auto 0 auto;
        color:#725b72;
        line-height:1.75;
        font-size:1rem;
    }

    .grid3{
        display:grid;
        grid-template-columns: repeat(3, 1fr);
        gap:12px;
        margin-top: 16px;
    }

    .mini{
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(126, 89, 142, 0.10);
        border-radius: 22px;
        padding: 16px;
        text-align:center;
        box-shadow: 0 10px 24px rgba(104, 70, 103, 0.08);
    }

    .num{
        font-size: 2rem;
        font-weight: 900;
        color: #6a3f73;
        line-height: 1;
    }

    .label{
        margin-top: 6px;
        color:#7b687b;
        font-size:0.92rem;
    }

    .section{
        margin-top: 18px;
    }

    .section h2{
        margin: 0 0 10px 0;
        color:#5a345f;
        font-size: 1.25rem;
    }

    .section p{
        margin:0;
        color:#725b72;
        line-height:1.72;
    }

    .chiprow{
        display:flex;
        flex-wrap:wrap;
        gap:10px;
        margin-top:12px;
    }

    .chip{
        padding: 8px 12px;
        border-radius:999px;
        background: linear-gradient(135deg, rgba(255, 147, 186, 0.24), rgba(176, 124, 255, 0.24));
        border: 1px solid rgba(126, 89, 142, 0.10);
        color:#5f3966;
        font-weight:700;
        font-size:0.92rem;
    }

    .glow{
        padding: 18px;
        border-radius: 24px;
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(126, 89, 142, 0.10);
        box-shadow: 0 10px 22px rgba(104, 70, 103, 0.08);
        height: 100%;
    }

    .glow h3{
        margin:0 0 8px 0;
        color:#5a345f;
        font-size:1.08rem;
    }

    .glow .txt{
        color:#725b72;
        line-height:1.65;
        font-size:0.97rem;
    }

    .wishline{
        font-size: 1.15rem;
        font-weight: 900;
        color:#5a345f;
        line-height:1.6;
    }

    .line{
        height:1px;
        background: linear-gradient(90deg, transparent, rgba(126,89,142,0.22), transparent);
        margin: 16px 0;
    }

    .cake-stage{
        position: relative;
        width: 100%;
        min-height: 430px;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        margin-top: 8px;
        overflow: hidden;
    }

    .plate{
        position: absolute;
        bottom: 20px;
        width: min(620px, 94%);
        height: 36px;
        border-radius: 999px;
        background: linear-gradient(180deg, #fff, #e9dceb);
        box-shadow: 0 12px 24px rgba(97, 71, 102, 0.12);
    }

    .cake{
        position: relative;
        width: min(460px, 92vw);
        height: 360px;
    }

    .cake-layer{
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 30px 30px 18px 18px;
        box-shadow: 0 12px 24px rgba(97, 71, 102, 0.20);
        background: var(--base);
    }

    .cake-bottom{
        bottom: 36px;
        width: 300px;
        height: 118px;
    }

    .cake-mid{
        bottom: 134px;
        width: 266px;
        height: 92px;
    }

    .cake-top{
        bottom: 210px;
        width: 230px;
        height: 72px;
    }

    .cake-frost{
        position: absolute;
        bottom: 256px;
        left: 50%;
        transform: translateX(-50%);
        width: 246px;
        height: 44px;
        border-radius: 24px 24px 14px 14px;
        background: var(--cream);
        box-shadow: 0 8px 16px rgba(97, 71, 102, 0.10);
    }

    .cake-candles{
        position: absolute;
        bottom: 302px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 1.55rem;
        letter-spacing: 3px;
        white-space: nowrap;
        color: #5a345f;
        text-shadow: 0 0 12px rgba(255,255,255,0.7);
    }

    .cake-topper{
        position: absolute;
        bottom: 272px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 2rem;
    }

    .cake-sparkles{
        position: absolute;
        bottom: 188px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 0.95rem;
        letter-spacing: 8px;
        color: rgba(255,255,255,0.82);
    }

    .cake-label{
        position: absolute;
        bottom: 8px;
        left: 50%;
        transform: translateX(-50%);
        color: #6a3f73;
        font-weight: 800;
        font-size: 0.96rem;
        text-align: center;
        white-space: nowrap;
    }

    .story{
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(126, 89, 142, 0.10);
        box-shadow: 0 10px 22px rgba(104, 70, 103, 0.08);
        margin-top: 12px;
    }

    .story .t{
        color: #5a345f;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .story .d{
        color: #725b72;
        line-height: 1.65;
        font-size: 0.95rem;
    }

    .final{
        padding: 18px;
        border-radius: 24px;
        background: rgba(255,255,255,0.84);
        border: 1px solid rgba(126, 89, 142, 0.10);
        box-shadow: 0 12px 24px rgba(104, 70, 103, 0.08);
        text-align: center;
    }

    .final h3{
        margin: 0 0 8px 0;
        color:#5a345f;
        font-size: 1.45rem;
    }

    .final p{
        color:#725b72;
        line-height:1.7;
        margin:0;
    }

    .mini-btn div.stButton > button{
        width:100%;
        border-radius: 999px;
        border:0;
        padding: 0.82rem 1rem;
        background: linear-gradient(135deg, #ff7da8, #b07cff);
        color:white;
        font-weight:800;
        box-shadow: 0 10px 24px rgba(94,60,97,0.18);
    }

    .round-card{
        background: rgba(255,255,255,0.80);
        border: 1px solid rgba(126, 89, 142, 0.10);
        border-radius: 24px;
        padding: 18px;
        box-shadow: 0 10px 22px rgba(104, 70, 103, 0.08);
    }

    .round-title{
        color:#5a345f;
        font-weight:900;
        margin-bottom:8px;
    }

    .round-text{
        color:#725b72;
        line-height:1.7;
    }

    .box-grid{
        display:grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
    }

    .small-grid{
        display:grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
    }

    .map-card{
        min-height: 390px;
        display:flex;
        align-items:center;
        justify-content:center;
        text-align:center;
        font-size: 3.5rem;
        color:#5a345f;
    }

    @media (max-width: 1100px){
        .grid3, .box-grid, .small-grid{grid-template-columns: 1fr 1fr;}
    }
    @media (max-width: 700px){
        .grid3, .box-grid, .small-grid{grid-template-columns: 1fr;}
        .cake-stage{min-height: 380px;}
        .cake{height: 320px;}
        .cake-bottom{width: 250px;}
        .cake-mid{width: 220px;}
        .cake-top{width: 190px;}
        .cake-frost{width: 210px;}
    }

    div.stButton > button{
        width:100%;
        border-radius: 999px;
        border:0;
        padding: 0.82rem 1rem;
        background: linear-gradient(135deg, #ff7da8, #b07cff);
        color:white;
        font-weight:800;
        box-shadow: 0 10px 24px rgba(94,60,97,0.18);
        transition: transform 0.16s ease, box-shadow 0.16s ease;
    }

    div.stButton > button:hover{
        transform: translateY(-1px);
        box-shadow: 0 14px 28px rgba(94,60,97,0.22);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# DECORATION
# -----------------------------
hearts_html = "".join(
    f'<span style="position:fixed;left:{random.randint(0,100)}%;bottom:-20px;'
    f'font-size:{random.randint(16,32)}px;opacity:0.22;'
    f'animation:floatup {random.randint(8,14)}s linear {random.uniform(0,6):.2f}s infinite;">❤</span>'
    for _ in range(16)
)
sparkles_html = "".join(
    f'<span style="position:fixed;left:{random.randint(0,100)}%;top:{random.randint(0,100)}%;'
    f'width:{random.randint(8,18)}px;height:{random.randint(8,18)}px;border-radius:999px;'
    f'background:rgba({random.randint(220,255)}, {random.randint(160,220)}, {random.randint(190,255)}, 0.28);'
    f'animation:drift {random.randint(5,10)}s ease-in-out {random.uniform(0,4):.2f}s infinite;"></span>'
    for _ in range(10)
)
st.markdown(
    f"""
    <style>
    @keyframes floatup {{
        0% {{ transform: translateY(0) scale(0.9) rotate(0deg); opacity: 0; }}
        12% {{ opacity: 0.28; }}
        100% {{ transform: translateY(-115vh) scale(1.2) rotate(20deg); opacity: 0; }}
    }}
    @keyframes drift {{
        0%,100% {{ transform: translateY(0) translateX(0); }}
        50% {{ transform: translateY(-12px) translateX(14px); }}
    }}
    </style>
    {hearts_html}
    {sparkles_html}
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# NAV
# -----------------------------
if st.session_state.page != "cover":
    nav_bar()

# -----------------------------
# COVER
# -----------------------------
if st.session_state.page == "cover":
    st.markdown(
        """
        <div class="card hero">
            <div class="badge">🎁 Birthday Game</div>
            <div class="title">มีของให้เปิด</div>
            <div class="sub">กดเริ่ม แล้วเล่นไปทีละหน้าจอ</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="grid3">
            <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิด</div></div>
            <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มที่เก็บได้</div></div>
            <div class="mini"><div class="num">5</div><div class="label">หน้าจอ</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("เริ่มเล่น"):
        st.session_state.opened = True
        st.session_state.page = "cake"
        add_heart()
        st.rerun()

    st.stop()

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    """
    <div class="card hero">
        <div class="badge">🎂 วันเกิดของเธอ</div>
        <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
        <div class="sub">วันนี้ขอให้เป็นวันของเธอจริง ๆ</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="grid3">
        <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิดถัดไป</div></div>
        <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มที่เก็บได้</div></div>
        <div class="mini"><div class="num">{st.session_state.spark_count}</div><div class="label">ครั้งที่กดเล่น</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# PAGE 1: CAKE
# -----------------------------
if st.session_state.page == "cake":
    st.markdown(
        """
        <div class="section">
            <h2>แต่งเค้ก</h2>
            <p>ปรับให้เค้กเปลี่ยนได้เอง</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    a, b, c, d = st.columns(4)
    with a:
        st.selectbox("รส", cake_bases, key="cake_base")
    with b:
        st.selectbox("ครีม", cake_creams, key="cake_cream")
    with c:
        st.selectbox("หน้าเค้ก", cake_toppers, key="cake_topper")
    with d:
        st.slider("เทียน", 0, 8, key="candles")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("สุ่มหน้าเค้ก"):
            st.session_state.cake_base = random.choice(cake_bases)
            st.session_state.cake_cream = random.choice(cake_creams)
            st.session_state.cake_topper = random.choice(cake_toppers)
            st.session_state.candles = random.randint(0, 8)
            add_heart()
            st.rerun()
    with c2:
        if st.button("เพิ่มเทียน"):
            st.session_state.candles = min(8, st.session_state.candles + 1)
            add_heart()
            st.rerun()
    with c3:
        if st.button("ต่อไป"):
            st.session_state.page = "hunt"
            st.rerun()

    st.markdown(
        cake_html(
            st.session_state.cake_base,
            st.session_state.cake_cream,
            st.session_state.cake_topper,
            st.session_state.candles,
        ),
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="final">
            <h3>{random.choice(wishes)}</h3>
            <p>{random.choice(gift_lines)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# PAGE 2: BOX HUNT
# -----------------------------
elif st.session_state.page == "hunt":
    st.markdown(
        """
        <div class="section">
            <h2>กล่องของขวัญ</h2>
            <p>หากล่องที่ใช่ 3 รอบ</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="round-card">
            <div class="round-title">รอบ {st.session_state.hunt_round + 1} / 3</div>
            <div class="round-text">{st.session_state.hunt_msg or "เลือกกล่องได้เลย"}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    found = False
    for row in range(3):
        cols = st.columns(3)
        for col_idx in range(3):
            box_num = row * 3 + col_idx + 1
            with cols[col_idx]:
                if st.button(f"🎁 {box_num}", key=f"box_{st.session_state.hunt_round}_{box_num}"):
                    if box_num == st.session_state.hunt_target:
                        st.session_state.hunt_round += 1
                        st.session_state.hunt_msg = "เจอแล้ว"
                        st.session_state.hearts += 2
                        st.session_state.hunt_target = random.randint(1, 9)
                        add_heart()
                        found = True
                        if st.session_state.hunt_round >= 3:
                            st.session_state.gift_opened = True
                        st.rerun()
                    else:
                        st.session_state.hunt_msg = "ยังไม่ใช่"
                        st.session_state.spark_count += 1
                        st.rerun()

    if found:
        st.success("ต่อได้")

    if st.session_state.hunt_round >= 3:
        st.balloons()
        st.markdown(
            """
            <div class="final">
                <h3>ผ่
