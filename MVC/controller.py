from view import view
from model import Model
from BotDAO import BotDAO

class controller:
    def __init__(self):
        self.__tela = View(self)
        self.__bot_dao = BotDAO()

    def iniciar(self):
        self.__tela.tela_bot()

        running = True
        while running:
            event, values = self.__tela.le_eventos()

            if event == sg.WIN_CLOSED
                self__bot_dao.dump()
                running = False