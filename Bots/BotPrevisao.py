from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando
import requests

class BotPrevisao(Bot):
    
    def __init__(self, nome):
        comandos = [Comando("Qual a previsão do tempo para hoje?", None),
                    Comando("Suas previsões são confiáveis?", "Mostro uma média das temperaturas diárias, apenas")]
        super().__init__(nome, comandos,"imagens/bot_weather.png")
        self.__api_key = "73ea9c3f03a0479a384487c43d0de627"
        
    def descobre_previsao(self):
        cidade = input("Digite o nome da cidade: ")
        url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={self.__api_key}&lang=pt_br)'
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            temperatura = dados["main"]["temp"] - 273.15
            return f"\nA temperatura media de hoje em {cidade.title()} é de {temperatura:.2f}ºC"
        else:
            return "Erro ao acessar a API"
        
    def executa_comando(self, cmd):
        if self.comandos[cmd].resposta == None:
            self.descobre_previsao()
        else:
            return self.comandos[cmd].resposta
            
    def apresentacao(self):
        return "Olá! Estou aqui para te dar a previsão do tempo da região que desejar"
            
    def boas_vindas(self):
        return "Bem vindo ao bot de previsão do tempo!"

    def despedida(self):
        return "Cuidado com o tempo!"
