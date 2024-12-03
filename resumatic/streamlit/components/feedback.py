import streamlit as st


def feedback():
    with st.expander("Submit Feedback", expanded=False):
        with st.form("feedback_form"):
            feedback_text = st.text_area("Your feedback", placeholder="Write your feedback here...")
            include_context = st.checkbox("Include context with feedback")
            submitted = st.form_submit_button("Submit")

            if submitted:
                st.toast("Submitted feedback", icon="✅")
                print(f"Submitted feedback:\n{feedback_text}\ninclude context: {include_context}")
                # Save feedback logic (optional)
