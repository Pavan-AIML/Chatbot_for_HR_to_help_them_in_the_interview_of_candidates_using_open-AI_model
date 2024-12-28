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


