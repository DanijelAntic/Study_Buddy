import streamlit as st
import pandas as pd

st.title("Noteneintrag Rechner")


# -------------------- Session State --------------------
if "noten_df" not in st.session_state:
    st.session_state["noten_df"] = pd.DataFrame(
        columns=["Fach", "Noten", "Durchschnitt"]
    )

if "fach_input" not in st.session_state:
    st.session_state["fach_input"] = ""

if "note_input" not in st.session_state:
    st.session_state["note_input"] = 4.0


# -------------------- Formular --------------------
st.subheader("Neue Note eintragen")

with st.form("noten_form"):

    fach = st.text_input(
        "Fach",
        key="fach_input",
        placeholder="z.B. Mathe"
    )

    note = st.number_input(
        "Note",
        min_value=1.0,
        max_value=6.0,
        step=0.1,
        key="note_input"
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

        df = st.session_state["noten_df"].copy()

        fach_clean = fach.strip()

        # Fach existiert bereits
        if fach_clean in df["Fach"].values:

            index = df.index[df["Fach"] == fach_clean][0]

            alte_noten = str(df.at[index, "Noten"])

            neue_noten = f"{alte_noten}, {note}"

            df.at[index, "Noten"] = neue_noten

            noten_liste = [
                float(n.strip())
                for n in neue_noten.split(",")
            ]

            durchschnitt = round(
                sum(noten_liste) / len(noten_liste),
                2
            )

            df.at[index, "Durchschnitt"] = durchschnitt

        # Neues Fach
        else:

            df.loc[len(df)] = {
                "Fach": fach_clean,
                "Noten": str(note),
                "Durchschnitt": round(note, 2)
            }

        st.session_state["noten_df"] = df

        st.success("Note gespeichert.")

        # Eingaben zurücksetzen
        st.session_state["fach_input"] = ""
        st.session_state["note_input"] = 4.0

        st.rerun()


# -------------------- Clear --------------------
if clear:

    st.session_state["noten_df"] = pd.DataFrame(
        columns=["Fach", "Noten", "Durchschnitt"]
    )

    st.session_state["fach_input"] = ""
    st.session_state["note_input"] = 4.0

    st.rerun()


# -------------------- Tabelle --------------------
st.subheader("Notentabelle")

if not st.session_state["noten_df"].empty:

    st.dataframe(
        st.session_state["noten_df"],
        use_container_width=True
    )

else:
    st.info("Noch keine Noten eingetragen.")
