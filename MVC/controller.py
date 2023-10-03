from view import View
from model import Model
from Persistencia.BotDAO import BotDAO
import PySimpleGUI as sg


class controller:
    def __init__(self):
        self.__tela = View(self)
        self.__bot_dao = BotDAO()

    def iniciar(self):
        self.__tela.tela_bot()

        running = True
        while running:
            event, values = self.__tela.le_eventos()

            if event == sg.WIN_CLOSED:
                self.__bot_dao.dump()
                running = False
            
            # elif event == ...