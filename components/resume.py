import streamlit as st

@st.dialog("Load your résumé")
def upload_resume():
    uploaded_file = st.file_uploader("Upload your resume here", type=["txt"])
    submit_button_is_disabled = uploaded_file is None
    if st.button("Submit", disabled=submit_button_is_disabled):
        st.session_state.resume_file = uploaded_file
        st.session_state.messages = []  # Reset messages
        st.rerun()

def resume_viewer():
    st.header("Résumé")
    if "resume_file" in st.session_state:
        resume_file = st.session_state.resume_file
        bytes_data = resume_file.getvalue()
        if resume_file.type == "text/plain":
            content = bytes_data.decode("utf-8")
            st.session_state.resume_text = content
            st.text(content)
        else:
            raise ValueError("Unknown file type uploaded")
        if st.button("Upload new résumé"):
            upload_resume()
    else:
        st.warning("Résumé has not been loaded")
        if st.button("Upload résumé"):
            upload_resume()
