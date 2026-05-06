import streamlit as st
import time

st.title("Timer")
st.subheader("Fokus Modus")


# -------------------- Session State --------------------
if "timer_running" not in st.session_state:
    st.session_state["timer_running"] = False

if "timer_paused" not in st.session_state:
    st.session_state["timer_paused"] = False

if "remaining_time" not in st.session_state:
    st.session_state["remaining_time"] = 25 * 60


# -------------------- Zeit einstellen --------------------
minuten = st.number_input(
    "Zeit einstellen in Minuten",
    min_value=1,
    max_value=120,
    value=25
)

# Zeit nur neu setzen, wenn Timer nicht läuft und nicht pausiert ist
if not st.session_state["timer_running"] and not st.session_state["timer_paused"]:
    st.session_state["remaining_time"] = minuten * 60


# -------------------- Timer Anzeige --------------------
minutes = st.session_state["remaining_time"] // 60
seconds = st.session_state["remaining_time"] % 60

st.markdown(
    f"""
    <div style="
        font-size:70px;
        text-align:center;
        border:4px solid black;
        padding:25px;
        border-radius:15px;
        margin:30px;">
        {minutes:02d}:{seconds:02d}
    </div>
    """,
    unsafe_allow_html=True
)


# -------------------- Buttons --------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Start"):
        st.session_state["timer_running"] = True
        st.session_state["timer_paused"] = False

with col2:
    if st.button("Pause"):
        st.session_state["timer_running"] = False
        st.session_state["timer_paused"] = True

with col3:
    if st.button("Reset"):
        st.session_state["timer_running"] = False
        st.session_state["timer_paused"] = False
        st.session_state["remaining_time"] = minuten * 60
        st.rerun()


# Weiter-Button erscheint nur nach Pause
if st.session_state["timer_paused"]:
    if st.button("Weiter"):
        st.session_state["timer_running"] = True
        st.session_state["timer_paused"] = False
        st.rerun()


# -------------------- Timer läuft --------------------
if st.session_state["timer_running"]:
    if st.session_state["remaining_time"] > 0:
        time.sleep(1)
        st.session_state["remaining_time"] -= 1
        st.rerun()
    else:
        st.session_state["timer_running"] = False
        st.session_state["timer_paused"] = False
        st.success("Zeit ist abgelaufen! Mach eine 10 Minuten Pause.")
        st.balloons()


st.info("Nach einer Fokusphase ist eine 10 Minuten Pause empfohlen.")