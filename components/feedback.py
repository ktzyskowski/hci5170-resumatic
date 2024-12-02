import streamlit as st

def feedback_section():
    st.header("Feedback")

    with st.form("feedback_form"):
        feedback_text = st.text_area("Your feedback", placeholder="Write your feedback here...")
        include_context = st.checkbox("Include context with feedback")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.toast("Submitted feedback", icon="✅")
            # Save feedback logic (optional)
