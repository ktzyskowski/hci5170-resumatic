import streamlit as st

from resumatic.streamlit.components import editor, feedback, upload_resume_modal, sidebar


def app():
    # set page width to take up entire browser
    st.set_page_config(layout="wide")

    if "resume_service" not in st.session_state:
        upload_resume_modal()
    else:
        sidebar()
        editor()

        st.divider()
        feedback()
