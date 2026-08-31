import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state (จุดที่ 1)
for key in ["ans1_val", "ans2_val", "ans3_val", "ans4_val"]:
    if key not in st.session_state:
        st.session_state[key] = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่ (จุดที่ 2)
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog) - อ่านค่าจาก session_state ตรงๆ
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog():
    st.balloons()
    score = 0

    # (จุดที่ 3) แปลงคำตอบเป็นตัวพิมพ์เล็ก
    u_ans1 = st.session_state.ans1_val.strip().lower()
    u_ans2 = st.session_state.ans2_val.strip().lower()
    u_ans3 = st.session_state.ans3_val.strip().lower()
    u_ans4 = st.session_state.ans4_val.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # (จุดที่ 4) ตรวจข้อ 3 และข้อ 4 (Gift 🎁)
    if u_ans3 == "gift":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "box":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    # (จุดที่ 5) ปรับคะแนนเต็มเป็น 4
    if score == 4:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (จุดที่ 6 - เพิ่มข้อ 3 และ 4 เรื่อง Gift)
ans1 = st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: I got a special `g _ f t` for my birthday. 🎁",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: Open the gift `b _ x` to see your surprise. 📦",
    value=st.session_state.ans4_val,
)

# (จุดที่ 7) อัปเดตค่าเข้า session_state
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 4. ปุ่มส่งคำตอบ (ลบ time.sleep(1) ออกเพื่อแก้ TypeError)
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

# 5. แสดง Dialog ผลลัพธ์ (จุดที่ 8 - เรียกใช้งานแบบไม่มี parameter)
if st.session_state.get("is_ended", False):
    show_result_dialog()

st.divider()
st.write("นายธีร์ธวัช เพ็ชรพงษ์ เลขที่ 29 ม.4/14")
