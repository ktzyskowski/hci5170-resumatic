from openai import OpenAI
import streamlit as st

openai_api_key = st.secrets.openai_api_key

def openai_completion(messages: list):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content

def judge_resume(resume_content: str):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[
        {
            "role": "system",
            "content": "You are a helpful AI résumé assistant. Summarize and judge the résumé quality."
        },
        {"role": "user", "content": resume_content}
    ])
    return response.choices[0].message.content
