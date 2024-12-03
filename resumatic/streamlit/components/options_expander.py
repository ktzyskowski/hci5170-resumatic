import streamlit as st


def inject_global_css(font_size):
    css = f"""
    <style>
    :root {{
        font-size: {font_size}px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def options_expander():
    with st.expander("Options", expanded=False):
        font_size = st.slider("Adjust global font size", min_value=10, max_value=30, value=14, step=1)
        inject_global_css(font_size)

        reset_conversation = st.button("Clear Conversation and Résumé", type="primary", icon="♻️")
        if reset_conversation:
            del st.session_state.file
            del st.session_state.messages
            st.rerun()
