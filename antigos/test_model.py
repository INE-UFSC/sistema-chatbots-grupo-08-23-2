from MVC.model import Model

from Bots.BotZangado import BotZangado
from Bots.BotNerdola import BotNerdola
from Bots.BotFeliz import BotFeliz


bots_list = [BotFeliz('Felizinho'),
BotNerdola('Nerdolinha'),
BotZangado('Zangadinho')]

model = Model('CrazyBots', bots_list)
print(model.boas_vindas())
print(model.menu())
print(model.escolher_bot())
