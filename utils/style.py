import streamlit as st


def page_title(title):

    st.markdown(
        f"""
        <h1 style="
            font-size:55px;
            font-family:'Times New Roman';
            color:#1D3557;
        ">
            {title}
        </h1>
        """,
        unsafe_allow_html=True
    )