import streamlit as st
from pathlib import Path

# -------------------- Logo Pfad --------------------
logo_path = (
    Path(__file__).parent.parent
    / "Images"
    / "studybuddy_logo.png"
)

# -------------------- Titel --------------------
st.markdown(
    """
    <div style="text-align:center; margin-top:20px;">

        <h1 style="
            font-size:70px;
            margin-bottom:0px;
            font-weight:800;
        ">
            Study<span style="color:#70cfc3;">Buddy</span>
        </h1>

        <h3 style="
            margin-top:10px;
            font-size:32px;
            font-weight:400;
        ">
            Dein persönlicher Lernplaner
        </h3>

    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- Abstand --------------------
st.markdown("<br>", unsafe_allow_html=True)

# -------------------- Logo anzeigen --------------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        str(logo_path),
        use_container_width=True
    )

# -------------------- Abstand --------------------
st.markdown("<br>", unsafe_allow_html=True)

# -------------------- Projektbeschreibung --------------------
st.write(
    "StudyBuddy wurde entwickelt, um Schülerinnen und Schüler "
    "bei der Organisation ihres Lernalltags zu unterstützen. "
    "Viele Lernende verlieren im Schulalltag schnell den Überblick "
    "über Aufgaben, Prüfungen und Lernzeiten. "
    "Die App soll dabei helfen, den Alltag strukturierter, "
    "übersichtlicher und stressfreier zu gestalten."
)

# -------------------- Abstand --------------------
st.markdown("<br>", unsafe_allow_html=True)

# -------------------- Entwicklerteam --------------------
st.subheader("Entwicklerteam")

st.markdown(
    """
- Danijel Antic  
  anticdan@students.zhaw.ch

- Eliah Diener  
  dieneeli@students.zhaw.ch

- Harini Murugadas  
  murughar@students.zhaw.ch

- Alexandra Vlk  
  vlkale01@students.zhaw.ch
"""
)




