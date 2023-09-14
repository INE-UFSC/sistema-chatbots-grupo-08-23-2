from abc import ABC, abstractmethod
import random as r
from SistemaChatBot.Comando import Comando

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
        for i, comando in enumerate(self.comandos, start=1):
            print(f"{i} - {comando.pergunta}")

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass
    
    def executa_comando(self, cmd):
        print(self.comandos[cmd-1].resposta)