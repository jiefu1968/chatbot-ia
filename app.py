import streamlit as st
import openai

st.title("🤖 Meu Assistente de IA")
st.write("Olá! Faça suas perguntas sobre qualquer assunto.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

if pergunta := st.chat_input("Digite sua pergunta aqui..."):
    
    with st.chat_message("user"):
        st.write(pergunta)
    
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            
            mensagens_para_gpt = [
                {"role": "system", "content": "Você é um assistente prestativo e educado."}
            ]
            mensagens_para_gpt.extend(st.session_state.mensagens)
            
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=mensagens_para_gpt
            )
            
            resposta_texto = resposta.choices[0].message.content
            
            st.write(resposta_texto)
            
            st.session_state.mensagens.append({
                "role": "assistant", 
                "content": resposta_texto
            })

if st.button("Comecar nova conversa"):
    st.session_state.mensagens = []
    st.rerun()
```

---

## 📝 COMO APLICAR (PASSO A PASSO)
```
1. GitHub → seu repositório chatbot-ia
2. Clique em: app.py
3. Clique no lápis para editar
4. Command + A (selecionar tudo)
5. Delete (apagar tudo)
6. Command + V (colar o código acima)
7. Scroll para baixo
8. Commit changes
