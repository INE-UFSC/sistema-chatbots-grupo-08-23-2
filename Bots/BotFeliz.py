from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando

class BotFeliz(Bot):
    def __init__(self, nome):
        self.__comandos = [Comando("Fale uma frase motivadora", "A vida é uma maravilha"),
                           Comando("O que te deixa mais feliz?", "A vidaaaa!"),
                           Comando("Como você é feliz?", "Basta querer e pensar positivo sempre!")]
            
        super().__init__(nome, self.__comandos, "imagens/img_feliz.png")
        self.__nome = nome
        
    def apresentacao(self):
        print("Olá, meu nome é {} da vida feliz.".format(self.__nome))
            
    def boas_vindas(self):
        print("Bem-vindx ao meu ChatBot Feliz! :D")

    def despedida(self):
        print("Adeus e tenha uma boa vida!")
