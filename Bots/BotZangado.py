from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando

class BotZangado(Bot):
    def __init__(self,nome):
        self.__comandos = [Comando("SABER ONDE EU MORO", "VOCÊ É MALUCO, EU NAO MORO EM LUGAR NENHUM, EU SOU UM ROBÔ"),
                           Comando("SABER O MOTIVO DA MINHA EXISTENCIA", "olha... essa nem eu sei te responder... PORQUE SE FOR PRA CONVERSAR CONTIGO EU PREFIRO IR DE ALT + F4 LOGO")]
        super().__init__(nome,self.__comandos, "imagens/angry.jpg")

    def apresentacao(self):
        return "OLÁ, EU SOU O BOT ZANGADO, PQ VOCÊ ESTÁ ME INCOMODANDO?"
        
    def boas_vindas(self):
        return "SEJA MAL VINDO AO CHATBOT ZANGADO!"
        
    def despedida(self):
        return "VAI LOGO, NAO AGUENTO MAIS FICAR AQUI"
