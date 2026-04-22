import streamlit as st
import time

# Initialisiere Session-State für den Timer
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
    st.session_state.running = False

st.title("Timer - Stoppuhr")

# Buttons zum Starten und Stoppen
col1, col2 = st.columns(2)
with col1:
    if st.button("Start"):
        st.session_state.start_time = time.time()
        st.session_state.running = True

with col2:
    if st.button("Stop"):
        st.session_state.running = False

# Zeige die Zeit an
if st.session_state.running and st.session_state.start_time:
    elapsed_time = time.time() - st.session_state.start_time
    st.write(f"Laufende Zeit: {elapsed_time:.2f} Sekunden")
elif st.session_state.start_time:
    elapsed_time = time.time() - st.session_state.start_time
    st.write(f"Gestoppte Zeit: {elapsed_time:.2f} Sekunden")
else:
    st.write("Timer bereit zum Starten.")