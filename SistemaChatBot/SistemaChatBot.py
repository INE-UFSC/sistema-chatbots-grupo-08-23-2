from Bots.Bot import Bot
from Bots.BotZangado import BotZangado

class SistemaChatBot:
    def __init__(self,nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__lista_bots = []
        for bot in lista_bots:
            if type(bot) == Bot:
                self.__lista_bots.append(bot)
        self.__bot = None
        self.__mensagens_comandos =  ["Bom dia", "Qual o seu nome?", "Quero um conselho", "Adeus"]
        self.__comandos = ['bom_dia', 'qual_nome', 'conselho', 'adeus'] ### CONFIRMAR COM OS OUTROS DEPOIS   
    
    @property
    def bot(self):
        return self.__bot
    
    @bot.setter
    def bot(self, bot):
        self.__bot = bot
    
    def boas_vindas(self):
        print(f"Olá, esse é o sistema de chatbots de {self.__empresa}!")

    def mostra_menu(self):
        print("Os chat bots disponíveis no momento são:")
        for i, bot in enumerate(self.__lista_bots):
            print(f"{i+1} - Bot: {bot.nome()} - Mensagem de apresentação: {bot.apresentacao()}")
    
    def escolhe_bot(self):
        while True:
            opcao = int(input("Digite o número do chatbot desejado: "))
            if 1 <= opcao <= len(self.__lista_bots):
                break
        self.bot(self.__lista_bots[opcao-1])
        

    def mostra_comandos_bot(self):
        for i, comando in enumerate(self.__mensagens_comandos):
            print(f"{i+1} - {comando}")

    def le_envia_comando(self):
        comando = int(input("Digite o comando desejado: "))
        if comando == -1:
            return False
        self.__bot.executa_comando(self.__comandos[comando-1]) 
        return True

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.boas_vindas()
        while True:
            self.mostra_comandos_bot()
            comando = self.le_envia_comando()
            if comando == False:
                break
        self.bot.despedida()