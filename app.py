import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_second = st.Page("views/unterseite_a.py", title="Unterseite A", icon=":material/info:")
pg_To_Do = st.Page("views/To_Do.py", title="To-Do") #icon=":white_check_mark:"
pg_Wochenplaner = st.Page("views/Wochenplaner.py", title="Wochenplaner") #icon=":spiral_calendar_pad:"
pg_Prüfungsplaner = st.Page("views/Prüfungsplaner.py", title="Prüfungsplaner") #icon=":spiral_calendar_pad:"
pg_Noteneintrag = st.Page("views/Noteneintrag.py", title="Noteneintrag") #icon=":spiral_calendar_pad:"
pg_Timer = st.Page("views/Timer.py", title="Timer") #icon=":spiral_calendar_pad:"

pg = st.navigation([pg_home, pg_second, pg_To_Do, pg_Wochenplaner, pg_Prüfungsplaner, pg_Noteneintrag, pg_Timer])
pg.run()
