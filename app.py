#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotNerdola import BotNerdola
from Bots.BotFalante import BotFalante
from Bots.BotPrevisao import BotPrevisao

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Zangado"), BotNerdola("Nerdola"), BotFeliz("Feliz"), BotFalante("Falante"), BotPrevisao("Previsão")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()