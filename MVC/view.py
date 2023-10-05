import PySimpleGUI as sg
from PIL import Image 
import base64, io, math

class view():
    
    def __init__(self, controler) -> None:
        self.__controler = controler
        self.__model = controler.model
        self.__container = []
        self.__window = sg.Window("ChatBot", self.__container)
        self.__itens_por_linha = 3
        
    def import_imgs(self, bot):
        img_path = bot.img_path
        img = Image.open(img_path)
        imagem_io = io.BytesIO()
        img.save(imagem_io, format="PNG")
        imagem_base64 = base64.b64encode(imagem_io.getvalue()).decode("utf-8")
        return imagem_base64
        
    def initial_screen(self):
        
        lista_bots = self.__model.lista_bots
  
        self.__container = [
            [sg.Text(f"Olá, esse é o sistema de chatbots de {self.__model.__empresa}!", expand_x=True, justification='center')],
            [sg.Text("Os chat bots disponíveis no momento são:", expand_x=True, justification='center')],
            [sg.Button(
                [sg.Text(f"{lista_bots[0].nome}", expand_x=True, justification='center')],
                [sg.Image(data=self.import_imgs(lista_bots[0]))]
                [sg.Text(f"{lista_bots[0].apresentacao}", expand_x=True, justification='center')],
            )]
        ]
        for i in range(len(self.__model.lista_bots)[::self.__itens_por_linha]):
            collum = []
            for
            self.collum.append([sg.Button(
                [sg.Text(f"{lista_bots[i].nome}", expand_x=True, justification='center')],
                [sg.Image(data=self.import_imgs(lista_bots[i]))]
                [sg.Text(f"{lista_bots[i].apresentacao}", expand_x=True, justification='center')],
            )])