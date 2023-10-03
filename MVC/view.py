import PySimpleGUI as sg
from PIL import Image 
import base64
import io

class view():
    
    def __init__(self, controler) -> None:
        self.__controler = controler
        self.__model = controler.model
        self.__container = []
        self.__window = sg.Window("ChatBot", self.__container)
        
    def import_img(self, bot):
        img_path = bot.img_path
        img = Image.open(img_path)
        imagem_io = io.BytesIO()
        img.save(imagem_io, format="PNG")
        imagem_base64 = base64.b64encode(imagem_io.getvalue()).decode("utf-8")
        return (imagem_base64)
        
    def initial_screen(self):
        imgs = []
        
        for bot in self.__model.__lista_bots:
            img = self.import_img(bot)
            imgs.append(img)
            
            
        self.__container = [
            [sg.Text("Olá, esse é o sistema de chatbots de {self.__model.__empresa}!", expand_x=True, justification='center')],
            [sg.Text("Os chat bots disponíveis no momento são:", expand_x=True, justification='center')],
        ]
        for i in self.__model.__lista_bots:
            temp = []
            for i, bot in enumerate(self.__model.__lista_bots):
                temp.append()
        