import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():

    style_base_layout()
    style_background_home()

    header_home()

    left, center, right = st.columns([1, 4, 1])

    with center:
        col1, col2 = st.columns(2)

    with col1:
        if st.button("Teacher Portal", use_container_width=True):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    with col2:
        if st.button("Student Portal", use_container_width=True):
            st.session_state["login_type"] = "student"
            st.rerun()