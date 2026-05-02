import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="Happy Birthday 🎂", page_icon="🎁", layout="wide", initial_sidebar_state="collapsed")

today = date.today()
start_date = date(2024, 2, 14)
days_together = (today - start_date).days
birthday_this_year = date(today.year, 6, 26)
next_birthday = birthday_this_year if today <= birthday_this_year else date(today.year + 1, 6, 26)
days_to_birthday = (next_birthday - today).days

wishes = [
    "สุขสันต์วันเกิดนะเธอ 🎂",
    "ขอให้วันนี้ยิ้มได้ทั้งวัน",
    "ขอให้ปีนี้ใจดีกับเธอมาก ๆ",
    "กินของอร่อยให้เต็มที่เลย",
    "ขอให้ทุกอย่างที่เหนื่อย ค่อย ๆ เบาลง",
]
memories = [
    "วันที่คุยกันแล้วไม่อยากวางแชท",
    "วันที่งอนกันนิดหน่อย แต่สุดท้ายก็กลับมาคุย",
    "วันที่ธรรมดา แต่จำได้ชัด",
    "วันที่อยู่ด้วยแล้วสบายใจ",
    "วันที่รู้สึกว่าเธอสำคัญขึ้นเรื่อย ๆ",
]
cake_bases = ["ช็อกโกแลต", "วานิลลา", "สตรอว์เบอร์รี"]
cake_creams = ["ครีม", "ชมพู", "ฟ้า"]
cake_tops = ["เชอร์รี", "สตรอว์เบอร์รี", "หัวใจ"]
gift_lines = [
    "ขอให้วันนี้ใจดีกับเธอมาก ๆ",
    "ขอให้เธอมีรอยยิ้มเต็มวัน",
    "ขอให้เรื่องดี ๆ วิ่งเข้ามาหาเอง",
    "ขอให้วันเกิดปีนี้น่าจำมากที่สุด",
]
tiny_lines = [
    "เธอทำให้วันธรรมดาดีขึ้น",
    "บางทีแค่มีเธอก็พอแล้ว",
    "วันนี้ขอให้ยิ้มเยอะ ๆ",
    "ของขวัญชิ้นนี้ตั้งใจทำมาก",
    "ไม่ต้องเยอะ แต่ต้องจริงใจ",
    "ถ้าวันนี้พิเศษ ก็ให้เป็นเธอ",
]

if "page" not in st.session_state: st.session_state.page = "cover"
if "hearts" not in st.session_state: st.session_state.hearts = 0
if "candles" not in st.session_state: st.session_state.candles = 4
if "cake_base" not in st.session_state: st.session_state.cake_base = "วานิลลา"
if "cake_cream" not in st.session_state: st.session_state.cake_cream = "ครีม"
if "cake_top" not in st.session_state: st.session_state.cake_top = "เชอร์รี"
if "wish_idx" not in st.session_state: st.session_state.wish_idx = 0
if "memory_idx" not in st.session_state: st.session_state.memory_idx = 0
if "final_open" not in st.session_state: st.session_state.final_open = False
if "opened" not in st.session_state: st.session_state.opened = False
if "note_text" not in st.session_state: st.session_state.note_text = "สุขสันต์วันเกิดนะเธอ ขอให้วันนี้เป็นวันที่ดีมาก ๆ แล้วก็มีแต่เรื่องที่ชอบ"
if "game_stage" not in st.session_state: st.session_state.game_stage = 0
if "game_msg" not in st.session_state: st.session_state.game_msg = ""
if "target1" not in st.session_state: st.session_state.target1 = random.randint(0, 2)
if "target2" not in st.session_state: st.session_state.target2 = random.randint(0, 3)
if "target3" not in st.session_state: st.session_state.target3 = random.randint(0, 3)
if "map_pin" not in st.session_state: st.session_state.map_pin = 0

def go(page):
    st.session_state.page = page
    st.rerun()

def cake_svg(base, cream, top, candles):
    base_map = {"ช็อกโกแลต": "#8a5a49", "วานิลลา": "#e3c57f", "สตรอว์เบอร์รี": "#ff7fa8"}
    cream_map = {"ครีม": "#fff1c2", "ชมพู": "#ffd5e5", "ฟ้า": "#d9efff"}
    top_map = {"เชอร์รี": "🍒", "สตรอว์เบอร์รี": "🍓", "หัวใจ": "💖"}
    candle_parts = []
    cx0 = 255
    for i in range(candles):
        x = cx0 + i * 28
        candle_parts.append(f'<rect x="{x}" y="110" width="12" height="40" rx="6" fill="#fff"/>')
        candle_parts.append(f'<circle cx="{x+6}" cy="104" r="8" fill="#ffd65a"/>')
    flame = "".join(candle_parts)
    candle_line = " ".join(["🕯️"] * candles) if candles > 0 else "🎂 ✨ 🎂"
    drip = f"""
    <path d="M252 165
    C272 140, 286 188, 304 165
    C321 140, 337 188, 354 165
    C372 138, 389 188, 406 165
    C423 138, 439 188, 456 165
    C474 140, 490 188, 508 165
    L508 196 L252 196 Z" fill="{cream_map[cream]}"/>
    """
    return f"""
    <svg viewBox="0 0 760 470" width="100%" height="430" role="img" aria-label="birthday cake">
      <defs>
        <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#8a5e8f" flood-opacity="0.18"/>
        </filter>
        <linearGradient id="plateg" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#ffffff"/>
          <stop offset="100%" stop-color="#eadceb"/>
        </linearGradient>
      </defs>

      <ellipse cx="380" cy="390" rx="230" ry="28" fill="url(#plateg)"/>
      <ellipse cx="380" cy="368" rx="200" ry="20" fill="#d9c8dd" opacity="0.28"/>

      <g filter="url(#shadow)">
        <rect x="240" y="176" width="280" height="128" rx="30" fill="{base_map[base]}"/>
        <rect x="260" y="156" width="240" height="42" rx="20" fill="{cream_map[cream]}"/>
        {drip}
        <rect x="272" y="205" width="216" height="26" rx="13" fill="rgba(255,255,255,0.16)"/>
        <text x="380" y="145" text-anchor="middle" font-size="30">{top_map[top]}</text>
        <text x="380" y="100" text-anchor="middle" font-size="24">{candle_line}</text>
        {flame}
      </g>

      <circle cx="292" cy="236" r="6" fill="rgba(255,255,255,0.7)"/>
      <circle cx="336" cy="220" r="5" fill="rgba(255,255,255,0.7)"/>
      <circle cx="410" cy="230" r="6" fill="rgba(255,255,255,0.7)"/>
      <circle cx="452" cy="214" r="5" fill="rgba(255,255,255,0.7)"/>

      <text x="380" y="336" text-anchor="middle" font-size="18" fill="#6a3f73" font-weight="700">
        {base} • {cream} • {top}
      </text>
    </svg>
    """

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}
.stApp{
    background:
        radial-gradient(circle at 15% 10%, rgba(255, 181, 213, .55), transparent 22%),
        radial-gradient(circle at 85% 18%, rgba(185, 165, 255, .40), transparent 20%),
        radial-gradient(circle at 50% 90%, rgba(255, 220, 160, .28), transparent 26%),
        linear-gradient(135deg, #fdeaf1 0%, #f6efff 45%, #fff4df 100%);
    background-attachment: fixed;
}
.block-container{max-width:1200px;padding-top:1rem;padding-bottom:2rem;}
.box{
    background:rgba(255,255,255,.80);
    border:1px solid rgba(126,89,142,.10);
    border-radius:28px;
    box-shadow:0 18px 40px rgba(104,70,103,.10);
    padding:22px;
    backdrop-filter: blur(10px);
}
.hero{text-align:center;margin-bottom:16px;}
.badge{
    display:inline-block;padding:7px 14px;border-radius:999px;
    background:rgba(255,255,255,.85);border:1px solid rgba(126,89,142,.10);
    color:#8a5e8f;font-weight:800;font-size:.92rem;margin-bottom:12px;
}
.title{font-size:clamp(2.1rem,5vw,4rem);font-weight:900;margin:0;color:#5a345f;}
.sub{max-width:820px;margin:12px auto 0;color:#725b72;line-height:1.75;}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:16px;}
.mini{
    background:rgba(255,255,255,.80);border:1px solid rgba(126,89,142,.10);
    border-radius:22px;padding:16px;text-align:center;box-shadow:0 10px 24px rgba(104,70,103,.08);
}
.num{font-size:2rem;font-weight:900;color:#6a3f73;line-height:1;}
.label{margin-top:6px;color:#7b687b;font-size:.92rem;}
.line{height:1px;background:linear-gradient(90deg, transparent, rgba(126,89,142,.22), transparent);margin:16px 0;}
h2{margin:0 0 10px 0;color:#5a345f;font-size:1.25rem;}
p{margin:0;color:#725b72;line-height:1.7;}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;}
.chip{
    padding:8px 12px;border-radius:999px;background:linear-gradient(135deg, rgba(255,147,186,.24), rgba(176,124,255,.24));
    border:1px solid rgba(126,89,142,.10);color:#5f3966;font-weight:700;font-size:.92rem;
}
.glow{
    padding:18px;border-radius:24px;background:rgba(255,255,255,.80);
    border:1px solid rgba(126,89,142,.10);box-shadow:0 10px 22px rgba(104,70,103,.08);
}
.wishline{font-size:1.15rem;font-weight:900;color:#5a345f;line-height:1.6;text-align:center;}
.small{color:#725b72;line-height:1.65;font-size:.96rem;}
.cakewrap{
    background:rgba(255,255,255,.8);
    border:1px solid rgba(126,89,142,.10);
    border-radius:24px;
    box-shadow:0 10px 22px rgba(104,70,103,.08);
    padding:10px 12px 0 12px;
}
div.stButton > button{
    width:100%;border-radius:999px;border:0;padding:.82rem 1rem;
    background:linear-gradient(135deg,#ff7da8,#b07cff);color:white;font-weight:800;
    box-shadow:0 10px 24px rgba(94,60,97,.18);
}
.tabbtn div.stButton > button{margin-top:0}
</style>
""", unsafe_allow_html=True)

def nav():
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("🎂 เค้ก"): go("cake")
    with c2:
        if st.button("🎮 เกม"): go("game")
    with c3:
        if st.button("💌 อวยพร"): go("wish")
    with c4:
        if st.button("🎁 จบ"): go("final")

def top_stats():
    st.markdown(f"""
    <div class="grid3">
        <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิดถัดไป</div></div>
        <div class="mini"><div class="num">{days_together}</div><div class="label">วันที่เริ่มคบกัน</div></div>
        <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มที่เก็บได้</div></div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.page == "cover":
    st.markdown(f"""
    <div class="box hero">
        <div class="badge">🎁 Birthday Game</div>
        <div class="title">มีของให้เปิด</div>
        <div class="sub">กดเริ่ม แล้วค่อยเล่นทีละหน้า</div>
    </div>
    """, unsafe_allow_html=True)
    top_stats()
    if st.button("เริ่มเล่น"):
        st.session_state.page = "cake"
        st.session_state.hearts += 1
        st.rerun()
    st.stop()

st.markdown(f"""
<div class="box hero">
    <div class="badge">🎂 วันเกิดของเธอ</div>
    <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
    <div class="sub">เล่นง่าย ๆ ทีละหน้า แล้วค่อยเปิดของขวัญ</div>
</div>
""", unsafe_allow_html=True)
top_stats()
st.markdown('<div class="line"></div>', unsafe_allow_html=True)
nav()

if st.session_state.page == "cake":
    st.markdown('<div class="small">แต่งเค้กให้ถูกใจ แล้วกดเสิร์ฟ</div>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a:
        st.session_state.cake_base = st.selectbox("รส", cake_bases, index=cake_bases.index(st.session_state.cake_base))
    with b:
        st.session_state.cake_cream = st.selectbox("ครีม", cake_creams, index=cake_creams.index(st.session_state.cake_cream))
    with c:
        st.session_state.cake_top = st.selectbox("หน้าเค้ก", cake_tops, index=cake_tops.index(st.session_state.cake_top))
    st.session_state.candles = st.slider("เทียน", 0, 8, st.session_state.candles)
    st.markdown('<div class="cakewrap">', unsafe_allow_html=True)
    st.markdown(cake_svg(st.session_state.cake_base, st.session_state.cake_cream, st.session_state.cake_top, st.session_state.candles), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("สุ่มเค้ก"):
            st.session_state.cake_base = random.choice(cake_bases)
            st.session_state.cake_cream = random.choice(cake_creams)
            st.session_state.cake_top = random.choice(cake_tops)
            st.session_state.candles = random.randint(0, 8)
            st.session_state.hearts += 1
            st.rerun()
    with c2:
        if st.button("จุดเทียน"):
            st.session_state.candles = min(8, st.session_state.candles + 1)
            st.session_state.hearts += 1
            st.rerun()
    with c3:
        if st.button("เป่าเค้ก"):
            st.session_state.candles = 0
            st.session_state.hearts += 2
            st.balloons()
            st.rerun()

    st.markdown(f'<div class="glow"><div class="wishline">{random.choice(wishes)}</div><div class="small" style="text-align:center;margin-top:8px;">{random.choice(gift_lines)}</div></div>', unsafe_allow_html=True)

elif st.session_state.page == "game":
    st.markdown('<div class="small">เกมสั้น ๆ แต่เล่นได้หลายรอบ</div>', unsafe_allow_html=True)
    st.progress((st.session_state.game_stage + 1) / 4)

    if st.session_state.game_stage == 0:
        st.markdown(f'<div class="glow"><h3>ด่าน 1</h3><div class="small">{st.session_state.game_msg or "เลือกกล่องของขวัญ"}</div></div>', unsafe_allow_html=True)
        cols = st.columns(3)
        for i, col in enumerate(cols):
            with col:
                if st.button(f"🎁 {i+1}", key=f"g1_{i}"):
                    if i == st.session_state.target1:
                        st.session_state.game_stage = 1
                        st.session_state.game_msg = "เจอแล้ว"
                        st.session_state.hearts += 1
                        st.session_state.target2 = random.randint(0, 3)
                        st.rerun()
                    else:
                        st.session_state.game_msg = "ยังไม่ใช่"
                        st.rerun()

    elif st.session_state.game_stage == 1:
        st.markdown(f'<div class="glow"><h3>ด่าน 2</h3><div class="small">{st.session_state.game_msg or "เลือกหัวใจ"}</div></div>', unsafe_allow_html=True)
        opts = ["✨", "🎈", "🌷", "💖"]
        cols = st.columns(4)
        for i, col in enumerate(cols):
            with col:
                if st.button(opts[i], key=f"g2_{i}"):
                    if i == st.session_state.target2:
                        st.session_state.game_stage = 2
                        st.session_state.game_msg = "ใช่แล้ว"
                        st.session_state.hearts += 1
                        st.session_state.target3 = random.randint(0, 3)
                        st.rerun()
                    else:
                        st.session_state.game_msg = "ลองใหม่"
                        st.rerun()

    elif st.session_state.game_stage == 2:
        st.markdown(f'<div class="glow"><h3>ด่าน 3</h3><div class="small">{st.session_state.game_msg or "เลือกของหวานที่ใช่"}</div></div>', unsafe_allow_html=True)
        opts = ["🍰", "🎂", "🧁", "🍮"]
        cols = st.columns(4)
        for i, col in enumerate(cols):
            with col:
                if st.button(opts[i], key=f"g3_{i}"):
                    if i == st.session_state.target3:
                        st.session_state.game_stage = 3
                        st.session_state.game_msg = "ผ่านแล้ว"
                        st.session_state.hearts += 2
                        st.session_state.final_open = True
                        st.balloons()
                        st.rerun()
                    else:
                        st.session_state.game_msg = "ยังไม่ใช่"
                        st.rerun()

    else:
        st.markdown('<div class="glow"><h3>ผ่านครบแล้ว</h3><div class="small">ไปเปิดจดหมายได้</div></div>', unsafe_allow_html=True)
        if st.button("ไปต่อ"):
            go("wish")

elif st.session_state.page == "wish":
    if st.button("สุ่มคำอวยพร"):
        st.session_state.wish_idx = random.randint(0, len(wishes) - 1)
        st.session_state.hearts += 1
        st.rerun()

    st.markdown(f'<div class="glow"><div class="wishline">{wishes[st.session_state.wish_idx]}</div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="glow" style="margin-top:12px;"><div class="small">{random.choice(gift_lines)}</div></div>', unsafe_allow_html=True)

    name = st.text_input("ชื่อเล่น", value="ครีม")
    note = st.text_area("ข้อความถึงเธอ", value=st.session_state.note_text, height=110)
    st.session_state.note_text = note

    c1, c2 = st.columns(2)
    with c1:
        if st.button("เปิดจดหมาย"):
            st.session_state.final_open = True
            st.session_state.hearts += 2
            st.balloons()
            st.rerun()
    with c2:
        st.download_button("ดาวน์โหลดข้อความ", data=note, file_name="birthday_message.txt", mime="text/plain", use_container_width=True)

    if st.session_state.final_open:
        st.markdown(f'''
        <div class="box hero">
            <div class="badge">💌</div>
            <div class="title">สุขสันต์วันเกิดนะ {name} 🎂</div>
            <div class="sub">
                ขอให้วันนี้ยิ้มได้เยอะ ๆ<br>
                กินของอร่อยได้เต็มที่<br>
                แล้วก็มีแต่เรื่องดี ๆ เข้ามาแบบไม่ต้องเหนื่อยหาเอง
            </div>
        </div>
        ''', unsafe_allow_html=True)

elif st.session_state.page == "final":
    if st.button("เปิดของขวัญ"):
        st.session_state.final_open = True
        st.session_state.hearts += 3
        st.balloons()
        st.snow()
        st.rerun()

    if st.session_state.final_open:
        st.markdown(f'''
        <div class="box hero">
            <div class="badge">🎁 Final</div>
            <div class="title">สุขสันต์วันเกิดนะเธอ 🎂</div>
            <div class="sub">
                ขอให้วันนี้ดีแบบที่เธอไม่ต้องฝืนยิ้ม<br>
                ขอให้มีความสุขเยอะ ๆ แล้วก็จำได้ว่าตัวเองมีค่ามากแค่ไหน<br><br>
                วันเกิดปีนี้ ขอให้เป็นปีที่ใจดีกับเธอมาก ๆ
            </div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="grid3">
        <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มรวม</div></div>
        <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิด</div></div>
        <div class="mini"><div class="num">1</div><div class="label">คนสำคัญ</div></div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("เล่นใหม่"):
        st.session_state.page = "cover"
        st.session_state.hearts = 0
        st.session_state.candles = 4
        st.session_state.final_open = False
        st.session_state.opened = False
        st.session_state.game_stage = 0
        st.session_state.game_msg = ""
        st.session_state.target1 = random.randint(0, 2)
        st.session_state.target2 = random.randint(0, 3)
        st.session_state.target3 = random.randint(0, 3)
        st.session_state.wish_idx = 0
        st.session_state.memory_idx = 0
        st.rerun()
