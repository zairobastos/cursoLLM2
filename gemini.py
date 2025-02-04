import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

chave = os.getenv("API_KEY")

genai.configure(api_key=chave)

modelos = [m.name for m in genai.list_models()]

print("Modelos: ")
for modelo in enumerate(modelos):
    print(f"{modelo[0]} - {modelo[1]}")

selecione_modelo = int(input("Selecione o modelo: "))
modelo = modelos[selecione_modelo]


model = genai.GenerativeModel(modelo)
inicio = time.time()

pergunta = "Fale sobre a importância da educação para a sociedade."

response = model.generate_content(pergunta)

tokens_pergunta = str(model.count_tokens(pergunta))
qtd_tokens_perguntas = int(tokens_pergunta.split(" ")[1])

tokens_resposta = str(model.count_tokens(response.text))
qtd_tokens_resposta = int(tokens_resposta.split(" ")[1])

fim = time.time()
print(response.text)
print(f"Tempo de resposta: {fim - inicio} segundos")

print(f"Tokens pergunta: {qtd_tokens_perguntas}")
print(f"Tokens resposta: {qtd_tokens_resposta}")
