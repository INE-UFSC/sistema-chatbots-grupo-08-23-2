from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando

class BotNerdola(Bot):
    def __init__(self, nome):
        self.__comandos = [Comando("Bom dia!", "Bom dia, como vai você?"),
                           Comando("Qual o seu nome?", f"Meu nome é {nome}"),
                           Comando("Qual sua idade?", "Minha idade é : 2 * 4 + 10 + cos(0)")]
        super().__init__(nome, self.__comandos,  "imagens/bot_nerd.png")
        self.__nome = nome

    def apresentacao(self):
        return f'Olá, eu sou o {self.__nome} e eu sei matemática!'

    def boas_vindas(self):
        return f'Bem-vindo viajante, em que posso ajudá-lo?'

    def despedida(self):
        return 'Adeus amigo, foi um prazer conversar com você. Por favor volte a falar comigo novamente, eu sou muito solitário...'
