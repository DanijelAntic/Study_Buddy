import streamlit as st
import random


def zeige_motivation():

    motivationen = [
        "🌿 Denk daran: Auch kleine Fortschritte zählen.",
        "✨ Schritt für Schritt kommst du deinem Ziel näher.",
        "📚 Du musst nicht perfekt sein — nur dranbleiben.",
        "🌸 Jeder Lerntag bringt dich weiter.",
        "💡 Kleine Fortschritte sind auch Fortschritte.",
        "🚀 Du schaffst mehr, als du denkst.",
        "☁️ Lernen darf auch entspannt sein."
    ]

    nachricht = random.choice(motivationen)

    position = random.choice(["left", "center", "right"])

    if position == "left":

        col1, col2, col3 = st.columns([2, 6, 2])

        with col1:
            st.markdown(
                f"""
                <div style="
                    background-color:#d8f3dc;
                    padding:15px;
                    border-radius:25px 25px 25px 8px;
                    margin-top:15px;
                    text-align:center;
                ">
                    {nachricht}
                </div>
                """,
                unsafe_allow_html=True
            )

    elif position == "center":

        col1, col2, col3 = st.columns([2, 6, 2])

        with col2:
            st.markdown(
                f"""
                <div style="
                    background-color:#dceeff;
                    padding:15px;
                    border-radius:25px;
                    margin-top:15px;
                    text-align:center;
                ">
                    {nachricht}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        col1, col2, col3 = st.columns([2, 6, 2])

        with col3:
            st.markdown(
                f"""
                <div style="
                    background-color:#ede7f6;
                    padding:15px;
                    border-radius:25px 25px 8px 25px;
                    margin-top:15px;
                    text-align:center;
                ">
                    {nachricht}
                </div>
                """,
                unsafe_allow_html=True
            )