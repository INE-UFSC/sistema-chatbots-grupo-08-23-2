from MVC.model import Model
from MVC.view import View
from MVC.model import Model


class Controller: 
    def __init__(self, model, view):
        self.__model = model
        self.__view = view
        
    @property
    def model(self):
        return self.__model
    
    @property
    def view(self):
        return self.__view
    
    @view.setter
    def view(self, new_view):
        self.__view = new_view
    
    def bots(self):
        return self.model.bots
    
    def bot_selecionado(self):
        return self.model.bot_selecionado
    
    def comando_selecionado(self):
        return self.model.comando_selecionado

    def set_comando_selecionado(self, val):
        self.model.comando_selecionado = val
        
    def get_bot_by_nome(self, nome):
        return self.model.get_bot_by_nome(nome)