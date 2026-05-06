import streamlit as st
import pandas as pd

st.title("Noteneintrag Rechner")

if "noten_df" not in st.session_state:
    st.session_state["noten_df"] = pd.DataFrame(
        columns=["Fach", "Noten", "Durchschnitt"]
    )

st.subheader("Neue Note eintragen")

with st.form("noten_form"):
    fach = st.text_input("Fach", placeholder="z.B. Mathe")
    note = st.number_input(
        "Note",
        min_value=1.0,
        max_value=6.0,
        step=0.1,
        value=4.0
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        speichern = st.form_submit_button("Speichern")

    with col2:
        clear = st.form_submit_button("Clear")

    with col3:
        durchschnitt_button = st.form_submit_button("Durchschnitt berechnen")


if speichern:
    if fach.strip() == "":
        st.warning("Bitte ein Fach eingeben.")
    else:
        df = st.session_state["noten_df"].copy()
        fach_clean = fach.strip()

        if fach_clean in df["Fach"].values:
            index = df.index[df["Fach"] == fach_clean][0]

            alte_noten = df.at[index, "Noten"]
            neue_noten = f"{alte_noten}, {note}"

            df.at[index, "Noten"] = neue_noten

            noten_liste = [
                float(n.strip()) for n in neue_noten.split(",")
            ]
            df.at[index, "Durchschnitt"] = round(
                sum(noten_liste) / len(noten_liste), 2
            )

        else:
            df.loc[len(df)] = {
                "Fach": fach_clean,
                "Noten": str(note),
                "Durchschnitt": round(note, 2)
            }

        st.session_state["noten_df"] = df
        st.success("Note gespeichert.")


if durchschnitt_button:
    df = st.session_state["noten_df"].copy()

    for index, row in df.iterrows():
        noten_liste = [
            float(n.strip()) for n in str(row["Noten"]).split(",")
            if n.strip() != ""
        ]

        if len(noten_liste) > 0:
            df.at[index, "Durchschnitt"] = round(
                sum(noten_liste) / len(noten_liste), 2
            )

    st.session_state["noten_df"] = df
    st.success("Durchschnitt berechnet.")


if clear:
    st.session_state["noten_df"] = pd.DataFrame(
        columns=["Fach", "Noten", "Durchschnitt"]
    )
    st.rerun()


st.subheader("Notentabelle")

if not st.session_state["noten_df"].empty:
    st.dataframe(st.session_state["noten_df"], use_container_width=True)
else:
    st.info("Noch keine Noten eingetragen.")
