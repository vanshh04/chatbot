import os 
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

st.set_page_config(
    page_title="krust.ai",
    page_icon="🫥",
    layout="centered",
)
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel('gemini-pro')

def translate_role(user_role):
    if user_role=="model":
        return "assistant"
    else:
        return user_role
    

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("fox.ai")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask fox...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    gemini_res=st.session_state.chat_session.send_message(user_prompt)

    with st.chat_message("assistant"):
        st.markdown(gemini_res.text)
