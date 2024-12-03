import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

from resumatic.model import chat_service


def editor():
    if "resume_service" not in st.session_state:
        raise RuntimeError("missing résumé service")

    resume_service = st.session_state.resume_service

    col1, col2 = st.columns(2)
    with col1:
        pdf_viewer(resume_service.resume.getvalue())

    with col2:
        # display an initial "judge" message to start off conversation
        history = st.container(border=False)
        with history:
            if len(st.session_state.messages) == 0:
                model_response = resume_service.judge(resume_service.resume_text)
                st.session_state.messages.append({"role": "assistant", "content": model_response})

            # display all messages in chat history
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])

        # get user prompt
        if prompt := st.chat_input("Enter message"):
            with history:
                # write user input to chat
                st.chat_message("user").write(prompt)
                st.session_state.messages.append({"role": "user", "content": prompt})

                # get model response and write to chat
                model_response = chat_service.chat_completion(st.session_state.messages,
                                                              api_key=st.secrets.openai.api_key)
                st.chat_message("assistant").write(model_response)
                st.session_state.messages.append({"role": "assistant", "content": model_response})
