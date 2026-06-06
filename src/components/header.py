import streamlit as st

def header_home():

    left, center, right = st.columns([2, 1, 2])

    with center:
        st.image("Logo/Logo.png", width=120)

    st.markdown(
        """
        <h1 style='text-align:center; color:#E0E3FF;'>
            BIOMETRIC<br>IDENTITY
        </h1>
        """,
        unsafe_allow_html=True
    )