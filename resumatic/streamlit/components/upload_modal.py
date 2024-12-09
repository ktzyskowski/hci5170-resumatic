import streamlit as st

from resumatic.model.resume_service import ResumeService


@st.dialog("Upload your résumé")
def upload_resume_modal():
    uploaded_file = st.file_uploader(label="upload_resume", label_visibility="collapsed", type=["pdf"])
    submit_button_is_disabled = uploaded_file is None
    if st.button("Submit", disabled=submit_button_is_disabled):
        # make sure to have this configured in .streamlit/secrets.toml file
        st.session_state.resume_service = ResumeService(uploaded_file, api_key=st.secrets.openai.api_key)

        # reset messages when we upload a new file
        st.session_state.messages = []
        st.rerun()
