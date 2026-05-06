import streamlit as st
import time

st.title("Fokus Modus")

# -------------------- CSS --------------------
st.markdown("""
<style>

/* Allgemeine Button-Styles */
.stButton > button {
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
    width: 100%;
    font-size: 18px;
}

/* START = Blau */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
    background-color: #BBD7FF;
    color: black;
}

/* PAUSE = Orange */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
    background-color: #FFD6A5;
    color: black;
}

/* RESET = Rot */
div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {
    background-color: #FFB3B3;
    color: black;
}

</style>
""", unsafe_allow_html=True)

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
    max_value=180,
    value=25
)

# Nur setzen wenn Timer nicht läuft
if (
    not st.session_state["timer_running"]
    and not st.session_state["timer_paused"]
):
    st.session_state["remaining_time"] = minuten * 60

# -------------------- Anzeige --------------------
minutes = st.session_state["remaining_time"] // 60
seconds = st.session_state["remaining_time"] % 60

st.markdown(
    f"""
    <div style="
        font-size:90px;
        text-align:center;
        border:5px solid black;
        padding:40px;
        border-radius:20px;
        margin-top:40px;
        margin-bottom:40px;
    ">
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

# -------------------- Weiter Button --------------------
if st.session_state["timer_paused"]:

    st.markdown("""
    <style>
    div.stButton button[kind="secondary"] {
        background-color: #C8F7C5;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

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

# -------------------- Hinweis --------------------
st.info(
    "Nach einer Fokusphase ist eine 10 Minuten Pause empfohlen."
)