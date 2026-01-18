import streamlit as st
import openai

# ============================================================================
# TÍTULO DO SEU CHATBOT
# ============================================================================
st.title("🤖 Meu Assistente de IA")
st.write("Olá! Faça suas perguntas sobre qualquer assunto.")

# ============================================================================
# CONFIGURAR A CHAVE DA API (vai vir dos "secrets")
# ============================================================================
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ============================================================================
# CRIAR MEMÓRIA DO CHAT
# ============================================================================
# Esta parte cria uma "memória" para o chatbot lembrar da conversa

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# ============================================================================
# MOSTRAR MENSAGENS ANTERIORES
# ============================================================================
# Mostra tudo que já foi conversado

for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# ============================================================================
# CAIXA PARA DIGITAR
# ============================================================================
# Aqui o usuário digita a pergunta

if pergunta := st.chat_input("Digite sua pergunta aqui..."):
    
    # Mostra a pergunta do usuário na tela
    with st.chat_message("user"):
        st.write(pergunta)
    
    # Guarda a pergunta na memória
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    
    # ========================================================================
    # PEDIR RESPOSTA PARA O GPT
    # ========================================================================
    
    with st.chat_message("assistant"):
        # Mostra "Pensando..." enquanto processa
        with st.spinner("Pensando..."):
            
            # Prepara todas as mensagens para enviar ao GPT
            mensagens_para_gpt = [
                {"role": "system", "content": "Você é um assistente prestativo e educado."}
            ]
            mensagens_para_gpt.extend(st.session_state.mensagens)
            
            # Chama a API do GPT
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=mensagens_para_gpt
            )
            
            # Pega a resposta
            resposta_texto = resposta.choices[0].message.content
            
            # Mostra a resposta na tela
            st.write(resposta_texto)
            
            # Guarda a resposta na memória
            st.session_state.mensagens.append({
                "role": "assistant", 
                "content": resposta_texto
            })

# ============================================================================
# BOTÃO PARA LIMPAR A CONVERSA
# ============================================================================

if st.button("🧹 Começar nova conversa"):
    st.session_state.mensagens = []
    st.rerun()
```

#### **1.5 - Salvar com o nome correto**
```
1. File (Arquivo) → Save (Salvar)
   Ou: Command + S

2. Vai abrir uma janela. Preencha assim:

   Save As (Salvar Como): app.py
   
   ⚠️ IMPORTANTE: 
   ☐ Desmarque: "If no extension is provided, use '.txt'"
   
   Where (Onde): escolha a pasta "meu-chatbot-ia" que você criou

3. Clique em "Save" (Salvar)
```

---

### **Opção 2: Usando Visual Studio Code (VS Code)** 

Se você quer usar um editor profissional (recomendo para o futuro):

#### **2.1 - Instalar VS Code (se não tiver)**
```
1. Acesse: https://code.visualstudio.com
2. Clique em "Download for Mac"
3. Abra o arquivo baixado
4. Arraste o VS Code para a pasta Applications
```

#### **2.2 - Abrir a pasta no VS Code**
```
1. Abra o VS Code
2. File → Open Folder
3. Escolha a pasta "meu-chatbot-ia"
```

#### **2.3 - Criar o arquivo**
```
1. No painel esquerdo, clique no ícone "New File" (+)
2. Digite: app.py
3. Aperte Enter
```

#### **2.4 - Colar o código**
```
1. Cole o código (o mesmo de cima)
2. Command + S para salvar
```

---

## 📄 CRIAR O SEGUNDO ARQUIVO: requirements.txt

### **No TextEdit:**
```
1. File → New (Command + N)
2. Cole isto:

streamlit
openai==0.28.0

3. File → Save As (Command + S)
   Save As: requirements.txt
   ☐ Desmarque: "If no extension is provided, use '.txt'"
   Where: pasta "meu-chatbot-ia"
   
4. Clique em "Save"
```

### **No VS Code:**
```
1. Clique no ícone "New File" (+)
2. Digite: requirements.txt
3. Cole:

streamlit
openai==0.28.0

4. Command + S para salvar
```

---

## ✅ VERIFICAR SE DEU CERTO

### **Método 1: Pelo Finder**
```
1. Abra o Finder
2. Vá até a pasta "meu-chatbot-ia"
3. Você deve ver:
   📄 app.py
   📄 requirements.txt
```

### **Método 2: Pelo Terminal**
```
1. Abra o Terminal (Command + Espaço → digite "Terminal")
2. Digite:

cd Desktop/meu-chatbot-ia
ls -la

3. Você deve ver algo como:
   app.py
   requirements.txt
```

---

## 🚨 PROBLEMAS COMUNS NO MAC

### ❌ **Problema: Arquivo salvou como app.py.txt**

**Solução:**
```
1. No Finder, clique com botão direito no arquivo
2. Escolha "Rename" (Renomear)
3. Apague o .txt do final
4. Deixe só: app.py
5. Confirme "Use .py"
```

### ❌ **Problema: TextEdit mostra formatação rica (negrito, cores)**

**Solução:**
```
1. Feche o arquivo
2. TextEdit → Preferences
3. Marque "Plain text"
4. Abra o arquivo novamente
```

### ❌ **Problema: Não consigo desmarcar "use .txt"**

**Solução:**
```
Quando for salvar:
1. No campo "Save As", digite o nome completo: app.py
2. Na parte de baixo, onde tem "Hide extension", mantenha DESMARCADO
3. Se aparecer um aviso, escolha "Use .py"
```

---

## 🎬 RESUMO VISUAL - PASSO A PASSO NO MAC
```
1. Command + Espaço
   ↓
2. Digite: TextEdit
   ↓
3. TextEdit → Preferences → Plain text ✅
   ↓
4. File → New (Command + N)
   ↓
5. Cole o código completo
   ↓
6. File → Save (Command + S)
   ↓
7. Nome: app.py
   Desmarque: "use .txt"
   Local: pasta meu-chatbot-ia
   ↓
8. Salvar
   ↓
9. Repetir para requirements.txt
   ↓
10. ✅ PRONTO!
```

---

## 📸 COMO DEVE ESTAR SUA PASTA
```
📁 meu-chatbot-ia/
   ├── 📄 app.py (código do chatbot, ~2 KB)
   └── 📄 requirements.txt (lista de bibliotecas, ~30 bytes)
```

---

## 🎯 PRÓXIMO PASSO

Depois que tiver os 2 arquivos criados:
```
✅ app.py está criado e salvo
✅ requirements.txt está criado e salvo
✅ Ambos estão na pasta "meu-chatbot-ia"

→ Vamos para o PASSO 2: Criar conta no GitHub!
