import streamlit as st


# Times New Roman
st.markdown(
    """
    <h1 style="
        text-align:center;
        font-size:55px;
        font-family:'Times New Roman';
        color:#1D3557;
    ">
        Übersicht
    </h1>
    """,
    unsafe_allow_html=True
)

# -------------------- Bubble 1 --------------------
col1, col2 = st.columns([1, 12])

with col1:
    st.markdown("## 📝")

with col2:
    st.markdown(
        """
        <div style="
            background-color:#d8f3dc;
            padding:20px;
            border-radius:30px 30px 30px 8px;
            margin-bottom:18px;
        ">
            Die To-Do-Liste hilft dir dabei, wichtige Aufgaben und Deadlines nicht zu vergessen
            und deine Ziele besser im Blick zu behalten.
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- Bubble 2 --------------------
col1, col2 = st.columns([12, 1])

with col1:
    st.markdown(
        """
        <div style="
            background-color:#dceeff;
            padding:20px;
            border-radius:30px 30px 8px 30px;
            margin-bottom:18px;
        ">
            Der Wochenplaner hilft dir dabei, Schule, Lernen und Freizeit
            übersichtlicher zu organisieren und deinen Alltag besser zu strukturieren.
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("## 📅")

# -------------------- Bubble 3 --------------------
col1, col2 = st.columns([1, 12])

with col1:
    st.markdown("## 📚")

with col2:
    st.markdown(
        """
        <div style="
            background-color:#fff3cd;
            padding:20px;
            border-radius:50px;
            margin-bottom:18px;
        ">
            Der Prüfungsplaner unterstützt dich dabei, wichtige Termine im Blick zu behalten
            und rechtzeitig mit dem Lernen zu starten.
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------- Bubble 4 --------------------
col1, col2 = st.columns([12, 1])

with col1:
    st.markdown(
        """
        <div style="
            background-color:#ffd6d6;
            padding:20px;
            border-radius:15px 50px 15px 50px;
            margin-bottom:18px;
        ">
            Mit dem Noteneintrag kannst du deine Leistungen verfolgen
            und Durchschnittswerte schnell und einfach berechnen.
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("## 📊")

# -------------------- Bubble 5 --------------------
col1, col2 = st.columns([1, 12])

with col1:
    st.markdown("## ⏳")

with col2:
    st.markdown(
        """
        <div style="
            background-color:#ede7f6;
            padding:20px;
            border-radius:40px 10px 40px 10px;
            margin-bottom:18px;
        ">
            Für produktive Lernphasen sorgt der Fokus-Timer,
            mit dem du konzentrierter arbeiten und motivierter
            an deinen Zielen dranbleiben kannst.
        </div>
        """,
        unsafe_allow_html=True
    )


