from SistemaChatBot.Comando import Comando
from Bots.Bot import Bot
import pyttsx3

class BotFalador(Bot):
    def __init__(self, nome, comandos):
        self.__comandos = {1: Comando("Quero um elogio do amigo falante", "Você é uma pessoa adorável."),
                           2: Comando("Modo papagaio: Repita o que eu digo.", "Test")}
        super().__init__(nome,self.__comandos)
        self.__comandos = comandos
        motor = pyttsx3.init()
        self.__motor = motor
        self.__motor.getProperty('voices')
        super().__init__(nome, comandos)
        
    def config_init(self):   
        self.__motor.setProperty('rate', 125)  
        self.__motor.setProperty('volume',1.0)     
        
        vozes = self.__motor.getProperty('voices')
        self.__motor.setProperty('voice', vozes[0].id)
        
    def run_voice(self, text):
        self.__motor.say(text)
        self.__motor.runAndWait()
        self.__motor.stop()
        
    def apresentacao(self):
        self.run_voice("Olá, meu nome é {}. Eu repito o que você quiser.".format(self.__nome))
 
    def mostra_comandos(self):
        cmds_counter = 1
        for cmds in self.comandos.keys():
            print("{}- {}".format(cmds_counter, cmds))
            cmds_counter += 1            
            
    def executa_comando(self,cmd):
        self.run_voice(self.comandos[cmd].resposta)

    def boas_vindas(self):
        self.run_voice("Seja bem-vindo!")

    def despedida(self):
        self.run_voice("Adeus e tenha uma boa vida!")