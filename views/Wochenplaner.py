import streamlit as st
import pandas as pd
import altair as alt
from datetime import date, timedelta

st.set_page_config(layout="wide")

st.title("Wochenplaner")
st.write("Plane deinen Wochenablauf mit diesem interaktiven Kalender.")

# -------------------- Woche auswählen --------------------
heute = date.today()

ausgewaehltes_datum = st.date_input(
    "Woche auswählen",
    value=heute
)

wochen_start = ausgewaehltes_datum - timedelta(days=ausgewaehltes_datum.weekday())
wochen_ende = wochen_start + timedelta(days=6)

st.info(
    f"Woche vom {wochen_start.strftime('%d.%m.%Y')} "
    f"bis {wochen_ende.strftime('%d.%m.%Y')}"
)

# -------------------- Tage & Zeiten --------------------
tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

zeiten = [
    f"{i:02d}:00-{(i + 1) % 24:02d}:00"
    for i in range(6, 24)
]

# -------------------- Aktivitäten --------------------
optionen = [
    "Leer",
    "Schule",
    "Lernen",
    "Sport",
    "Arbeit",
    "Freizeit",
    "Schlafen"
]

# -------------------- Farben --------------------
farben = {
    "Leer": "#F2F2F2",
    "Schule": "#BBD7FF",
    "Lernen": "#D8C8FF",
    "Sport": "#C8F7C5",
    "Arbeit": "#FFB3B3",
    "Freizeit": "#FFF3A3",
    "Schlafen": "#D9D9D9"
}

# -------------------- Session State --------------------
if "wochenplan" not in st.session_state:
    st.session_state["wochenplan"] = {
        tag: {zeit: "Leer" for zeit in zeiten}
        for tag in tage
    }

# -------------------- Legende --------------------
st.subheader("Legende")

leg_cols = st.columns(4)

for i, name in enumerate(optionen):
    with leg_cols[i % 4]:
        st.markdown(
            f"""
            <div style="
                background-color: {farben[name]};
                padding: 10px;
                border-radius: 10px;
                text-align: center;
                font-weight: bold;
                margin-bottom: 8px;
            ">
                {name}
            </div>
            """,
            unsafe_allow_html=True
        )

st.caption("Leer = Erholung, Essen, Duschen, freie Zeit oder nichts geplant")

# -------------------- Tabelle --------------------
st.divider()
st.subheader("Wochenübersicht")

header_cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1])

with header_cols[0]:
    st.markdown("**Zeit**")

for i, tag in enumerate(tage):
    with header_cols[i + 1]:
        st.markdown(f"**{tag}**")

for zeit in zeiten:
    row_cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1])

    with row_cols[0]:
        st.markdown(f"**{zeit}**")

    for i, tag in enumerate(tage):
        with row_cols[i + 1]:
            aktueller_wert = st.session_state["wochenplan"][tag][zeit]

            auswahl = st.selectbox(
                label=f"{tag} {zeit}",
                options=optionen,
                index=optionen.index(aktueller_wert),
                key=f"{tag}_{zeit}",
                label_visibility="collapsed"
            )

            st.session_state["wochenplan"][tag][zeit] = auswahl

# -------------------- Buttons --------------------
st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("Plan speichern"):
        st.success("Wochenplan wurde gespeichert.")

with col2:
    if st.button("Clear"):
        st.session_state["wochenplan"] = {
            tag: {zeit: "Leer" for zeit in zeiten}
            for tag in tage
        }
        st.rerun()

# -------------------- Grafik --------------------
st.divider()
st.subheader("Grafische Wochenübersicht")

aktivitaeten = []

for tag in tage:
    for zeit in zeiten:
        aktivitaeten.append(st.session_state["wochenplan"][tag][zeit])

grafik_df = pd.DataFrame({"Aktivität": aktivitaeten})

stunden_df = grafik_df["Aktivität"].value_counts().reset_index()
stunden_df.columns = ["Aktivität", "Stunden"]

chart = alt.Chart(stunden_df).mark_bar().encode(
    x=alt.X("Aktivität:N", title="Aktivität"),
    y=alt.Y("Stunden:Q", title="Anzahl Stunden pro Woche"),
    color=alt.Color(
        "Aktivität:N",
        scale=alt.Scale(
            domain=list(farben.keys()),
            range=list(farben.values())
        ),
        legend=None
    ),
    tooltip=[
        alt.Tooltip("Aktivität:N"),
        alt.Tooltip("Stunden:Q")
    ]
)

st.altair_chart(
    chart,
    use_container_width=True
)

st.caption(
    "Die Grafik zeigt, wie viele Stunden pro Aktivität in der Woche eingeplant sind."
)