from Persistencia.BotDAO import BotDAO

class Model:
    def __init__(self, nome_empresa, bots) -> None:
        self.__bots = bots
        self.__nome_empresa = nome_empresa
        self.__bot_selecionado = bots[0] if len(bots) > 0 else None
        if len(self.__bot_selecionado.comandos) > 0:
            self.__comando_selecionado = self.__bot_selecionado.comandos[0]
        else:
            self.__comando_selecionado = None
        self.__DAO = BotDAO()

    @property
    def bots(self):
        return self.__bots
    
    @property
    def nome_empresa(self):
        return self.__nome_empresa
    
    @property
    def bot_selecionado(self):
        return self.__bot_selecionado
    
    @property
    def comando_selecionado(self):
        return self.__comando_selecionado
    
    @comando_selecionado.setter
    def comando_selecionado(self, val):
        self.__comando_selecionado = val
        
    @bot_selecionado.setter
    def bot_selecionado(self, val):
        self.__bot_selecionado = val
        
    def get_bot_by_nome(self, nome):
        for bot in self.bots:
            if bot.nome == nome:
                return bot
        return None
    
    def salvar_dados(self):
        self.__DAO.dump(self.__bot_selecionado, self.comando_selecionado)

    def carregar_dados(self):
        return self.__DAO.load()
