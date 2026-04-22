import streamlit as st
import time

# Initialisiere Session-State für den Timer
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
    st.session_state.running = False

st.title("Timer - Stoppuhr")

# Buttons zum Starten, Stoppen und Aktualisieren
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Start"):
        st.session_state.start_time = time.time()
        st.session_state.running = True

with col2:
    if st.button("Stop"):
        st.session_state.running = False

with col3:
    if st.button("Aktualisieren"):
        pass  # Button triggert ein Rerun der Seite, um die Zeit neu zu berechnen

# Zeige die Zeit an (immer, wenn eine Startzeit gesetzt ist)
if st.session_state.start_time:
    elapsed_time = time.time() - st.session_state.start_time
    if st.session_state.running:
        st.write(f"Laufende Zeit: {elapsed_time:.2f} Sekunden")
    else:
        st.write(f"Gestoppte Zeit: {elapsed_time:.2f} Sekunden")
else:
    st.write("Timer bereit zum Starten.")