import streamlit as st

def main():
    st.title("Wochenplaner")
    st.write("Plane deinen Wochenablauf mit diesem interaktiven Kalender.")

    # Definierte Wochentage und Zeiten
    tage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    zeiten = [f"{i}-{i+1}" for i in range(6, 22)]  # 6-7, 7-8, ..., 21-22

    # Optionen für die Drop-Down-Auswahl (kannst du erweitern)
    optionen = ["Leer", "Lernen", "Sport", "Essen", "Arbeit", "Freizeit", "Schlafen"]

    # Initialisiere session_state für den Wochenplan, falls nicht vorhanden
    if 'wochenplan' not in st.session_state:
        st.session_state['wochenplan'] = {tag: {zeit: "Leer" for zeit in zeiten} for tag in tage}

    # Erstelle die Tabelle mit Spalten für die Tage
    cols = st.columns(len(tage) + 1)  # +1 für die Zeit-Spalte links

    # Header: Leere Zelle links oben, dann die Tage
    with cols[0]:
        st.write("")  # Leere Zelle für die Ecke
    for i, tag in enumerate(tage):
        with cols[i + 1]:
            st.markdown(f"**{tag}**")

    # Für jede Zeit eine Zeile erstellen
    for zeit in zeiten:
        # Zeit-Spalte links
        with cols[0]:
            st.markdown(f"**{zeit}**")
        
        # Für jeden Tag eine Zelle mit Selectbox
        for i, tag in enumerate(tage):
            with cols[i + 1]:
                # Hole den aktuellen Wert aus session_state
                aktueller_wert = st.session_state['wochenplan'][tag][zeit]
                # Selectbox für die Auswahl
                neuer_wert = st.selectbox(
                    label=f"{tag} {zeit}",  # Label für die Selectbox (unsichtbar, aber erforderlich)
                    options=optionen,
                    index=optionen.index(aktueller_wert) if aktueller_wert in optionen else 0,
                    key=f"{tag}_{zeit}",  # Eindeutiger Key für jede Zelle
                    label_visibility="collapsed"  # Verstecke das Label, um Platz zu sparen
                )
                # Speichere die Änderung in session_state
                st.session_state['wochenplan'][tag][zeit] = neuer_wert

    # Optional: Zeige den aktuellen Plan als JSON an (für Debugging)
    st.write("### Aktueller Wochenplan (Vorschau)")
    st.json(st.session_state['wochenplan'])

# Diese Funktion wird von Streamlit als Seite aufgerufen
if __name__ == "__main__":
    main()