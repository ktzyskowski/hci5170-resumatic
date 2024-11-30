import streamlit as st

from resumatic.streamlit.components import editor, options_expander, upload_resume_modal


def app():
    # set page width to take up entire browser
    st.set_page_config(layout="wide")

    if "resume_service" not in st.session_state:
        upload_resume_modal()
    else:
        options_expander()
        editor()
