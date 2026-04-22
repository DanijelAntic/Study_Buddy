import streamlit as st

def main():
    st.title("Wochenplaner")
    st.write("Plane deinen Wochenablauf mit diesem interaktiven Kalender.")

    # Definierte Wochentage und Zeiten
    tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    zeiten = [f"{i}-{i+1}" for i in range(6, 22)]  # 6-7, 7-8, ..., 21-22

    # Optionen für die Drop-Down-Auswahl
    optionen = ["Leer", "Lernen", "Sport", "Essen", "Arbeit", "Freizeit", "Schlafen"]

    # Initialisiere session_state
    if 'wochenplan' not in st.session_state:
        st.session_state['wochenplan'] = {tag: {zeit: "Leer" for zeit in zeiten} for tag in tage}

    # Header
    header_cols = st.columns([0.8, 1, 1, 1, 1, 1, 1, 1])
    with header_cols[0]:
        st.markdown("**Zeit**")
    for i, tag in enumerate(tage):
        with header_cols[i + 1]:
            st.markdown(f"**{tag}**")

    # Tabelle - jede Zeile mit Spalten
    for zeit in zeiten:
        row_cols = st.columns([0.8, 1, 1, 1, 1, 1, 1, 1])
        
        # Zeit-Spalte links
        with row_cols[0]:
            st.markdown(f"{zeit}")
        
        # Für jeden Tag eine Selectbox
        for i, tag in enumerate(tage):
            with row_cols[i + 1]:
                aktueller_wert = st.session_state['wochenplan'][tag][zeit]
                neuer_wert = st.selectbox(
                    label=f"{tag} {zeit}",
                    options=optionen,
                    index=optionen.index(aktueller_wert) if aktueller_wert in optionen else 0,
                    key=f"{tag}_{zeit}",
                    label_visibility="collapsed"
                )
                st.session_state['wochenplan'][tag][zeit] = neuer_wert

if __name__ == "__main__":
    main()
