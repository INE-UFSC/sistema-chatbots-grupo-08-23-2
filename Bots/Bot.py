from abc import ABC, abstractmethod
from Persistencia.Comando import Comando

class Bot(ABC):

    def __init__(self, nome, comandos, img_path):
        self.__nome = nome
        self.__comandos = comandos
        self.__img_path = img_path

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome
        
    @property
    def comandos(self):
        return self.__comandos
    
    @comandos.setter
    def comandos(self,comandos):
        self.__comandos = comandos

    @property
    def img_path(self):
        return self.img_path

    @abstractmethod
    def boas_vindas():
        pass

    @abstractmethod
    def despedida():
        pass

    def mostra_comandos(self):
        for i, comando in enumerate(self.comandos, start=1):
            return f"{i} - {comando.pergunta}"

    def executa_comando(self, cmd):
        return self.comandos[cmd].resposta
