
import streamlit as st
from openai import OpenAI
from config import secreat_key

# in the secreat key I have kept the OpenAI API key for the security purpose.
api_key = secreat_key

st.set_page_config(page_title="Hr.Assistant", page_icon='speech_balloon')

# Title of the chatbot.

st.title("HR. Chatbot")

client = OpenAI(api_key = api_key)

# Setting up the model fro the session state.

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt := st.chat_input("your answer."):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            # model cheks the model
            model = st.session_state["openai_model"],
            # message parameter that takes entire chat history to improve the assistance response.
            messages = [
                {
                    "role": m["role"], "content": m["content"]

                }
                for m in st.session_state.messages
            ],
            stream = True, # to receive the response as stream.

        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role":"assistant", "content": response})



