import streamlit as st
from datetime import date
from html import escape
import random
import time

st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- DATA --------------------
today = date.today()
start_date = date(2024, 2, 14)
days_together = (today - start_date).days

birthday_month = 6
birthday_day = 26
birthday_this_year = date(today.year, birthday_month, birthday_day)
next_birthday = birthday_this_year if today <= birthday_this_year else date(today.year + 1, birthday_month, birthday_day)
days_to_birthday = (next_birthday - today).days

wishes = [
    "สุขสันต์วันเกิดนะเธอ 💖",
    "ขอให้วันนี้เป็นวันที่ดีมาก ๆ",
    "ขอให้ยิ้มได้ทั้งวันเลย",
    "ขอให้เธอได้กินของอร่อย ๆ",
    "ขอให้ปีนี้มีแต่เรื่องที่ชอบ",
    "วันนี้เป็นวันของเธอจริง ๆ",
    "ขอให้เรื่องหนัก ๆ เบาลงเยอะ ๆ",
    "ขอให้มีแต่เรื่องน่ารัก ๆ เข้ามา",
]

memories = [
    "วันที่คุยกันแล้วไม่อยากหยุด",
    "วันที่งอนกันแล้วก็ยังกลับมาคุย",
    "วันที่ธรรมดาแต่จำได้ชัด",
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

if "opened" not in st.session_state:
    st.session_state.opened = False
if "wish_index" not in st.session_state:
    st.session_state.wish_index = 0
if "memory_index" not in st.session_state:
    st.session_state.memory_index = 0
if "spark_count" not in st.session_state:
    st.session_state.spark_count = 0
if "candles" not in st.session_state:
    st.session_state.candles = 6
if "gift_open" not in st.session_state:
    st.session_state.gift_open = False
if "secret_open" not in st.session_state:
    st.session_state.secret_open = False
if "mood" not in st.session_state:
    st.session_state.mood = 64
if "cover_clicks" not in st.session_state:
    st.session_state.cover_clicks = 0
if "typed_done" not in st.session_state:
    st.session_state.typed_done = False

# -------------------- CSS --------------------
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 12% 12%, rgba(255, 181, 213, 0.55), transparent 24%),
            radial-gradient(circle at 88% 16%, rgba(184, 165, 255, 0.42), transparent 20%),
            radial-gradient(circle at 50% 92%, rgba(255, 225, 172, 0.30), transparent 28%),
            linear-gradient(135deg, #fdeaf1 0%, #f5efff 46%, #fff4df 100%);
        background-attachment: fixed;
    }

    .block-container {
        max-width: 1220px;
        padding-top: 1rem;
        padding-bottom: 2.3rem;
    }

    .floatwrap {
        position: fixed;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }

    .heart {
        position: absolute;
        bottom: -40px;
        opacity: 0.22;
        animation: floatup linear infinite;
        user-select: none;
    }

    .spark {
        position: absolute;
        border-radius: 999px;
        opacity: 0.28;
        animation: drift ease-in-out infinite;
    }

    @keyframes floatup {
        0% { transform: translateY(0) scale(0.9) rotate(0deg); opacity: 0; }
        12% { opacity: 0.28; }
        100% { transform: translateY(-115vh) scale(1.2) rotate(20deg); opacity: 0; }
    }

    @keyframes drift {
        0%, 100% { transform: translateY(0) translateX(0); }
        50% { transform: translateY(-12px) translateX(14px); }
    }

    .hero {
        position: relative;
        z-index: 2;
        background: rgba(255,255,255,0.74);
        border: 1px solid rgba(125, 87, 140, 0.10);
        border-radius: 30px;
        padding: 28px 22px;
        text-align: center;
        box-shadow: 0 18px 40px rgba(105, 71, 102, 0.10);
        backdrop-filter: blur(10px);
        margin-bottom: 18px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.85);
        border: 1px solid rgba(125, 87, 140, 0.10);
        color: #8a5e8f;
        font-weight: 800;
        margin-bottom: 12px;
        font-size: 0.92rem;
    }

    .title {
        font-size: clamp(2.2rem, 5vw, 4.2rem);
        font-weight: 900;
        margin: 0;
        color: #5a3460;
        letter-spacing: -0.03em;
    }

    .subtitle {
        margin: 12px auto 0 auto;
        max-width: 840px;
        color: #725a72;
        line-height: 1.75;
        font-size: 1rem;
    }

    .topgrid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-top: 18px;
        position: relative;
        z-index: 2;
    }

    .stat {
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(125, 87, 140, 0.10);
        border-radius: 22px;
        padding: 16px 14px;
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        text-align: center;
    }

    .num {
        font-size: 2rem;
        font-weight: 900;
        color: #6a3f73;
        line-height: 1;
    }

    .label {
        margin-top: 6px;
        color: #7c687b;
        font-size: 0.92rem;
    }

    .panel {
        margin-top: 18px;
        padding: 18px;
        border-radius: 26px;
        background: rgba(255,255,255,0.70);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 12px 26px rgba(105, 71, 102, 0.08);
        position: relative;
        z-index: 2;
        backdrop-filter: blur(8px);
    }

    .panel h2 {
        margin: 0 0 8px 0;
        color: #5a3460;
        font-size: 1.35rem;
    }

    .panel p {
        margin: 0;
        color: #725a72;
        line-height: 1.72;
    }

    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 12px;
    }

    .chip {
        padding: 8px 12px;
        border-radius: 999px;
        background: linear-gradient(135deg, rgba(255, 146, 184, 0.24), rgba(173, 142, 255, 0.24));
        border: 1px solid rgba(125, 87, 140, 0.10);
        color: #5f3966;
        font-weight: 700;
        font-size: 0.92rem;
    }

    .glass {
        padding: 16px;
        border-radius: 22px;
        background: rgba(255,255,255,0.80);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        height: 100%;
    }

    .gtitle {
        color: #5a3460;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .gbody {
        color: #725a72;
        line-height: 1.68;
        font-size: 0.96rem;
    }

    .story {
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        margin-top: 12px;
    }

    .story .t {
        color: #5a3460;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .story .d {
        color: #725a72;
        line-height: 1.65;
        font-size: 0.95rem;
    }

    .final {
        padding: 18px;
        border-radius: 24px;
        background: rgba(255,255,255,0.84);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 12px 24px rgba(105, 71, 102, 0.08);
        text-align: center;
    }

    .final h3 {
        margin: 0 0 8px 0;
        color: #5a3460;
        font-size: 1.45rem;
    }

    .final p {
        color: #725a72;
        line-height: 1.7;
        margin: 0;
    }

    .bigtext {
        color: #5a3460;
        font-size: 1.08rem;
        line-height: 1.8;
        font-weight: 700;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 999px;
        border: 0;
        padding: 0.82rem 1rem;
        background: linear-gradient(135deg, #ff7da8, #b07cff);
        color: white;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(94, 60, 97, 0.18);
        transition: transform 0.16s ease, box-shadow 0.16s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 28px rgba(94, 60, 97, 0.22);
    }

    @media (max-width: 1100px) {
        .topgrid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 700px) {
        .topgrid { grid-template-columns: 1fr; }
        .hero { padding: 22px 16px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- FLOATING EFFECTS --------------------
hearts_html = "".join(
    f'<span class="heart" style="left:{random.randint(0,100)}%; '
    f'font-size:{random.randint(16,32)}px; '
    f'animation-duration:{random.randint(8,14)}s; '
    f'animation-delay:{random.uniform(0,6):.2f}s;">❤</span>'
    for _ in range(18)
)

sparkles_html = "".join(
    f'<span class="spark" style="left:{random.randint(0,100)}%; top:{random.randint(0,100)}%; '
    f'width:{random.randint(8,18)}px; height:{random.randint(8,18)}px; '
    f'background: rgba({random.randint(220,255)}, {random.randint(160,220)}, {random.randint(190,255)}, 0.35); '
    f'animation-duration:{random.randint(5,10)}s; '
    f'animation-delay:{random.uniform(0,4):.2f}s;"></span>'
    for _ in range(12)
)

st.markdown(
    f"<div class='floatwrap'>{hearts_html}{sparkles_html}</div>",
    unsafe_allow_html=True,
)

def card(title, body):
    return f"""
    <div class="glass">
        <div class="gtitle">{title}</div>
        <div class="gbody">{body}</div>
    </div>
    """

# -------------------- COVER --------------------
if not st.session_state.opened:
    st.markdown(
        """
        <div class="hero">
            <div class="badge">🎁</div>
            <div class="title">มีของให้เปิด</div>
            <div class="subtitle">กดตรงนี้</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("เปิด"):
        st.session_state.opened = True
        st.rerun()

    st.stop()

# -------------------- MAIN HERO --------------------
st.markdown(
    """
    <div class="hero">
        <div class="badge">Birthday Gift for เธอ 🎂</div>
        <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
        <div class="subtitle">
            วันนี้ขอให้เป็นวันของเธอจริง ๆ กดเล่นได้เลย
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="topgrid">
        <div class="stat"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิดถัดไป</div></div>
        <div class="stat"><div class="num">{days_together}</div><div class="label">วันที่เริ่มคบกัน</div></div>
        <div class="stat"><div class="num">{st.session_state.spark_count}</div><div class="label">ครั้งที่กดเล่น</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- ACTION PANEL --------------------
st.markdown(
    """
    <div class="panel">
        <h2>กดเล่นได้เลย</h2>
        <p>ไม่ต้องอ่านเยอะ แค่กดแล้วมันเปลี่ยน</p>
        <div class="chips">
            <span class="chip">🎁</span>
            <span class="chip">🎂</span>
            <span class="chip">🫶</span>
            <span class="chip">✨</span>
            <span class="chip">💌</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- TABS --------------------
tab1, tab2, tab3, tab4 = st.tabs(["🎁", "🌍", "💌", "✨"])

with tab1:
    left, right = st.columns([1.1, 0.9])

    with left:
        a, b, c = st.columns(3)
        with a:
            if st.button("🎀"):
                st.session_state.wish_index = random.randint(0, len(wishes) - 1)
                st.session_state.spark_count += 1
        with b:
            if st.button("🕯️"):
                st.session_state.candles = min(8, st.session_state.candles + 1)
                st.session_state.spark_count += 1
        with c:
            if st.button("💨"):
                st.session_state.candles = 0
                st.session_state.gift_open = True
                st.session_state.spark_count += 1
                st.balloons()

        candles = "🕯️ " * st.session_state.candles if st.session_state.candles > 0 else "🎂 ✨ 🎂"

        st.markdown(
            f"""
            <div class="panel">
                <h2>เค้ก</h2>
                <p style="margin-bottom:10px;">{candles}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(card(wishes[st.session_state.wish_index], tiny_lines[st.session_state.wish_index % len(tiny_lines)]), unsafe_allow_html=True)

        if st.button("✨"):
            st.session_state.gift_open = True
            st.session_state.spark_count += 1
            st.snow()

        st.markdown(
            f"""
            <div class="story">
                <div class="t">กดไปแล้ว</div>
                <div class="d">{st.session_state.spark_count} ครั้ง</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        mode = st.select_slider("", options=["💗", "🎂", "✨", "🫶", "🌷"], value="💗", label_visibility="collapsed")
        mode_text = {
            "💗": "นุ่ม ๆ",
            "🎂": "วันเกิด",
            "✨": "วิบวับ",
            "🫶": "อบอุ่น",
            "🌷": "ละมุน",
        }[mode]

        st.markdown(card(mode, mode_text), unsafe_allow_html=True)

        st.session_state.mood = st.slider(" ", 0, 100, st.session_state.mood, label_visibility="collapsed")
        st.progress(st.session_state.mood / 100)

        if st.session_state.mood < 30:
            mood_text = "ยังนุ่ม ๆ อยู่"
        elif st.session_state.mood < 70:
            mood_text = "เริ่มเข้าฟีลแล้ว"
        else:
            mood_text = "ตอนนี้เป็นวันพิเศษแล้ว"

        st.markdown(
            f"""
            <div class="story">
                <div class="t">{mood_text}</div>
                <div class="d">{tiny_lines[st.session_state.mood % len(tiny_lines)]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("🫶"):
            st.session_state.gift_open = True
            st.session_state.spark_count += 1
            st.balloons()

        if st.session_state.gift_open:
            st.markdown(
                """
                <div class="final">
                    <h3>เปิดแล้ว</h3>
                    <p>วันนี้เป็นวันของเธอจริง ๆ</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

with tab2:
    map_left, map_right = st.columns([1.1, 0.9])

    with map_left:
        st.markdown(
            """
            <div class="panel">
                <h2>แผนที่หัวใจ</h2>
                <p>หมุดนี้คือจุดพิเศษที่อยากให้ดูนาน ๆ</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="final">
                <h3>🌍❤</h3>
                <p>ปักไว้ตรงนี้เพื่อแทน “ที่ที่อยากอยู่ด้วยนาน ๆ”</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="story">
                <div class="t">หมายเหตุ</div>
                <div class="d">ถ้าอยากให้เป็นแผนที่จริงแบบ interactive มากขึ้น ค่อยอัปเป็นตัวเต็มได้</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with map_right:
        if st.button("📍"):
            st.session_state.memory_index = random.randint(0, len(memories) - 1)
            st.session_state.spark_count += 1

        st.markdown(
            card("หมุดหัวใจ", memories[st.session_state.memory_index]),
            unsafe_allow_html=True,
        )

        st.markdown(
            card("ตำแหน่งนี้", tiny_lines[st.session_state.memory_index % len(tiny_lines)]),
            unsafe_allow_html=True,
        )

with tab3:
    if st.button("สุ่มคำอวยพร"):
        st.session_state.wish_index = random.randint(0, len(wishes) - 1)
        st.session_state.spark_count += 1

    if st.button("สุ่มความทรงจำ"):
        st.session_state.memory_index = random.randint(0, len(memories) - 1)
        st.session_state.spark_count += 1

    st.markdown(
        card("คำที่โผล่มา", wishes[st.session_state.wish_index]),
        unsafe_allow_html=True,
    )

    st.markdown(
        card("ความทรงจำที่สุ่มได้", memories[st.session_state.memory_index]),
        unsafe_allow_html=True,
    )

    st.text_input("ชื่อเล่น", value="ครีม")
    st.text_area("ข้อความถึงเธอ", value="สุขสันต์วันเกิดนะเธอ ขอให้วันนี้เป็นวันที่ดีมาก ๆ แล้วก็มีแต่เรื่องที่ชอบ", height=120)

    if st.button("เปิดข้อความ"):
        st.session_state.secret_open = True
        st.session_state.spark_count += 1

    if st.session_state.secret_open:
        st.markdown(
            """
            <div class="final">
                <h3>สุขสันต์วันเกิดนะเธอ 💖</h3>
                <p>
                    ขอให้วันนี้ยิ้มได้เยอะ ๆ<br>
                    กินของอร่อยได้เต็มที่<br>
                    แล้วก็มีแต่เรื่องดี ๆ เข้ามาแบบไม่ต้องเหนื่อยหาเอง
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.download_button(
        "ดาวน์โหลดข้อความนี้",
        data="สุขสันต์วันเกิดนะเธอ ขอให้วันนี้เป็นวันที่ดีมาก ๆ และมีแต่เรื่องที่ชอบ",
        file_name="birthday_message.txt",
        mime="text/plain",
        use_container_width=True,
    )

with tab4:
    if st.button("เปิดทั้งหมด"):
        st.session_state.gift_open = True
        st.session_state.secret_open = True
        st.session_state.spark_count += 1
        st.balloons()
        st.snow()

    g1, g2, g3, g4 = st.columns(4)
    cards = [
        ("💗", "วันนี้"),
        ("🎂", "เค้ก"),
        ("✨", "ประกาย"),
        ("🫶", "ใจ"),
    ]
    for col, (a, b) in zip([g1, g2, g3, g4], cards):
        with col:
            st.markdown(card(a, b), unsafe_allow_html=True)

    st.markdown(
        card("ท้ายสุด", "ขอให้วันนี้ดีแบบที่จำได้ไปนาน ๆ"),
        unsafe_allow_html=True,
    )

    if st.session_state.gift_open:
        st.markdown(
            """
            <div class="final">
                <h3>สุขสันต์วันเกิดนะเธอ 🎂</h3>
                <p>
                    ขอให้วันนี้ดีแบบที่เธอไม่ต้องฝืนยิ้ม<br>
                    ขอให้มีความสุขเยอะ ๆ แล้วก็จำได้ว่าตัวเองมีค่ามากแค่ไหน
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
