import streamlit as st
import pandas as pd
from datetime import date, datetime

from utils.data_manager import DataManager


# -------------------- Speichern Funktion --------------------
def save_todos():

    data_manager = DataManager()

    # Wenn Aufgaben vorhanden
    if st.session_state["todos"]:

        todos_df = pd.DataFrame(
            st.session_state["todos"]
        )

    # Wenn keine Aufgaben vorhanden
    else:

        todos_df = pd.DataFrame(
            columns=[
                "Aufgabe",
                "Beschreibung",
                "Deadline",
                "Erledigt"
            ]
        )

    data_manager.save_user_data(
        todos_df,
        "todos.csv"
    )


# -------------------- Titel --------------------
st.markdown(
    """
    <h1 style="
        font-size:55px;
        font-family:'Times New Roman';
        color:#1D3557;
    ">
        To-Do-Liste
    </h1>
    """,
    unsafe_allow_html=True
)

st.write(
    "Organisiere deine Aufgaben und behalte wichtige "
    "To-Dos und Deadlines im Überblick."
)


# -------------------- Daten laden --------------------
if "todos" not in st.session_state:

    data_manager = DataManager()

    try:

        todos_df = data_manager.load_user_data(
            "todos.csv",
            pd.DataFrame()
        )

        if not todos_df.empty:

            st.session_state["todos"] = (
                todos_df.to_dict("records")
            )

        else:

            st.session_state["todos"] = []

    except pd.errors.EmptyDataError:

        st.session_state["todos"] = []


# -------------------- Formular --------------------
with st.form(
    "todo_form",
    clear_on_submit=True
):

    aufgabe = st.text_input(
        "Aufgabe"
    )

    beschreibung = st.text_input(
        "Kurze Beschreibung"
    )

    deadline = st.date_input(
        "Deadline"
    )

    speichern = st.form_submit_button(
        "Speichern"
    )

    if speichern:

        if aufgabe.strip() == "":

            st.warning(
                "Bitte eine Aufgabe eingeben."
            )

        else:

            st.session_state["todos"].append({

                "Aufgabe":
                    aufgabe.strip(),

                "Beschreibung":
                    beschreibung.strip(),

                "Deadline":
                    deadline.strftime("%d.%m.%Y"),

                "Erledigt":
                    False
            })

            save_todos()

            st.success(
                "Aufgabe gespeichert."
            )


# -------------------- Aufgaben anzeigen --------------------
if st.session_state["todos"]:

    st.subheader(
        "Meine Aufgaben"
    )

    col1, col2, col3, col4 = st.columns(
        [2, 3, 2, 1]
    )

    col1.write("**Aufgabe**")
    col2.write("**Kurze Beschreibung**")
    col3.write("**Deadline**")
    col4.write("**Erledigt**")

    checkbox_geaendert = False

    for i, todo in enumerate(
        st.session_state["todos"]
    ):

        c1, c2, c3, c4 = st.columns(
            [2, 3, 2, 1]
        )

        c1.write(todo["Aufgabe"])
        c2.write(todo["Beschreibung"])
        c3.write(todo["Deadline"])

        erledigt = c4.checkbox(
            "",
            value=bool(todo["Erledigt"]),
            key=f"todo_done_{i}"
        )

        if erledigt != todo["Erledigt"]:

            st.session_state["todos"][i]["Erledigt"] = erledigt

            checkbox_geaendert = True

    if checkbox_geaendert:

        save_todos()

else:

    st.info(
        "Noch keine Aufgaben vorhanden."
    )


# -------------------- Clear Button --------------------
if st.button("Clear"):

    st.session_state["todos"] = []

    save_todos()

    st.rerun()


# -------------------- Erinnerungen --------------------
if st.session_state["todos"]:

    st.subheader(
        "Erinnerungen"
    )

    heute = date.today()

    for todo in st.session_state["todos"]:

        deadline_date = datetime.strptime(
            todo["Deadline"],
            "%d.%m.%Y"
        ).date()

        tage = (
            deadline_date - heute
        ).days

        if todo["Erledigt"]:

            continue

        if tage < 0:

            st.error(
                f"Die Aufgabe '{todo['Aufgabe']}' "
                f"ist überfällig!"
            )

        elif tage == 0:

            st.warning(
                f"Heute fällig: "
                f"{todo['Aufgabe']}"
            )

            st.toast(
                f"Heute fällig: "
                f"{todo['Aufgabe']}",
                icon="⚠️"
            )

        elif tage == 1:

            st.info(
                f"Morgen fällig: "
                f"{todo['Aufgabe']}"
            )

        elif tage <= 3:

            st.info(
                f"{todo['Aufgabe']} "
                f"ist in {tage} Tagen fällig."
            )

