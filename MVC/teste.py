import PySimpleGUI as sg
from PIL import Image, ImageTk
import io

# Função para carregar e converter uma imagem em formato compatível com o PySimpleGUI
def load_image(filename):
    try:
        image = Image.open(filename)
        image.thumbnail((50, 50))
        bio = io.BytesIO()
        image.save(bio, format="GIF")
        return bio.getvalue()
    except Exception as e:
        print(f"Erro ao carregar a imagem: {str(e)}")
        return None

# Layout da janela
layout = [
    [sg.Text("Lista de Imagens")],
    [sg.Listbox(values=[], size=(50, 6), key="-LIST-", enable_events=True)],
    [sg.Image(data="", size=(50, 50), key="-IMAGE-")],
    [sg.Button("Sair")]
]

# Crie a janela
window = sg.Window("Exemplo de ListBox com Imagens", layout)

# Loop de eventos
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Sair":
        break

    if event == "-LIST-":
        selected_index = values["-LIST-"][0]
        image_filename = f"imagem_{selected_index}.png"  # Substitua pelo nome do arquivo da imagem
        image_data = load_image(image_filename)
        if image_data:
            window["-IMAGE-"].update(data=image_data)

window.close()
