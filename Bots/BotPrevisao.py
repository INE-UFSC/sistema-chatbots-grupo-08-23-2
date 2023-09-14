from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando
import requests

class BotPrevisao(Bot):
    
    def __init__(self, nome):
        comandos = [Comando("Qual a previsão do tempo para hoje?", None),
                    Comando("Suas previsões são confiáveis?", "Mostro uma média das temperaturas diárias, apeneas")]
        super().__init__(nome, comandos)
        self.__api_key = "73ea9c3f03a0479a384487c43d0de627"
        
    def descobre_previsao(self, cidade):
        cidade = input("Digite o nome da cidade: (0) ")
        url = "https://api.openweathermap.org/data/2.5/weather?q=sao+paulo&appid={}&lang=pt_br".format(self.__api_key)
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            temperatura = dados["main"]["temp"] - 273.15
            print(f"A temperatura media de hoje em {cidade.title()} é de {temperatura:.2f}ºC")
        else:
            print("Erro ao acessar a API")
        
    def executa_comando(self, cmd):
        if self.comandos[cmd].resposta == None:
            self.descobre_previsao()
        else:
            print(self.comandos[cmd].resposta)
            
    def apresentacao(self):
        print("Olá! Estou aqui para te dar a previsão do tempo da região que desejar")
            
    def boas_vindas(self):
        print("Bem vindo ao bot de previsão do tempo!")

    def despedida(self):
        print("Cuidado com o tempo!")
