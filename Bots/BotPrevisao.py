from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando
import requests

class BotPrevisao(Bot):
    
    def __init__(self, nome):
        comandos = [Comando("Qual a previsão do tempo para hoje?", None)]
        super().__init__(nome, comandos)
        self.__api_key = "73ea9c3f03a0479a384487c43d0de627"
        
    def executa_comando(self, cmd):
        while True:
            cidade = input("Digite o nome da cidade: (0 para sair)")
            if cidade == "0":
                break
            url = "https://api.openweathermap.org/data/2.5/weather?q=sao+paulo&appid={}&lang=pt_br".format(self.__api_key)
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                temperatura = dados["main"]["temp"] - 273.15
                print(f"A temperatura media de hoje em {cidade.title()} é de {temperatura:.2f}ºC")
            else:
                print("Erro ao acessar a API")
            
    def apresentacao(self):
        print("Olá! Estou aqui para te dar a previsão do tempo da região que desejar")
            
    def boas_vindas(self):
        print("Bem-vindx ao meu ChatBot Feliz! :D")

    def despedida(self):
        print("Adeus e tenha uma boa vida!")
