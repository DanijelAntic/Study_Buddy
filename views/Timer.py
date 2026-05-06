import streamlit as st
import time

st.title("Timer")
st.subheader("Fokus Modus")

if "timer_running" not in st.session_state:
    st.session_state["timer_running"] = False

if "remaining_time" not in st.session_state:
    st.session_state["remaining_time"] = 25 * 60

minuten = st.number_input(
    "Zeit einstellen in Minuten",
    min_value=1,
    max_value=120,
    value=25
)

if not st.session_state["timer_running"]:
    st.session_state["remaining_time"] = minuten * 60

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

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Start"):
        st.session_state["timer_running"] = True

with col2:
    if st.button("Pause"):
        st.session_state["timer_running"] = False

with col3:
    if st.button("Reset"):
        st.session_state["timer_running"] = False
        st.session_state["remaining_time"] = minuten * 60
        st.rerun()

if st.session_state["timer_running"]:
    if st.session_state["remaining_time"] > 0:
        time.sleep(1)
        st.session_state["remaining_time"] -= 1
        st.rerun()
    else:
        st.session_state["timer_running"] = False
        st.success("Zeit ist abgelaufen! Mach eine 10 Minuten Pause.")
        st.balloons()

st.info("Nach einer Fokusphase ist eine 10 Minuten Pause empfohlen.")