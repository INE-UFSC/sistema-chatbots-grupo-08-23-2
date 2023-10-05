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
        ]
        cont = 0
        for line in range(len(math.ceil(lista_bots)/self.__itens_por_linha)):
            linha = []
            for item in range(self.__itens_por_linha):
                img = self.import_imgs(lista_bots[cont].img_path)
                item = [
                    [sg.Text(f"{lista_bots[cont].nome}", expand_x=True, justification='center')],
                    [sg.Image(data=img)]
                ]
                cont += 1
                linha.append(item)
            self.__container.append(linha)
        self.__container.append([sg.Button("Escolher Bot", key='escolher_bot')])