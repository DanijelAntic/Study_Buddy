import streamlit as st
from utils.data_manager import DataManager

st.set_page_config(
    page_title="StudyBuddy",
    page_icon=":material/home:",
    layout="wide"
)

# ZUERST username setzen
if "username" not in st.session_state:
    st.session_state["username"] = "studybuddy"

# DANACH WebDAV verbinden
if "data_manager" not in st.session_state:
    DataManager(fs_protocol="webdav")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_uebersicht = st.Page("views/uebersicht.py", title="Übersicht", icon=":material/info:")
pg_to_do = st.Page("views/to_do.py", title="To-Do")
pg_wochenplaner = st.Page("views/wochenplaner.py", title="Wochenplaner")
pg_pruefungsplaner = st.Page("views/pruefungsplaner.py", title="Prüfungsplaner")
pg_noteneintrag = st.Page("views/noteneintrag.py", title="Noteneintrag")
pg_timer = st.Page("views/timer.py", title="Timer")

pg = st.navigation([
    pg_home,
    pg_uebersicht,
    pg_to_do,
    pg_wochenplaner,
    pg_pruefungsplaner,
    pg_noteneintrag,
    pg_timer
])

pg.run()