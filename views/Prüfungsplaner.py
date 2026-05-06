import streamlit as st
import pandas as pd
from datetime import date

st.title("Prüfungsplaner")

if "exams_df" not in st.session_state:
    st.session_state["exams_df"] = pd.DataFrame(
        columns=["Fach", "Datum", "Bemerkung", "Tage bis Prüfung"]
    )

with st.form("exam_form", clear_on_submit=True):
    fach = st.text_input("Fach", placeholder="z.B. Biologie")
    pruefungsdatum = st.date_input("Datum")
    bemerkung = st.text_area("Bemerkung", placeholder="z.B. Buch S. 10–25 lernen")

    col1, col2 = st.columns(2)

    with col1:
        speichern = st.form_submit_button("Speichern")

    with col2:
        clear = st.form_submit_button("Clear")

if speichern:
    if fach.strip() == "":
        st.warning("Bitte ein Fach eingeben.")
    else:
        tage = (pruefungsdatum - date.today()).days

        neue_pruefung = pd.DataFrame([{
            "Fach": fach,
            "Datum": pruefungsdatum.strftime("%d.%m.%Y"),
            "Bemerkung": bemerkung,
            "Tage bis Prüfung": tage
        }])

        st.session_state["exams_df"] = pd.concat(
            [st.session_state["exams_df"], neue_pruefung],
            ignore_index=True
        )

        st.success("Prüfung wurde gespeichert.")

if clear:
    st.session_state["exams_df"] = pd.DataFrame(
        columns=["Fach", "Datum", "Bemerkung", "Tage bis Prüfung"]
    )
    st.rerun()

st.subheader("Meine Prüfungen")

if not st.session_state["exams_df"].empty:
    st.dataframe(st.session_state["exams_df"], use_container_width=True)

    for _, row in st.session_state["exams_df"].iterrows():
        tage = int(row["Tage bis Prüfung"])

        if tage < 0:
            st.info(f"Die Prüfung in {row['Fach']} ist bereits vorbei.")
        elif tage == 0:
            st.error(f"Heute ist deine Prüfung in {row['Fach']}!")
            st.toast(f"Heute Prüfung: {row['Fach']}", icon="⚠️")
        elif tage <= 3:
            st.warning(f"Achtung: {row['Fach']} ist in {tage} Tagen!")
            st.toast(f"{row['Fach']} ist bald!", icon="⏰")
        elif tage <= 7:
            st.info(f"{row['Fach']} ist in {tage} Tagen.")
else:
    st.info("Noch keine Prüfungen gespeichert.")
    