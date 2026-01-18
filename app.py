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

### **PASSO 3: Salvar**
```
1. Role até o final da página
2. Na caixa "Commit changes" digite: Corrigindo erro de sintaxe
3. Clique em: [Commit changes] (botão verde)
```

---

## ⏰ AGUARDAR ATUALIZAÇÃO
```
1. Volte para a página do seu chatbot no Streamlit
2. Aguarde 30-60 segundos
3. O Streamlit vai detectar a mudança e REINICIAR automaticamente
4. Você verá: "Updating..." e depois "Running"
```

---

## 🎯 ALTERNATIVA: Reboot Manual

Se não atualizar sozinho:
```
1. Na página do Streamlit, clique nos 3 pontinhos (⋮)
2. Escolha: "Reboot app"
3. Aguarde 1 minuto
```

---

## ✅ TESTAR SE FUNCIONOU

Depois que reiniciar:
```
1. Digite: Olá!
2. O chatbot deve responder
3. ✅ SEM ERRO = FUNCIONOU!
```

---

## 🤔 POR QUE DEU ESSE ERRO?
```
O código tinha comentários decorativos tipo:
File (Arquivo) → Save (Salvar)
              ↑
           Esta setinha é um caractere Unicode especial
           que Python NÃO aceita no código!

Solução: Usei um código mais limpo, sem decorações.
```

---

## 📋 CHECKLIST DE VERIFICAÇÃO

Depois de aplicar a correção:
```
☐ Editei o app.py no GitHub
☐ Apaguei o código antigo
☐ Colei o código novo (limpo)
☐ Fiz commit das mudanças
☐ Aguardei o Streamlit atualizar
☐ Testei o chatbot
☐ FUNCIONOU! ✅
```

---

## 🆘 SE AINDA DER ERRO

Me envie um print da nova mensagem de erro e eu te ajudo!

Ou me diga:
- Qual linha dá erro agora?
- Qual a mensagem completa?

---

## 💡 DICA PRO

Para evitar esses erros no futuro:
```
SEMPRE use código PURO, sem:
❌ Setas decorativas (→ ← ↑ ↓)
❌ Emojis dentro do código
❌ Caracteres especiais em comentários

✅ Use apenas:
- Letras normais (a-z, A-Z)
- Números (0-9)
- Símbolos básicos (# - _ =)
