from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        self.__comandos = {1: "RECEBER UM BOAS-VINDAS", 2: "SABER ONDE EU MORO", 3: "SABER O MOTIVO DA MINHA EXISTENCIA", 4: "IR EMBORA(POR FAVOR ESCOLHA ESSE)"}
        super().__init__(nome,self.__comandos)
        self.__nome = nome

    def apresentacao(self):
        print("OLÁ, EU SOU O BOT ZANGADO, PQ VOCÊ ESTÁ ME INCOMODANDO?")
        
    def executa_comando(self,cmd):
        if cmd == 1:
            self.boas_vindas()
        elif cmd == 2:
            self.onde_moro()
        elif cmd == 3:
            self.minha_existencia()
        elif cmd == 4:
            self.despedida()

    def boas_vindas(self):
        print("SEJA MAL VINDO AO CHATBOT ZANGADO!")
    
    def onde_moro(self):
        print("VOCÊ É MALUCO, EU NAO MORO EM LUGAR NENHUM, EU SOU UM ROBÔ")
    
    def minha_existencia(self):
        print("olha... essa nem eu sei te responder... PORQUE SE FOR PRA CONVERSAR CONTIGO EU PREFIRO IR DE ALT + F4 LOGO")

    def despedida(self):
        print("ATÉ NUNCA MAIS!")
