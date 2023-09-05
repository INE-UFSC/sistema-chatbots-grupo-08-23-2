from Bots.Bot import Bot
import pyttsx3

class BotFalador(Bot):
    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos
        super().__init__(nome, comandos)
        
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
        # CONFIG
        motor = pyttsx3.init()

        rate = motor.getProperty('rate')   
        print (rate)                       
        motor.setProperty('rate', 125)  
        
        volume = motor.getProperty('volume')
        print (volume)                      
        motor.setProperty('volume',1.0)     
        
        vozes = motor.getProperty('voices')
        motor.setProperty('voice', vozes[0].id)
        
        motor.say("Olá, meu nome é BotFalador. Fale e eu repito.")
        motor.runAndWait()
        motor.stop()
 
    def mostra_comandos(self):
        cmds_counter = 1
        for cmds in self.comandos.keys():
            print("{}- {}".format(cmds_counter, cmds))
            cmds_counter += 1            
            
    def executa_comando(self,cmd):
        print("Você disse ---> {}".format(cmd))
        print("Eu respondo ---> {}".format(self.comandos[cmd]))
        # CONFIG
        motor = pyttsx3.init()

        rate = motor.getProperty('rate')   
        print (rate)                       
        motor.setProperty('rate', 125)  
        
        volume = motor.getProperty('volume')
        print (volume)                      
        motor.setProperty('volume',1.0)     
        
        vozes = motor.getProperty('voices')
        motor.setProperty('voice', vozes[0].id)
        
        motor.say("Você disse " + cmd)
        motor.say("E eu respondo " + self.get_comandos()[cmd])
        motor.runAndWait()
        motor.stop()

    def boas_vindas(self):
        # CONFIG
        motor = pyttsx3.init()

        rate = motor.getProperty('rate')   
        print (rate)                       
        motor.setProperty('rate', 125)  
        
        volume = motor.getProperty('volume')
        print (volume)                      
        motor.setProperty('volume',1.0)     
        
        vozes = motor.getProperty('voices')
        motor.setProperty('voice', vozes[0].id)
        
        motor.say("Seja bem-vindo!")
        motor.runAndWait()
        motor.stop()
        

    def despedida(self):
        print("Adeus e tenha uma boa vida!")