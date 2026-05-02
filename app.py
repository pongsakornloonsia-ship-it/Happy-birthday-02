import streamlit as st
from datetime import date
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
start_date = date(2024, 2, 14)
days_together = (today - start_date).days

birthday_this_year = date(today.year, 6, 26)
next_birthday = birthday_this_year if today <= birthday_this_year else date(today.year + 1, 6, 26)
days_to_birthday = (next_birthday - today).days

birthday_lines = [
    "สุขสันต์วันเกิดนะเธอ 🎂",
    "ขอให้วันนี้เป็นวันของเธอจริง ๆ",
    "ยิ้มเยอะ ๆ แล้วก็พักให้เต็มที่",
    "กินของอร่อยให้สุดไปเลย",
    "ขอให้ปีนี้มีแต่เรื่องที่ชอบ",
    "วันนี้ไม่ต้องคิดอะไรเยอะก็ได้",
]

cake_bases = ["ช็อกโกแลต", "สตรอว์เบอร์รี", "วานิลลา"]
cake_tops = ["สตรอว์เบอร์รี", "คุกกี้", "ช็อกโกแลต", "เชอร์รี"]
cake_fx = ["แสงดาว", "หัวใจ", "ประกาย", "ลูกโป่ง"]

gift_notes = [
    "ขอให้วันนี้ใจดีกับเธอมาก ๆ",
    "ขอให้เธอมีรอยยิ้มเต็มวัน",
    "ขอให้เรื่องดี ๆ วิ่งเข้ามาหาเอง",
    "ขอให้วันเกิดปีนี้น่าจำมากที่สุด",
]

memory_lines = [
    "วันที่คุยกันแล้วไม่อยากวางแชท",
    "วันที่งอนกันนิดนึง แต่สุดท้ายก็กลับมาคุย",
    "วันที่ธรรมดา แต่จำได้ชัด",
    "วันที่อยู่ด้วยแล้วสบายใจ",
    "วันที่รู้สึกว่าเธอสำคัญขึ้นเรื่อย ๆ",
]

final_wishes = [
    "ขอให้ปีนี้มีแต่วันสบายใจ",
    "ขอให้เธอเจอแต่เรื่องที่ชอบ",
    "ขอให้ยิ้มได้ง่ายขึ้นกว่าเดิม",
    "ขอให้ไม่ต้องเหนื่อยกับเรื่องที่ไม่จำเป็น",
    "ขอให้วันนี้และทุกวันหลังจากนี้นุ่มนวลกับเธอ",
]

# -----------------------------
# STATE
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False
if "hearts" not in st.session_state:
    st.session_state.hearts = 0
if "candles" not in st.session_state:
    st.session_state.candles = 0
if "cake_base" not in st.session_state:
    st.session_state.cake_base = cake_bases[0]
if "cake_top" not in st.session_state:
    st.session_state.cake_top = cake_tops[0]
if "cake_fx" not in st.session_state:
    st.session_state.cake_fx = cake_fx[0]
if "lucky_box" not in st.session_state:
    st.session_state.lucky_box = random.randint(0, 2)
if "gift_opened" not in st.session_state:
    st.session_state.gift_opened = False
if "wish_index" not in st.session_state:
    st.session_state.wish_index = 0
if "mood" not in st.session_state:
    st.session_state.mood = 60
if "final_open" not in st.session_state:
    st.session_state.final_open = False
if "box_result" not in st.session_state:
    st.session_state.box_result = ""

def rerun():
    try:
        st.rerun()
    except Exception:
        pass

def add_heart(n=1):
    st.session_state.hearts += n

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
        background: rgba(255,255,255,0.78);
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
        background: rgba(255,255,255,0.80);
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
        font-size: 1.3rem;
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
        background: rgba(255,255,255,0.74);
        border: 1px solid rgba(126, 89, 142, 0.10);
        box-shadow: 0 10px 22px rgba(104, 70, 103, 0.08);
    }

    .glow h3{
        margin:0 0 8px 0;
        color:#5a345f;
        font-size:1.15rem;
    }

    .glow .txt{
        color:#725b72;
        line-height:1.65;
        font-size:0.97rem;
    }

    .wishline{
        font-size: 1.2rem;
        font-weight: 900;
        color:#5a345f;
        line-height:1.6;
    }

    .boxbtn div.stButton > button{
        width:100%;
        border-radius:999px;
        border:0;
        padding: 0.82rem 1rem;
        background: linear-gradient(135deg, #ff7da8, #b07cff);
        color:white;
        font-weight:800;
        box-shadow: 0 10px 24px rgba(94,60,97,0.18);
    }

    .widebtn div.stButton > button{
        width:100%;
        border-radius:999px;
        border:0;
        padding: 0.90rem 1rem;
        background: linear-gradient(135deg, #ff7da8, #b07cff);
        color:white;
        font-weight:800;
        box-shadow: 0 10px 24px rgba(94,60,97,0.18);
    }

    .line{
        height:1px;
        background: linear-gradient(90deg, transparent, rgba(126,89,142,0.22), transparent);
        margin: 16px 0;
    }

    .candy{
        display:grid;
        grid-template-columns: repeat(4, 1fr);
        gap:12px;
    }

    .pill{
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(126, 89, 142, 0.10);
        border-radius: 22px;
        padding: 14px;
        text-align:center;
        box-shadow: 0 10px 24px rgba(104, 70, 103, 0.08);
    }

    .pill .a{
        font-size: 1.2rem;
        font-weight: 900;
        color:#5a345f;
    }

    .pill .b{
        margin-top: 6px;
        color:#725b72;
        font-size:0.95rem;
        line-height:1.55;
    }

    .final{
        text-align:center;
        padding: 22px;
        border-radius: 26px;
        background: rgba(255,255,255,0.84);
        border: 1px solid rgba(126, 89, 142, 0.10);
        box-shadow: 0 12px 24px rgba(104, 70, 103, 0.08);
    }

    .final h2{
        margin:0 0 8px 0;
        color:#5a345f;
        font-size:1.45rem;
    }

    .final p{
        margin:0;
        color:#725b72;
        line-height:1.75;
    }

    @media (max-width: 1100px){
        .grid3, .candy{grid-template-columns: 1fr 1fr;}
    }
    @media (max-width: 700px){
        .grid3, .candy{grid-template-columns: 1fr;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# COVER
# -----------------------------
if not st.session_state.started:
    st.markdown(
        """
        <div class="card hero">
            <div class="badge">🎁 Birthday Game</div>
            <div class="title">มีของให้เปิด</div>
            <div class="sub">กดเริ่ม แล้วเล่นไปทีละด่านได้เลย</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("เริ่มเล่น"):
        st.session_state.started = True
        st.session_state.hearts += 1
        rerun()
    st.stop()

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    f"""
    <div class="card hero">
        <div class="badge">🎂 วันเกิดของเธอ</div>
        <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
        <div class="sub">
            วันนี้ไม่ต้องคิดอะไรเยอะ แค่เล่นไปทีละด่าน พอจบแล้วจะมีของขวัญรออยู่
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="grid3">
        <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิดถัดไป</div></div>
        <div class="mini"><div class="num">{days_together}</div><div class="label">วันที่เริ่มคบกัน</div></div>
        <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มที่เก็บได้</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
        <div class="chiprow">
            <span class="chip">🎁 เปิดกล่อง</span>
            <span class="chip">🕯️ จุดเทียน</span>
            <span class="chip">🍰 แต่งเค้ก</span>
            <span class="chip">🎈 แตกลูกโป่ง</span>
            <span class="chip">💌 คำอวยพร</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# LEVEL 1: LIGHT THE CANDLES
# -----------------------------
st.markdown('<div class="section"><h2>ด่าน 1 • จุดเทียน</h2></div>', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6 = st.columns(6)

buttons = [col1, col2, col3, col4, col5, col6]
for i, col in enumerate(buttons):
    with col:
        if st.button("🕯️", key=f"candle_{i}"):
            st.session_state.candles = min(6, st.session_state.candles + 1)
            add_heart()

if st.session_state.candles >= 6:
    st.session_state.gift_open = True

st.markdown(
    f"""
    <div class="glow">
        <h3>เค้กตอนนี้</h3>
        <div class="wishline" style="text-align:center;">{"🕯️ " * st.session_state.candles if st.session_state.candles > 0 else "🎂 ✨ 🎂"}</div>
        <div class="txt" style="text-align:center; margin-top:10px;">กดให้ครบ แล้วค่อยไปต่อ</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.session_state.candles >= 6:
    st.success("พร้อมแล้ว ไปด่านต่อได้เลย")

# -----------------------------
# LEVEL 2: CAKE BUILDER
# -----------------------------
st.markdown('<div class="section"><h2>ด่าน 2 • แต่งเค้ก</h2></div>', unsafe_allow_html=True)
cake_col1, cake_col2, cake_col3 = st.columns(3)

with cake_col1:
    st.session_state.cake_base = st.selectbox("ฐานเค้ก", cake_bases, index=cake_bases.index(st.session_state.cake_base))
with cake_col2:
    st.session_state.cake_top = st.selectbox("ท็อปปิ้ง", cake_tops, index=cake_tops.index(st.session_state.cake_top))
with cake_col3:
    st.session_state.cake_fx = st.selectbox("เอฟเฟกต์", cake_fx, index=cake_fx.index(st.session_state.cake_fx))

cake_art = f"🎂 {st.session_state.cake_base} + {st.session_state.cake_top} + {st.session_state.cake_fx}"
st.markdown(
    f"""
    <div class="glow">
        <h3>เค้กของเธอ</h3>
        <div class="wishline" style="text-align:center;">{cake_art}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("เสิร์ฟเค้ก"):
    add_heart(2)
    st.session_state.wish_index = random.randint(0, len(birthday_lines) - 1)
    st.session_state.memory_index = random.randint(0, len(memory_lines) - 1)
    st.session_state.final_open = True
    st.balloons()

# -----------------------------
# LEVEL 3: GIFT BOX HUNT
# -----------------------------
st.markdown('<div class="section"><h2>ด่าน 3 • เลือกกล่องของขวัญ</h2></div>', unsafe_allow_html=True)
box1, box2, box3 = st.columns(3)
box_pressed = None

with box1:
    if st.button("🎁", key="box1"):
        box_pressed = 0
with box2:
    if st.button("🎁", key="box2"):
        box_pressed = 1
with box3:
    if st.button("🎁", key="box3"):
        box_pressed = 2

if box_pressed is not None:
    add_heart()
    if box_pressed == st.session_state.lucky_box:
        st.session_state.box_result = "เจอแล้ว 🎉"
        st.session_state.final_open = True
        st.snow()
    else:
        st.session_state.box_result = "ยังไม่ใช่ ลองอีกใบ"

st.markdown(
    f"""
    <div class="glow">
        <h3>ผลลัพธ์</h3>
        <div class="wishline" style="text-align:center;">{st.session_state.box_result if st.session_state.box_result else "เลือกสักกล่อง"}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# LEVEL 4: WISH MIXER
# -----------------------------
st.markdown('<div class="section"><h2>ด่าน 4 • คำอวยพร</h2></div>', unsafe_allow_html=True)
wish_col1, wish_col2 = st.columns([1.2, 0.8])

with wish_col1:
    st.session_state.mood = st.slider("ฟีลวันนี้", 0, 100, st.session_state.mood)
    if st.button("สุ่มคำอวยพร"):
        st.session_state.wish_index = random.randint(0, len(birthday_lines) - 1)
        add_heart()

with wish_col2:
    st.markdown(
        f"""
        <div class="glow">
            <h3>แต้มฟีล</h3>
            <div class="wishline" style="text-align:center;">{st.session_state.mood}</div>
            <div class="txt" style="text-align:center; margin-top:8px;">
                {random.choice(tiny_lines := [
                    "เบา ๆ แต่กินใจ",
                    "น่ารักแบบไม่ต้องพยายาม",
                    "วันนี้ควรยิ้มเยอะ ๆ",
                    "ของขวัญกำลังเข้าที่",
                ])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <div class="glow">
        <h3>คำอวยพรที่สุ่มได้</h3>
        <div class="wishline" style="text-align:center;">{birthday_lines[st.session_state.wish_index]}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# LEVEL 5: REVEAL
# -----------------------------
st.markdown('<div class="section"><h2>ด่านสุดท้าย • ของขวัญ</h2></div>', unsafe_allow_html=True)
if st.button("เปิดของขวัญ"):
    st.session_state.final_open = True
    st.session_state.hearts += 2
    st.balloons()
    st.snow()

if st.session_state.final_open:
    final_text = random.choice(final_wishes)
    memory = random.choice(memory_lines)
    st.markdown(
        f"""
        <div class="final">
            <h2>สุขสันต์วันเกิดนะเธอ 🎂</h2>
            <p>{final_text}<br><br>{memory}<br><br>
            ขอให้วันนี้ดีมาก ๆ แล้วก็มีแต่เรื่องที่ชอบ</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# EXTRA FUN
# -----------------------------
st.markdown('<div class="section"><h2>โบนัส</h2></div>', unsafe_allow_html=True)
b1, b2, b3, b4 = st.columns(4)
bonuses = [
    ("💖", "ยิ้ม"),
    ("🎈", "ลูกโป่ง"),
    ("✨", "ประกาย"),
    ("🎁", "กล่อง"),
]
for col, (a, b) in zip([b1, b2, b3, b4], bonuses):
    with col:
        if st.button(a, key=f"bonus_{b}"):
            add_heart()
            st.session_state.box_result = f"ได้ {b} แล้ว"
            st.session_state.final_open = True

st.markdown(
    """
    <div class="card" style="text-align:center; margin-top:18px;">
        <div class="wishline">กดเล่นให้ครบ แล้วค่อยกดเปิดของขวัญ</div>
    </div>
    """,
    unsafe_allow_html=True,
)
