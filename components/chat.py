import streamlit as st
from utils.openai_utils import judge_resume, openai_completion

def chat():
    st.header("Chat")
    if "resume_file" not in st.session_state:
        st.chat_message("assistant").write("Please upload your résumé.")
    else:
        if len(st.session_state.messages) == 0:
            with st.spinner("Looking at your résumé..."):
                resume_response = judge_resume(st.session_state.resume_text)
            st.session_state.messages.append({"role": "assistant", "content": resume_response})

        # Display chat messages
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        # Handle user input
        if prompt := st.chat_input():
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

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
                    "content": st.session_state.resume_text
                }
            ]
            msg = openai_completion(prompt + st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.rerun()
