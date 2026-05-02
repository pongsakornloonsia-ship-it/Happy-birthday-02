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

if "page" not in st.session_state:
    st.session_state.page = "cover"
if "candles" not in st.session_state:
    st.session_state.candles = 3
if "cake" not in st.session_state:
    st.session_state.cake = {"base": "วานิลลา", "cream": "ครีม", "top": "เชอร์รี"}
if "step" not in st.session_state:
    st.session_state.step = 0
if "clues" not in st.session_state:
    st.session_state.clues = 0
if "wish_idx" not in st.session_state:
    st.session_state.wish_idx = 0
if "opened" not in st.session_state:
    st.session_state.opened = False
if "hearts" not in st.session_state:
    st.session_state.hearts = 0

wishes = [
    "สุขสันต์วันเกิดนะเธอ 🎂",
    "ขอให้วันนี้ยิ้มได้ทั้งวัน",
    "ขอให้ปีนี้ใจดีกับเธอมาก ๆ",
    "กินของอร่อยให้เต็มที่เลย",
    "ขอให้ทุกอย่างที่เหนื่อย ค่อย ๆ เบาลง",
]
cake_bases = ["ช็อกโกแลต", "วานิลลา", "สตรอว์เบอร์รี"]
cake_creams = ["ครีม", "ชมพู", "ฟ้า"]
cake_tops = ["เชอร์รี", "สตรอว์เบอร์รี", "หัวใจ"]

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
    background:rgba(255,255,255,.78);
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
.cake-stage{
    position:relative;width:100%;min-height:380px;display:flex;align-items:flex-end;justify-content:center;overflow:hidden;
}
.plate{
    position:absolute;bottom:20px;width:min(560px,94%);height:36px;border-radius:999px;
    background:linear-gradient(180deg,#fff,#ebdeef);box-shadow:0 12px 24px rgba(97,71,102,.12);
}
.cake{position:relative;width:min(420px,92vw);height:320px;}
.layer{
    position:absolute;left:50%;transform:translateX(-50%);border-radius:28px 28px 18px 18px;box-shadow:0 12px 24px rgba(97,71,102,.18);
}
.bottom{bottom:36px;width:280px;height:110px;background:var(--base);}
.mid{bottom:128px;width:246px;height:84px;background:var(--base);}
.top{bottom:198px;width:212px;height:66px;background:var(--base);}
.frost{
    position:absolute;bottom:240px;left:50%;transform:translateX(-50%);
    width:226px;height:40px;border-radius:22px 22px 14px 14px;background:var(--cream);
}
.candles{
    position:absolute;bottom:286px;left:50%;transform:translateX(-50%);
    font-size:1.4rem;letter-spacing:3px;white-space:nowrap;color:#5a345f;
}
.topper{
    position:absolute;bottom:256px;left:50%;transform:translateX(-50%);font-size:2rem;
}
.labelcake{
    position:absolute;bottom:8px;left:50%;transform:translateX(-50%);
    color:#6a3f73;font-weight:800;font-size:.96rem;white-space:nowrap;
}
.card{
    background:rgba(255,255,255,.80);border:1px solid rgba(126,89,142,.10);border-radius:24px;
    box-shadow:0 10px 22px rgba(104,70,103,.08);padding:16px;height:100%;
}
.small{color:#725b72;line-height:1.65;font-size:.96rem;}
div.stButton > button{
    width:100%;border-radius:999px;border:0;padding:.82rem 1rem;
    background:linear-gradient(135deg,#ff7da8,#b07cff);color:white;font-weight:800;
    box-shadow:0 10px 24px rgba(94,60,97,.18);
}
.tabbtn div.stButton > button{margin-top:0}
.hint{font-size:.94rem;color:#7b687b;}
</style>
""", unsafe_allow_html=True)

def cake_html():
    colors = {
        "ช็อกโกแลต": "#8d5a48",
        "วานิลลา": "#e2c38b",
        "สตรอว์เบอร์รี": "#ff86aa",
    }
    creams = {"ครีม": "#fff1c2", "ชมพู": "#ffd1e2", "ฟ้า": "#d6efff"}
    tops = {"เชอร์รี": "🍒", "สตรอว์เบอร์รี": "🍓", "หัวใจ": "💖"}
    candle_line = " ".join(["🕯️"] * st.session_state.candles) if st.session_state.candles > 0 else "🎂 ✨ 🎂"
    return f"""
    <div class="cake-stage">
        <div class="plate"></div>
        <div class="cake" style="--base:{colors[st.session_state.cake['base']]};--cream:{creams[st.session_state.cake['cream']]}">
            <div class="candles">{candle_line}</div>
            <div class="topper">{tops[st.session_state.cake['top']]}</div>
            <div class="layer top"></div>
            <div class="layer mid"></div>
            <div class="layer bottom"></div>
            <div class="frost"></div>
            <div class="labelcake">{st.session_state.cake['base']} • {st.session_state.cake['cream']} • {st.session_state.cake['top']}</div>
        </div>
    </div>
    """

def open_page(page):
    st.session_state.page = page

if st.session_state.page == "cover":
    st.markdown(f"""
    <div class="box hero">
        <div class="badge">🎁 Birthday Game</div>
        <div class="title">มีของให้เปิด</div>
        <div class="sub">กดเริ่ม แล้วเล่นไปทีละหน้าจอ</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="grid3">
        <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิด</div></div>
        <div class="mini"><div class="num">{days_together}</div><div class="label">วันที่เริ่มคบ</div></div>
        <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มที่เก็บได้</div></div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("เริ่มเล่น"):
        st.session_state.page = "cake"
        st.session_state.hearts += 1
        st.rerun()

    st.stop()

st.markdown(f"""
<div class="box hero">
    <div class="badge">🎂 วันเกิดของเธอ</div>
    <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
    <div class="sub">เล่นง่าย ๆ ทีละด่าน แล้วค่อยเปิดของขวัญ</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="grid3">
    <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิดถัดไป</div></div>
    <div class="mini"><div class="num">{days_together}</div><div class="label">วันที่เริ่มคบ</div></div>
    <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มทั้งหมด</div></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="line"></div>', unsafe_allow_html=True)

tabs = st.tabs(["🎂 เค้ก", "🎮 เกม", "💌 อวยพร", "🎁 จบ"])

with tabs[0]:
    st.markdown('<div class="small">แต่งเค้กให้ถูกใจ แล้วกดเสิร์ฟ</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.session_state.cake["base"] = st.selectbox("รส", cake_bases, index=cake_bases.index(st.session_state.cake["base"]))
    with c2:
        st.session_state.cake["cream"] = st.selectbox("ครีม", cake_creams, index=cake_creams.index(st.session_state.cake["cream"]))
    with c3:
        st.session_state.cake["top"] = st.selectbox("หน้าเค้ก", cake_tops, index=cake_tops.index(st.session_state.cake["top"]))

    st.session_state.candles = st.slider("เทียน", 0, 8, st.session_state.candles)
    st.markdown(cake_html(), unsafe_allow_html=True)

    if st.button("สุ่มเค้ก"):
        st.session_state.cake["base"] = random.choice(cake_bases)
        st.session_state.cake["cream"] = random.choice(cake_creams)
        st.session_state.cake["top"] = random.choice(cake_tops)
        st.session_state.candles = random.randint(0, 8)
        st.session_state.hearts += 1
        st.rerun()

    if st.button("เสิร์ฟเค้ก"):
        st.session_state.hearts += 2
        st.session_state.wish_idx = random.randint(0, len(wishes) - 1)
        st.balloons()
        st.session_state.page = "game"
        st.rerun()

with tabs[1]:
    st.markdown('<div class="small">เกมสั้น ๆ ไม่ยาก แต่เล่นได้หลายรอบ</div>', unsafe_allow_html=True)
    st.session_state.step = st.select_slider("ด่าน", options=[1, 2, 3], value=st.session_state.step or 1)
    if st.session_state.step == 1:
        st.write("เลือกกล่องที่คิดว่าใช่")
        cols = st.columns(3)
        pick = None
        for i, col in enumerate(cols, start=1):
            with col:
                if st.button(f"🎁 {i}", key=f"box{i}"):
                    pick = i
        target = 2
        if pick is not None:
            if pick == target:
                st.success("เจอแล้ว!")
                st.session_state.clues += 1
                st.session_state.hearts += 1
            else:
                st.info("ลองอีกใบ")
    elif st.session_state.step == 2:
        st.write("จับคู่รูปแบบ")
        choice = st.radio("อันไหนเป็นหัวใจ", ["✨", "🎈", "💖"], horizontal=True)
        if st.button("เช็ก"):
            if choice == "💖":
                st.success("ถูกแล้ว")
                st.session_state.clues += 1
                st.session_state.hearts += 1
            else:
                st.warning("ยังไม่ใช่")
    else:
        st.write("กดให้ครบ 5 ครั้ง")
        if st.button("กด"):
            st.session_state.clues += 1
            st.session_state.hearts += 1
        st.write(f"แต้ม: {st.session_state.clues}/5")

    if st.button("ไปต่อ"):
        st.session_state.page = "wish"
        st.rerun()

with tabs[2]:
    if st.button("สุ่มคำอวยพร"):
        st.session_state.wish_idx = random.randint(0, len(wishes) - 1)
        st.session_state.hearts += 1

    st.markdown(f"""
    <div class="card">
        <div class="wishline">{wishes[st.session_state.wish_idx]}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="small">ข้อความสั้น ๆ ที่อยากให้จำ</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card">
        <div class="small">{random.choice(gift_notes)}</div>
    </div>
    """, unsafe_allow_html=True)

    note = st.text_input("เขียนชื่อเล่น", value="ครีม")
    msg = st.text_area("ข้อความถึงเธอ", value="สุขสันต์วันเกิดนะเธอ ขอให้วันนี้เป็นวันที่ดีมาก ๆ", height=110)
    if st.button("เปิดข้อความ"):
        st.session_state.opened = True
        st.balloons()
        st.session_state.hearts += 2

    if st.session_state.opened:
        st.markdown(f"""
        <div class="final">
            <h2>สุขสันต์วันเกิดนะ {note} 🎂</h2>
            <p>{msg}<br><br>ขอให้วันนี้ยิ้มได้เยอะ ๆ แล้วก็มีแต่เรื่องที่ชอบ</p>
        </div>
        """, unsafe_allow_html=True)

with tabs[3]:
    if st.button("เปิดของขวัญ"):
        st.session_state.final_open = True
        st.session_state.hearts += 3
        st.balloons()
        st.snow()

    if st.session_state.final_open:
        st.markdown(f"""
        <div class="final">
            <h2>สุขสันต์วันเกิดนะเธอ 🎁</h2>
            <p>
                ขอให้วันนี้ดีแบบที่เธอไม่ต้องฝืนยิ้ม<br>
                ขอให้มีความสุขเยอะ ๆ แล้วก็จำได้ว่าตัวเองมีค่ามากแค่ไหน<br><br>
                วันเกิดปีนี้ ขอให้เป็นปีที่ใจดีกับเธอมาก ๆ
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="grid3">
        <div class="mini"><div class="num">{st.session_state.hearts}</div><div class="label">แต้มรวม</div></div>
        <div class="mini"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิด</div></div>
        <div class="mini"><div class="num">1</div><div class="label">คนสำคัญ</div></div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.page != "cover":
    st.markdown("<div class='small'>กดแท็บด้านบนเพื่อสลับหน้าจอ</div>", unsafe_allow_html=True)
