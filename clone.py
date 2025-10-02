import streamlit as st
import google.generativeai as genai
from IPython.display import HTML, Markdown, display
from gemini import llm

st.title("Gemini Clone")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "intro_shown" not in st.session_state:
    st.session_state.intro_shown = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
         st.markdown(message["content"])

prompt = st.chat_input("Say something")
if prompt:
    st.session_state.intro_shown = False
    with st.chat_message("human"):
        st.write(prompt)
    st.session_state.messages.append({"role":"human","content":prompt})
    with st.spinner("🤖 Gemini is thinking..."):
        response = llm(prompt)
    st.session_state.messages.append({"role":"assistant","content":response})
    with st.chat_message("assistant"):
         st.write(llm(prompt))
    

if st.session_state.intro_shown:
    with st.chat_message("assistant"):
        st.write("Hello, How can i help you?")
