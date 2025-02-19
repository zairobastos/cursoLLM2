import streamlit as st 
from gemini import Gemini

st.sidebar.title("Configurações")


modelo = st.sidebar.selectbox("Modelo", ["models/gemini-1.5-pro-latest", "lm-studio"])
temperatura = st.sidebar.slider(label="Temperatura", min_value=0.0, max_value=1.0, value=0.8, step=0.01)
top_k = st.sidebar.slider("Top K", 1, 100)
top_p = st.sidebar.slider(label="Top P", min_value=0.0, max_value=1.0, value=0.8, step=0.01)

prompt = st.text_area("Prompt")
botao = st.button("Gerar resposta")
if prompt != "":
	gemini = Gemini(prompt, modelo, temperatura, top_k, top_p)
	if botao:
		resposta, qtd_tokens_perguntas, qtd_tokens_resposta, tempo = gemini.geracao_resposta()
		col1, col2, col3 = st.columns(3)
		tempo = round(tempo, 2)
		col1.metric("Tokens pergunta", qtd_tokens_perguntas)
		col2.metric("Tokens resposta", qtd_tokens_resposta)
		col3.metric("Tempo", f"{tempo} s")

		st.code(resposta, language="python", line_numbers=True)