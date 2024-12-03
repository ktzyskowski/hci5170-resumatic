import streamlit as st

from resumatic.streamlit.components import options_expander


def sidebar():
    with st.sidebar:
        st.header("User Menu")
        st.button("Log In", key="login_sidebar")
        st.button("Account Settings", key="account_settings_sidebar")
        st.button("Help", key="help_sidebar")
        options_expander()
