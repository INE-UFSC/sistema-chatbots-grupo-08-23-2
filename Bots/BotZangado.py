from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando

class BotZangado(Bot):
    def __init__(self,nome):
        self.__comandos = {1: Comando("SABER ONDE EU MORO", "VOCÊ É MALUCO, EU NAO MORO EM LUGAR NENHUM, EU SOU UM ROBÔ"),
                           2: Comando("SABER O MOTIVO DA MINHA EXISTENCIA", "olha... essa nem eu sei te responder... PORQUE SE FOR PRA CONVERSAR CONTIGO EU PREFIRO IR DE ALT + F4 LOGO")}
        super().__init__(nome,self.__comandos)
        self.__nome = nome

    def apresentacao(self):
        print("OLÁ, EU SOU O BOT ZANGADO, PQ VOCÊ ESTÁ ME INCOMODANDO?")
        
    def boas_vindas(self):
        print("SEJA MAL VINDO AO CHATBOT ZANGADO!")
        
    def executa_comando(self,cmd):
        print(self.comandos[cmd].resposta)
        
    def despedida(self):
        print("VAI LOGO, NAO AGUENTO MAIS FICAR AQUI")