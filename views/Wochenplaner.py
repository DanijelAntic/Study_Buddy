import streamlit as st

def main():
    st.title("Wochenplaner")
    st.write("Plane deinen Wochenablauf mit diesem interaktiven Kalender.")

    # Definierte Wochentage und Zeiten
    tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]  # Abgekürzte Wochentage
    zeiten = [f"{i}-{i+1}" for i in range(6, 22)]  # 6-7, 7-8, ..., 21-22 (endet bei 22 Uhr, keine Felder danach)

    # Optionen für die Drop-Down-Auswahl (kannst du erweitern)
    optionen = ["Leer", "Lernen", "Sport", "Essen", "Arbeit", "Freizeit", "Schlafen"]

    # Initialisiere session_state für den Wochenplan, falls nicht vorhanden
    if 'wochenplan' not in st.session_state:
        st.session_state['wochenplan'] = {tag: {zeit: "Leer" for zeit in zeiten} for tag in tage}

    # Header in separater Zeile
    header_cols = st.columns(8)  # Gleiche Anzahl Spalten wie die Tabelle
    with header_cols[0]:
        st.write("")  # Obere linke Ecke leer
    for i, tag in enumerate(tage):
        with header_cols[i + 1]:
            st.markdown(f"**{tag}**")

    # Leerzeile, um die Zeiten eine Zeile darunter zu starten
    st.write("")

    # Tabelle mit Zeiten (startet eine Zeile unter dem Header)
    cols = st.columns(8)  # Alle 8 Spalten gleich breit

    # Für jede Zeit eine Zeile erstellen (keine Felder nach 22 Uhr)
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

# Diese Funktion wird von Streamlit als Seite aufgerufen
if __name__ == "__main__":
    main()