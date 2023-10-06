class Comando:
    
    def __init__(self, pergunta, resposta):
        self.__pergunta = pergunta
        self.__resposta = resposta
        
    @property
    def pergunta(self):
        return self.__pergunta
    
    @pergunta.setter
    def pergunta(self, pergunta):
        self.__pergunta = pergunta
        
    @property
    def resposta(self):
        return self.__resposta
    
    @resposta.setter
    def resposta(self, resposta):
        self.__resposta = resposta