from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome
        
        comandos = {1: "Fale uma frase motivadora", 2: "O que te deixa mais feliz?",3: "Como você é feliz?",}
        
        self.__comandos = comandos
        super().__init__(nome)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def comandos(self):
        return self.__comandos
    
    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos
        
    def apresentacao(self):
        print("Olá, meu nome é {} da vida feliz.".format(self.__nome))
 
    def mostra_comandos(self):
        cmds_counter = 1
        for cmds in self.comandos.values():
            print("{}- {}".format(cmds_counter, cmds))
            cmds_counter += 1   
            
    def frase_motivadora(self):
        print("A vida é uma maravilha")
        
    def como_eh_feliz(self):
        print("Basta querer e pensar positivo sempre!")
        
    def oq_deixa_mais_feliz():
        print("a vidaaaa!")         
            
    def executa_comando(self,cmd):
        if cmd == 1:
            self.frase_motivadora()
        elif cmd == 2:
            self.oq_deixa_mais_feliz()
        elif cmd == 3:
            self.como_eh_feliz()

    def boas_vindas(self):
        print("Bem-vindx ao meu ChatBot Feliz! :D")

    def despedida(self):
        print("Adeus e tenha uma boa vida!")