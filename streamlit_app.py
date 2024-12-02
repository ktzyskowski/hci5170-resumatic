import streamlit as st

from openai import OpenAI

# set page width to take up entire browser
st.set_page_config(layout="wide")

# load in OpenAI API key from `.streamlit/secrets.toml` file
openai_api_key = st.secrets.openai_api_key


@st.dialog("Load your résumé")
def upload_resume():
    uploaded_file = st.file_uploader("Upload your resume here", type=["txt"])
    submit_button_is_disabled = uploaded_file is None
    if st.button("Submit", disabled=submit_button_is_disabled):
        st.session_state.resume_file = uploaded_file
        # reset messages when we upload a new file
        st.session_state.messages = []
        st.rerun()

def inject_global_css(font_size):
    # Inject CSS into the app to adjust font size globally
    css = f"""
    <style>
    :root {{
        font-size: {font_size}px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def resume_viewer():
    st.header("Résumé")
    if "resume_file" in st.session_state:
        resume_file = st.session_state.resume_file
        bytes_data = resume_file.getvalue()
        if resume_file.type ==  "text/plain":
            content = bytes_data.decode("utf-8")
            st.session_state.resume_text = content
            st.text(content)
        else:
            raise ValueError("unknown file type uploaded")
        if st.button("Upload new résumé"):
            upload_resume()
    else:
        st.warning("Résumé has not been loaded")
        if st.button("Upload résumé"):
            upload_resume()


def openai_completion(messages: list):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    msg = response.choices[0].message.content
    return msg


def judge_resume(resume_content: str):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful AI resume assistant. "
                "Begin the conversation by judging the given resume content by its quality and providing a high level summary. "
                "Respond in less than 4 sentences and speak in the 2nd person tense. "
            )
        },
        {
            "role": "user",
            "content": resume_content
        }
    ])
    msg = response.choices[0].message.content
    return msg


def chat():
    st.header("Chat")

    if "resume_file" not in st.session_state:
        st.chat_message("assistant").write("Please upload your résumé.")
    else:
        # make a summary of uploaded resume
        if len(st.session_state.messages) == 0:
            # upload a generic summary of the resume.
            with st.spinner("Looking at your résumé..."):
                resume_response = judge_resume(st.session_state.resume_text)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": resume_response
                },
            )

        # display all messages in chat history
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        # accept user input
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
            # st.chat_message("assistant").write(msg)

def feedback_section():
    st.markdown("---")
    st.header("Feedback")

    with st.form("feedback_form"):
        feedback_text = st.text_area("Your feedback", placeholder="Write your feedback here...")
        submitted = st.form_submit_button("Submit")
        include_context = st.checkbox("Include context with feedback")


    if submitted:
            # Display a popup confirmation
            st.toast("Submitted feedback", icon="✅")
            # Save the feedback to a file or database including context if selected

st.title("📝 Résumatic")

def sidebar_menu():
    with st.sidebar:
        st.header("User Menu")
        st.button("Log In", key="login_sidebar")
        st.button("Account Settings", key="account_settings_sidebar")
        st.button("Help", key="help_sidebar")
    # Implement the sidebar menu functionality in final app


# Call the sidebar menu function
sidebar_menu()



# Add a slider for font size at the top of the app
font_size = st.slider("Adjust global font size", min_value=10, max_value=30, value=14, step=1)

viewer_col, chat_col = st.columns(2)

with viewer_col:
    with st.container(border=True):
        resume_viewer()

with chat_col:
    with st.container(border=True):
        chat()

# Add a feedback button at the bottom of the app
st.markdown("---")
# Call the feedback section function
feedback_section()
inject_global_css(font_size)

