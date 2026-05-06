import streamlit as st
from datetime import date, datetime

st.title("To-Do Liste")

# -------------------- Session State --------------------
if "todos" not in st.session_state:
    st.session_state["todos"] = []


# -------------------- Formular --------------------
with st.form("todo_form", clear_on_submit=True):
    aufgabe = st.text_input("Aufgabe")
    beschreibung = st.text_input("Kurze Beschreibung")
    deadline = st.date_input("Deadline")

    speichern = st.form_submit_button("Speichern")

    if speichern:
        if aufgabe.strip() == "":
            st.warning("Bitte eine Aufgabe eingeben.")
        else:
            st.session_state["todos"].append({
                "Aufgabe": aufgabe,
                "Beschreibung": beschreibung,
                "Deadline": deadline.strftime("%d.%m.%Y"),
                "Erledigt": False
            })
            st.success("Aufgabe gespeichert.")


# -------------------- Aufgaben anzeigen --------------------
if st.session_state["todos"]:
    st.subheader("Meine Aufgaben")

    col1, col2, col3, col4 = st.columns([2, 3, 2, 1])
    col1.write("**Aufgabe**")
    col2.write("**Kurze Beschreibung**")
    col3.write("**Deadline**")
    col4.write("**Erledigt**")

    for i, todo in enumerate(st.session_state["todos"]):
        c1, c2, c3, c4 = st.columns([2, 3, 2, 1])

        c1.write(todo["Aufgabe"])
        c2.write(todo["Beschreibung"])
        c3.write(todo["Deadline"])

        erledigt = c4.checkbox(
            "",
            value=todo["Erledigt"],
            key=f"todo_done_{i}"
        )

        st.session_state["todos"][i]["Erledigt"] = erledigt

else:
    st.info("Noch keine Aufgaben vorhanden.")


# -------------------- Clear Button --------------------
if st.button("Clear"):
    st.session_state["todos"] = []
    st.rerun()


# -------------------- Erinnerungen --------------------
if st.session_state["todos"]:
    st.subheader("Erinnerungen")

    heute = date.today()

    for todo in st.session_state["todos"]:
        deadline_date = datetime.strptime(todo["Deadline"], "%d.%m.%Y").date()
        tage = (deadline_date - heute).days

        if todo["Erledigt"]:
            continue

        if tage < 0:
            st.error(f"Die Aufgabe '{todo['Aufgabe']}' ist überfällig!")
        elif tage == 0:
            st.warning(f"Heute fällig: {todo['Aufgabe']}")
            st.toast(f"Heute fällig: {todo['Aufgabe']}", icon="⚠️")
        elif tage == 1:
            st.info(f"Morgen fällig: {todo['Aufgabe']}")
        elif tage <= 3:
            st.info(f"{todo['Aufgabe']} ist in {tage} Tagen fällig.")