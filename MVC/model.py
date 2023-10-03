import json

from SistemaChatBot.Comando import Comando
from Bots.BotFalante import BotFalante
from Bots.BotFeliz import BotFeliz
from Bots.BotNerdola import BotNerdola
from Bots.BotZangado import BotZangado

class Model(object):
    def __init__(self, resquest_key: int) -> None:
        self.__request_key = resquest_key
        self.__answer = None

    