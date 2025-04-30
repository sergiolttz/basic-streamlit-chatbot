import streamlit as st

st.title("RupertoBot")
st.write("Este es un bot")

st.sidebar.title("Sidebar")
st.sidebar.write("This is a sidebar")

messages = []
# 1. Inicializar el session state para los mensajes
if "message" not in st.session_state:
    st.session_state.message = messages  

# 2. Mostrar los mensajes previos en el historial
for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Procesar el mensaje del usuario
if prompt := st.chat_input("Que te gustaría decir?"):
    # 4. Añadir el mensaje del usuario a session_state
    st.session_state.message.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)


# 4. Ejemplo de una respuesta
response = f"Echo: {prompt}"
with st.chat_message("assistant"):
    st.markdown(response)

# 5. agregar la respuesta del bot al session state
st.session_state.message.append({"role": "assistant", "content": response})