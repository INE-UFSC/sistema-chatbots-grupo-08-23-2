from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.nome = nome
        self.comandos = comandos

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

    def mostra_comandos(self):
        for i, comando in (self.comandos.items()):
            print(f"{i} - {comando}")

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass