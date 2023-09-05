from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos
        # self.comandos = {"O que é a vida?": "É uma maravilha!", "Comando 02": "Resposta 02", "Comando 03": "Resposta 03"}
        super().__init__(nome, comandos)

    #nao esquecer o decorator
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
        print("Olá, meu nome é BotFeliz da vida feliz.")
 
    def mostra_comandos(self):
        cmds_counter = 1
        for cmds in self.comandos.keys():
            print("{}- {}".format(cmds_counter, cmds))
            cmds_counter += 1            
            
    def executa_comando(self,cmd):
        print("Você disse ---> {}".format(cmd))
        print("Eu respondo ---> {}".format(self.comandos[cmd]))

    def boas_vindas(self):
        print("Bem-vindx ao meu ChatBot Feliz! :D")

    def despedida(self):
        print("Adeus e tenha uma boa vida!")