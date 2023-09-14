from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando

class BotNerdola(Bot):
    def __init__(self, nome):
        self.__comandos = {1: Comando("Bom dia!", "Bom dia, como vai você?"),
                           2: Comando("Qual o seu nome?", f"Meu nome é {nome}"),
                           3: Comando("Qual sua idade?", "Minha idade é : 2 * 4 + 10 + cos(0)") }
        super().__init__(nome, self.__comandos)
        self.__nome = nome

    def apresentacao(self):
        print(f'Olá, eu sou o {self.__nome} e eu sei matemática!')

    def boas_vindas(self):
        print(f'Bem-vindo viajante, em que posso ajudá-lo?')

    def despedida(self):
        print('Adeus amigo, foi um prazer conversar com você. Por favor volte a falar comigo novamente, eu sou muito solitário...')
    
    def executa_comando(self, cmd):
        print(self.comandos[cmd].resposta)