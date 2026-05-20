import streamlit as st
import pandas as pd
from datetime import date

from utils.style import page_title
from utils.data_manager import DataManager


# -------------------- Titel --------------------
page_title("Prüfungsplaner")

st.write(
    "Plane deine Prüfungen übersichtlich und behalte wichtige "
    "Termine und Vorbereitungen im Blick."
)


# -------------------- Daten laden --------------------
if "exams_df" not in st.session_state:

    data_manager = DataManager()

    exams_df = data_manager.load_user_data(
        "pruefungen.csv",
        pd.DataFrame()
    )

    if not exams_df.empty:

        st.session_state["exams_df"] = exams_df

    else:

        st.session_state["exams_df"] = pd.DataFrame(
            columns=[
                "Fach",
                "Datum",
                "Bemerkung",
                "Tage bis Prüfung"
            ]
        )


# -------------------- Formular --------------------
with st.form("exam_form", clear_on_submit=True):

    fach = st.text_input(
        "Fach",
        placeholder="z.B. Biologie"
    )

    pruefungsdatum = st.date_input(
        "Datum"
    )

    bemerkung = st.text_area(
        "Bemerkung",
        placeholder="z.B. Buch S. 10–25 lernen"
    )

    col1, col2 = st.columns(2)

    with col1:
        speichern = st.form_submit_button("Speichern")

    with col2:
        clear = st.form_submit_button("Clear")


# -------------------- Speichern --------------------
if speichern:

    if fach.strip() == "":

        st.warning("Bitte ein Fach eingeben.")

    else:

        tage = (
            pruefungsdatum - date.today()
        ).days

        neue_pruefung = pd.DataFrame([
            {
                "Fach": fach.strip(),
                "Datum": pruefungsdatum.strftime("%d.%m.%Y"),
                "Bemerkung": bemerkung.strip(),
                "Tage bis Prüfung": tage
            }
        ])

        st.session_state["exams_df"] = pd.concat(
            [
                st.session_state["exams_df"],
                neue_pruefung
            ],
            ignore_index=True
        )

        # -------------------- CSV speichern --------------------
        data_manager = DataManager()

        data_manager.save_user_data(
            st.session_state["exams_df"],
            "pruefungen.csv"
        )

        st.success("Prüfung wurde gespeichert.")


# -------------------- Clear --------------------
if clear:

    st.session_state["exams_df"] = pd.DataFrame(
        columns=[
            "Fach",
            "Datum",
            "Bemerkung",
            "Tage bis Prüfung"
        ]
    )

    # -------------------- Leere CSV speichern --------------------
    data_manager = DataManager()

    data_manager.save_user_data(
        st.session_state["exams_df"],
        "pruefungen.csv"
    )

    st.rerun()


# -------------------- Anzeige --------------------
st.subheader("Meine Prüfungen")

if not st.session_state["exams_df"].empty:

    st.dataframe(
        st.session_state["exams_df"],
        use_container_width=True
    )

    for _, row in st.session_state["exams_df"].iterrows():

        tage = int(
            row["Tage bis Prüfung"]
        )

        if tage < 0:

            st.info(
                f"Die Prüfung in {row['Fach']} ist bereits vorbei."
            )

        elif tage == 0:

            st.error(
                f"Heute ist deine Prüfung in {row['Fach']}!"
            )

            st.toast(
                f"Heute Prüfung: {row['Fach']}",
                icon="⚠️"
            )

        elif tage <= 3:

            st.warning(
                f"Achtung: {row['Fach']} ist in {tage} Tagen!"
            )

            st.toast(
                f"{row['Fach']} ist bald!",
                icon="⏰"
            )

        elif tage <= 7:

            st.info(
                f"{row['Fach']} ist in {tage} Tagen."
            )

else:

    st.info("Noch keine Prüfungen gespeichert.")

