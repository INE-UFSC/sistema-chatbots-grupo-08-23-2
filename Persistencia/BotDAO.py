from DAO import DAO
# from Comando import Comando
# from Bots.Bot import Bot
# from Bots.BotFeliz import BotFeliz


class BotDAO(DAO):
    def __init__(self):
        super().__init__('comandos.json')

    # def add(self, bot: Bot, comando: tuple):
    #     if isinstance(bot, Bot):
    #         super().cache[bot.nome] = comando
    #         self.dump()
    
    # def remove(self, bot: Bot):
    #     if isinstance(bot, Bot):
    #         return super().remove(bot.nome)

    def add(self, bot, comando):
        super().cache[bot] = comando
        self.dump()
    
    def remove(self, bot):
        return super().remove(bot)
    
botdao = BotDAO()
botdao.add("1", "2")
print(botdao.get_all())
