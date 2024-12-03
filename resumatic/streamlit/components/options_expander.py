import streamlit as st


def set_font_size(font_size):
    css = f"<style> :root {{font-size: {font_size}px;}}</style>"
    st.markdown(css, unsafe_allow_html=True)


def options_expander():
    with st.expander("Options", expanded=False):
        font_size = st.slider("Adjust global font size", min_value=10, max_value=30, value=14, step=1)
        set_font_size(font_size)

        reset_conversation = st.button("Clear Conversation and Résumé", type="primary", icon="♻️")
        if reset_conversation:
            del st.session_state.resume_service
            del st.session_state.messages
            st.rerun()
