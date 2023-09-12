from Bots.Bot import Bot
class BotNerdola(Bot):
    def __init__(self, nome):
        self.__comandos = {1: 'Bom dia!', 2: 'Qual o seu nome?', 3: 'Qual sua idade?', 4: 'Adeus'}
        super().__init__(nome, self.__comandos)
        self.__nome = nome

    def apresentacao(self):
        print(f'Olá, eu sou o {self.__nome} e eu sei matemática!')

    def bom_dia(self):
        print('Bom dia, como vai você?')

    def qual_seu_nome(self):
        print(self.__nome)

    def qual_sua_idade(self):
        print(f'Minha idade é : 2 * 4 + 10 + cos(0)')


    def executa_comando(self, cmd):
        if cmd == 1:
            self.bom_dia()

        elif cmd == 2:
            self.qual_seu_nome()

        elif cmd == 3:
            self.qual_sua_idade()

        elif cmd == 4:
            self.despedida()

        else:
            print(f'Por favor selecione uma opção válida, bocó')

    def boas_vindas(self):
        print(f'Bem-vindo viajante, em que posso ajudá-lo?')

    def despedida(self):
        print('Adeus amigo, foi um prazer conversar com você. Por favor volte a falar comigo novamente, eu sou muito solitário...')