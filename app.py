import streamlit as st
import openai

st.title("Meu Assistente de IA")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if pergunta := st.chat_input("Digite sua pergunta..."):
    with st.chat_message("user"):
        st.write(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    
    with st.chat_message("assistant"):
        mensagens = [{"role": "system", "content": "Voce e um assistente util."}]
        mensagens.extend(st.session_state.mensagens)
        
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=mensagens
        )
        
        texto = resposta.choices[0].message.content
        st.write(texto)
        st.session_state.mensagens.append({"role": "assistant", "content": texto})

if st.button("Nova conversa"):
    st.session_state.mensagens = []
    st.rerun()
