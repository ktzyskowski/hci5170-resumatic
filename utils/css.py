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
