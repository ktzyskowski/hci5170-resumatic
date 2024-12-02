import streamlit as st
from components.sidebar import sidebar_menu
from components.feedback import feedback_section
from components.resume import resume_viewer
from components.chat import chat
from utils.css import inject_global_css

st.set_page_config(layout="wide")
st.title("📝 Résumatic")

# Sidebar menu
sidebar_menu()

# Global font size adjustment
font_size = st.slider("Adjust global font size", min_value=10, max_value=30, value=14, step=1)
inject_global_css(font_size)

# Main content layout
viewer_col, chat_col = st.columns(2)

with viewer_col:
    with st.container(border=True):
        resume_viewer()

with chat_col:
    with st.container(border=True):
        chat()

# Feedback section
st.markdown("---")
feedback_section()
