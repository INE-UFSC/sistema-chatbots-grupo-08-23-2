import PySimpleGUI as sg
import tkinter as tk
from MVC.model import Model
from MVC.view import View
from MVC.controller import Controller

from Bots.BotFalante import BotFalante
from Bots.BotZangado import BotZangado
from Bots.BotNerdola import BotNerdola
from Bots.BotFeliz import BotFeliz
from Bots.BotPrevisao import BotPrevisao

class MainApplication():
    def __init__(self):
        bots = [BotZangado("Zangado"), BotNerdola("Nerdola"), BotFeliz("Feliz"), BotFalante("Falante"), BotPrevisao("Previsão")]
        model = Model("Empresa de Bots", bots)
        
        controller = Controller(model=model, view=None)
        view = View(controller)
        controller.view = view
        
        self.view = view
        
    def init(self):
        self.view.init()
       
mainApp = MainApplication()
mainApp.init()