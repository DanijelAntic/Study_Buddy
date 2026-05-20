import streamlit as st
from utils.data_manager import DataManager

# -------------------- Seitenlayout --------------------
st.set_page_config(
    page_title="StudyBuddy",
    page_icon=":material/home:",
    layout="wide"
)

# -------------------- Benutzername --------------------
st.session_state["username"] = "studybuddy"

# -------------------- Alten DataManager löschen --------------------
if "data_manager" in st.session_state:
    del st.session_state["data_manager"]

# -------------------- SWITCHdrive Verbindung --------------------
DataManager(
    fs_protocol="webdav",
    fs_root_folder="StudyBuddy"
)

# -------------------- INFO TEST --------------------
st.write(
    st.session_state["data_manager"].info()
)

# -------------------- Seiten --------------------
pg_home = st.Page(
    "views/home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

pg_uebersicht = st.Page(
    "views/uebersicht.py",
    title="Übersicht",
    icon=":material/info:"
)

pg_to_do = st.Page(
    "views/to_do.py",
    title="To-Do"
)

pg_wochenplaner = st.Page(
    "views/wochenplaner.py",
    title="Wochenplaner"
)

pg_pruefungsplaner = st.Page(
    "views/pruefungsplaner.py",
    title="Prüfungsplaner"
)

pg_noteneintrag = st.Page(
    "views/noteneintrag.py",
    title="Noteneintrag"
)

pg_timer = st.Page(
    "views/timer.py",
    title="Timer"
)

# -------------------- Navigation --------------------
pg = st.navigation([
    pg_home,
    pg_uebersicht,
    pg_to_do,
    pg_wochenplaner,
    pg_pruefungsplaner,
    pg_noteneintrag,
    pg_timer
])

