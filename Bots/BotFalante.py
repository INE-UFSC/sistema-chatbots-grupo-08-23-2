from Bots.Bot import Bot
import pyttsx3

class BotFalador(Bot):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos
        motor = pyttsx3.init()
        self.__motor = motor
        self.__vozes = motor.getProperty('voices')
        super().__init__(nome, comandos)
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def motor(self):
        return self.__motor
    
    @nome.setter
    def motor(self, motor):
        self.__motor = motor
        
    @property
    def comandos(self):
        return self.__comandos
    
    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos
        
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
        self.run_voice("Olá, meu nome é BotFalador. Fale e eu repito.")
 
    def mostra_comandos(self):
        cmds_counter = 1
        for cmds in self.comandos.keys():
            print("{}- {}".format(cmds_counter, cmds))
            cmds_counter += 1            
            
    def executa_comando(self,cmd):
        self.run_voice(self.get_comandos()[cmd])

    def boas_vindas(self):
        self.run_voice("Seja bem-vindo!")
        

    def despedida(self):
        self.run_voice("Adeus e tenha uma boa vida!")