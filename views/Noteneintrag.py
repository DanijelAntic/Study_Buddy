import streamlit as st
import pandas as pd

st.title("Noteneintrag Rechner")

if "grades_df" not in st.session_state:
    st.session_state["grades_df"] = pd.DataFrame(
        columns=["Fach", "Noten", "Durchschnitt"]
    )

with st.form("noten_form"):
    fach = st.text_input("Fach eintragen", placeholder="z.B. Mathe, Chemie, Bio")

    noten_text = st.text_input(
        "Noten eintragen",
        placeholder="z.B. 5, 4.5, 6"
    )

    col1, col2 = st.columns(2)

    with col1:
        speichern = st.form_submit_button("Speichern")

    with col2:
        clear = st.form_submit_button("Clear")


if speichern:
    try:
        noten = [
            float(note.strip().replace(",", "."))
            for note in noten_text.split(",")
            if note.strip() != ""
        ]

        if fach.strip() == "":
            st.warning("Bitte ein Fach eingeben.")

        elif len(noten) == 0:
            st.warning("Bitte mindestens eine Note eingeben.")

        elif any(note < 1 or note > 6 for note in noten):
            st.warning("Noten müssen zwischen 1 und 6 liegen.")

        else:
            durchschnitt = round(sum(noten) / len(noten), 2)

            neue_zeile = pd.DataFrame([{
                "Fach": fach,
                "Noten": ", ".join(str(note) for note in noten),
                "Durchschnitt": durchschnitt
            }])

            st.session_state["grades_df"] = pd.concat(
                [st.session_state["grades_df"], neue_zeile],
                ignore_index=True
            )

            st.success(f"{fach} gespeichert. Durchschnitt: {durchschnitt}")

    except ValueError:
        st.error("Bitte Noten korrekt eingeben, z.B. 5, 4.5, 6")


if clear:
    st.session_state["grades_df"] = pd.DataFrame(
        columns=["Fach", "Noten", "Durchschnitt"]
    )
    st.rerun()


st.subheader("Gespeicherte Noten")

if not st.session_state["grades_df"].empty:
    st.dataframe(st.session_state["grades_df"], use_container_width=True)
else:
    st.info("Noch keine Noten gespeichert.")
    