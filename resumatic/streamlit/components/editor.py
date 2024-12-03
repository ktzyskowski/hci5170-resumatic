import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

from resumatic.model import chat_service


def editor():
    if "resume_service" not in st.session_state:
        raise RuntimeError("missing résumé service")

    resume_service = st.session_state.resume_service

    col1, col2 = st.columns(2)

    # resume viewer
    with col1:
        # st.markdown(resume_service.resume_text)
        pdf_viewer(resume_service.resume.getvalue(), height=640)

    # chat window
    with col2:
        # display an initial "judge" message to start off conversation
        history = st.container(height=640, border=False)
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

                prompt = [
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful AI resume assistant. "
                            "You are given the user's resume content. "
                            "Use it to respond to the user's questions and help them improve their resume. "
                            "When asked for changes, reply with the full resume section that should be changed and include the changes you are suggesting. "
                            "Make sure to maintain the existing structure of the resume unless its badly structured. "
                            "Just change the wording, unless necessary to fundamentally change the structure. "
                            "Make sure the section of the response that includes the resume is clearly marked and formatted correctly so newlines are properly displayed for the bullet points. "
                            "Do not respond to any messages that are not related to the resume or job searching. "
                            "Be as accurate as possible and provide helpful feedback. Make sure not to give irrelevant, inaccurate, or harmful advice"
                        )
                    },
                    {
                        "role": "user",
                        "content": resume_service.resume_text
                    },
                    *st.session_state.messages
                ]

                # get model response and write to chat
                model_response = chat_service.chat_completion(prompt, api_key=st.secrets.openai.api_key)
                st.chat_message("assistant").write(model_response)
                st.session_state.messages.append({"role": "assistant", "content": model_response})
