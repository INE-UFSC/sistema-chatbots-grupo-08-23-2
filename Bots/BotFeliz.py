from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome
        
        comandos = {"1- Fale uma frase motivadora": "A vida é uma maravilha", 
                    "2- Qual é o seu nome?": "Meu nome é {} e eu sou muito feliz!".format(self.__nome),
                    "3- Como você é feliz?": "Basta querer e pensar positivo sempre!"}
        
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