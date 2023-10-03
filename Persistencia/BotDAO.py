from Bots.Bot import Bot
from DAO import DAO
from SistemaChatBot.Comando import Comando

class BotDAO(DAO):
    def __init__(self):
        super().__init__('comandos.pkl')

    def add(self, comando: Comando):
        if isinstance(comando, Comando) and (comando is not None):
            super().cache[comando.pergunta] = comando.resposta
            self.dump()
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
