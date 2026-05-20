import streamlit as st


# -------------------- Titel --------------------
st.markdown(
    "<h1 style='text-align: center;'>StudyBuddy</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>Dein persönlicher Lernplaner</h3>",
    unsafe_allow_html=True
)


# -------------------- Logo --------------------
col1, col2, col3 = st.columns([0.9, 1, 0.8])

with col2:
    st.image(
        "Images/studybuddy_logo.png",
        width=260
    )


# -------------------- Beschreibung --------------------
st.write(
    "StudyBuddy wurde entwickelt, um Schülerinnen und Schüler "
    "bei der Organisation ihres Lernalltags zu unterstützen. "
    "Viele Lernende verlieren im Schulalltag schnell den Überblick "
    "über Aufgaben, Prüfungen und Lernzeiten."
)

st.write(
    "Die App hilft dabei, den Alltag strukturierter, "
    "übersichtlicher und stressfreier zu gestalten."
)


# -------------------- Entwicklerteam --------------------
st.write("Diese App wurde von folgenden Personen entwickelt:")

st.markdown(
    """
- Danijel Antic ([anticdan@students.zhaw.ch](mailto:anticdan@students.zhaw.ch))

- Eliah Diener ([dieneeli@students.zhaw.ch](mailto:dieneeli@students.zhaw.ch))

- Harini Murugadas ([murughar@students.zhaw.ch](mailto:murughar@students.zhaw.ch))

- Alexandra Vlk ([vlkale01@students.zhaw.ch](mailto:vlkale01@students.zhaw.ch))
"""
)

