from Bots.Bot import Bot
from Persistencia.Comando import Comando

class BotFeliz(Bot):
    def __init__(self, nome):
        self.__comandos = [Comando("Fale uma frase motivadora", "A vida é uma maravilha"),
                           Comando("O que te deixa mais feliz?", "A vidaaaa!"),
                           Comando("Como você é feliz?", "Basta querer e pensar positivo sempre!")]
            
        super().__init__(nome, self.__comandos, "imagens/bot_happy.png")
        self.__nome = nome
        
    def apresentacao(self):
        return "Olá, meu nome é {} da vida feliz.".format(self.__nome)
            
    def boas_vindas(self):
        return "Bem-vindx ao meu ChatBot Feliz! :D"

    def despedida(self):
        return "Adeus e tenha uma boa vida!"
