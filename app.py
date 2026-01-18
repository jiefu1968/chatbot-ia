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

if st.button("🧹 Começar nova conversa"):
    st.session_state.mensagens = []
    st.rerun()
```

---

## 🎯 COMO APLICAR NO GITHUB

### **Passo a Passo:**
```
1. Vá para: github.com
2. Entre no repositório: chatbot-ia
3. Clique no arquivo: app.py
4. Clique no ícone de LÁPIS ✏️ (Edit this file)
5. Aperte Command + A (selecionar tudo)
6. Aperte Delete (apagar tudo)
7. Cole o código acima (Command + V)
8. Role até o final
9. Digite na caixa: Codigo corrigido sem erros
10. Clique em: [Commit changes] (botão verde)
```

---

## ⏰ AGUARDAR
```
Após salvar:
- Aguarde 30-60 segundos
- O Streamlit atualiza automaticamente
- Seu chatbot vai reiniciar
- Teste novamente!
