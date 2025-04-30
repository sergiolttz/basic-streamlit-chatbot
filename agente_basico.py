#importar librerias basicas
import streamlit as st 
from dotenv import load_dotenv
import os
from langchain_cohere import ChatCohere
from langchain.schema import SystemMessage, HumanMessage, AIMessage

from utils import get_role
from core.llm import model
from prompts.prompts import basic_prompt, especialista_futbol

st.title("maldini")
st.write("Este es un bot de futbol")

init_message = SystemMessage(
    content= especialista_futbol
)

if "message" not in st.session_state:
    st.session_state.message = [init_message]

for message in st.session_state.message:
    role = get_role(message)
    if role != "system":
        with st.chat_message(role):
            st.markdown(message.content)

if prompt := st.chat_input("Que te gustaria decir?"):
    user_message = HumanMessage(content=prompt)
    st.session_state.message.append(user_message)
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = model.invoke(st.session_state.message)
            ai_message = AIMessage(content=response.content)
            st.markdown(response.content)

            st.session_state.message.append(ai_message)