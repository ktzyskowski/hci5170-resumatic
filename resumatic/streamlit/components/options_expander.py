import streamlit as st


def options_expander():
    with st.expander("Conversation Options", expanded=False):
        reset_conversation = st.button("Clear Conversation and Résumé", type="primary", icon="♻️")
        if reset_conversation:
            del st.session_state.file
            del st.session_state.messages
            st.rerun()
