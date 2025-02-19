import google.generativeai as genai
import os
import time
from dotenv import load_dotenv



class Gemini:
	def __init__(self, prompt:str="", modelo:str="models/gemini-1.5-pro-latest", temperatura:float=0.8, top_k:int=20, top_p:float=0.8):
		"""Classe para configurar e gerar respostas com o modelo Gemini

		Args:
			prompt (str, optional): Prompt que o usuário definiu. Defaults to "".
			modelo (str, optional): Modelo quefoi selecionado para a geração da resposta. Defaults to "models/gemini-1.5-pro-latest".
			temperatura (float, optional): Nível de criatividade da resposta. Defaults to 0.8.
			top_k (int, optional): Limitante de resposta provável. Defaults to 20.
			top_p (float, optional): Limitante de resposta provável. Defaults to 0.8.
		"""
		self.prompt = prompt
		self.modelo = modelo
		self.temperatura = temperatura
		self.top_k = top_k
		self.top_p = top_p

	def config_gemini(self):
		load_dotenv()
		chave = os.getenv("API_KEY")
		if chave is None:
			raise Exception("Chave de API não encontrada")
		
		genai.configure(
			api_key=chave
		)

		return genai

	def geracao_resposta(self)-> tuple[str, int, int, int]:
		"""Geração da resposta com o modelo Gemini

		Returns:
			tuple[str, int, int, int]: Retorna a resposta gerada, a quantidade de tokens da pergunta, a quantidade de tokens da resposta e o tempo de resposta
		"""
		model = self.config_gemini()
		inicio = time.time()
		gemini = model.GenerativeModel(
			model_name=self.modelo,
			generation_config={
				"temperature": self.temperatura,
				"top_k": self.top_k,
				"top_p": self.top_p
			}
		)
		response = gemini.generate_content(self.prompt)
		tokens_pergunta = str(gemini.count_tokens(self.prompt))
		qtd_tokens_perguntas = int(tokens_pergunta.split(" ")[1])

		tokens_resposta = str(gemini.count_tokens(response.text))
		qtd_tokens_resposta = int(tokens_resposta.split(" ")[1])

		fim = time.time()
		tempo = fim - inicio

		return response.text, qtd_tokens_perguntas, qtd_tokens_resposta, tempo