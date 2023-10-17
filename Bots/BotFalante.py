from Persistencia.Comando import Comando
from Bots.Bot import Bot
import pyttsx3

class BotFalante(Bot):
    def __init__(self, nome):
        # antigo
        # self.__comandos = [Comando("Repitindo pronúncias", None)]
        self.__comandos = [Comando("Repitir pronúncia", [Comando("O que quer que eu diga?", self.fala)])]
        super().__init__(nome,self.__comandos, "imagens/bot_talk.png")
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
        return "Olá, eu sou um bot falante gringo. Eu repito o que você quiser."   
    
    def fala(self, frase):
        self.run_voice(frase)
            
    def executa_comando(self, comando):
        print("Eu estou falando, não vou repetir de novo!")
        comando = input("O que quer que eu repita? ")
        self.run_voice(comando)

    def boas_vindas(self):
        return "Seja bem-vindo!"

    def despedida(self):
        self.run_voice("Adeus e tenha uma boa vida!")