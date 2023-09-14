from SistemaChatBot.Comando import Comando
from Bots.Bot import Bot
import pyttsx3

class BotFalante(Bot):
    def __init__(self, nome):
        self.__comandos = [Comando("Quero um elogio do amigo falante gringo", "You are beautiful."),
                           Comando("Repitindo pronúncias", "I'm Erika")]
        super().__init__(nome,self.__comandos)
        motor = pyttsx3.init()
        self.__motor = motor
        self.__motor.getProperty('voices')
        
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
        print("Olá, eu sou um bot falante gringo. Eu repito o que você quiser.")        
            
    def executa_comando(self,cmd):
        print("Eu estou falando, não vou repetir de novo!")
        self.run_voice(self.comandos[cmd-1].resposta)

    def boas_vindas(self):
        print("Seja bem-vindo!")

    def despedida(self):
        self.run_voice("Adeus e tenha uma boa vida!")