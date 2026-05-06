import streamlit as st

st.title("To-Do Liste")

if "todos" not in st.session_state:
    st.session_state["todos"] = []

with st.form("todo_form"):
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

col_clear, col_space = st.columns([1, 3])

with col_clear:
    if st.button("Clear"):
        st.session_state["todos"] = []
        st.rerun()
        