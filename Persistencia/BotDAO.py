from Persistencia.DAO import DAO


class BotDAO(DAO):
    def __init__(self):
        super().__init__('comandos.json')

    def add(self, bot, comando):
        super().cache[bot] = comando
        self.dump()
    
    def remove(self, bot):
        return super().remove(bot)