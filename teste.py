import tkinter as tk
import PySimpleGUI as sg
from Bots.BotFalante import BotFalante
from Bots.BotZangado import BotZangado
from Bots.BotNerdola import BotNerdola
from Bots.BotFeliz import BotFeliz
from Bots.BotPrevisao import BotPrevisao


def talk_with_chatbot(bot_selected):
    def selected_command_bot(selected): 
        select_int_comm = -1
        
        try:
            select_int_comm = int(selected)
        except:
            select_int_comm = -1
            
        for i, val in enumerate(bot_selected.comandos):
            if (select_int_comm != -1 and select_int_comm == i+1) or selected == val.pergunta:
                return i
        return None
    
    def on_submit(event=None):
        user_input = input_field.get()
        output_field.config(state='normal')
        output_field.insert('end', '\nEu: ' + user_input + '\n', 'red')
        com_bot = selected_command_bot(user_input)
        
        if user_input == str((len(bot_selected.comandos) + 1)) or user_input == "Não quero mais conversar!":
            output_field.insert('end', bot_selected.despedida(), 'blue')
        elif com_bot == None:
            output_field.insert('end', 'Desculpe, mas não entendi o que disse.\n', 'blue')
        else:
            output_field.insert('end', bot_selected.executa_comando(com_bot), 'blue')
            
        input_field.delete(0, 'end')
        output_field.config(state='disabled')

    root = tk.Tk()
    root.title("Chat")

    output_frame = tk.Frame(root)
    output_frame.pack(side='top', fill='both', expand=True)

    output_label = tk.Label(output_frame, text="Chat:")
    output_label.pack(side='left')

    output_field = tk.Text(output_frame, height="10")
    output_field.pack(side='left', fill='both', expand=True)
    output_field.config(state='disabled')
    output_field.tag_config('blue', foreground='blue')
    output_field.tag_config('red', foreground='red')
    output_field.config(font=("Futura", 16))
    
    output_field.config(state='normal')
    output_field.insert('end', bot_selected.boas_vindas(), 'blue')
    output_field.insert('end', "\nSelecione um comando para conversar comigo!", 'blue')
    comandos_str = ''
    for i, val in enumerate(bot_selected.comandos):
        comandos_str += f"\n---> {i+1}: {val.pergunta}"
    
    output_field.insert('end', comandos_str, 'blue')
    output_field.insert('end', f"\n---> {len(bot_selected.comandos) + 1}: Não quero mais conversar!", 'blue')

    input_frame = tk.Frame(root)
    input_frame.pack(side='bottom', fill='x')

    input_label = tk.Label(input_frame, text="Digite:")
    input_label.pack(side='left')

    input_field = tk.Entry(input_frame, width=150)
    input_field.pack(side='left')
    input_field.bind("<Return>", on_submit)

    submit_button = tk.Button(input_frame, text="Submit", command=on_submit)
    close_button = tk.Button(input_frame, text="Sair do Chat", command=root.destroy, background="red")
    submit_button.pack(side='left')
    close_button.pack(side='left')

    root.mainloop()

def select_bot(items, selected):
    for ev in list(map(lambda x: x.nome, items)):
        if ev == selected:
            window[ev].update(button_color="light steel blue")
        else:
            window[ev].update(button_color="azure4")
            
def talk_bot(bot):
    col = [[]]
    if bot != None:
        col.append([sg.Text("BOT: ", font=("Helvetica", 12, "bold"))])
        col.append([sg.Text(bot.boas_vindas(), key="-BOASVINDAS-")])
        col.append([sg.Input(default_text="Digite um comando")])
    return col        

def get_bot(items, bot):
    for b in items:
        if b.nome == bot:
            return b
    return None

items = [BotZangado("Zangado"), BotNerdola("Nerdola"), BotFeliz("Feliz"), BotFalante("Falante"), BotPrevisao("Previsão")]

column1 = [[sg.Button(item.nome, expand_x=True, key=item.nome, size=(25), button_color=("light steel blue" if item.nome == items[0].nome else "azure4"), font=("Helvetica", 10, "bold"))] for item in items]

column2 = [[]]
for i, item in enumerate(items):
    column = []
    column.append([sg.Text(item.nome, expand_x=True, justification='center', font=("Helvetica", 18, "bold"))])
    column.append([sg.Image(item.img_path, expand_x=True)])
    column.append([sg.Text(item.apresentacao(), expand_x=True, justification='center', font=("Helvetica", 12, "bold"))])
    column2[0].append(sg.Column(column, visible=(i==0), key=("Page", item.nome)))

column3 = [[sg.Button("Conversar agora!", key=("_SELECT_BOT_"), font=("Helvetica", 10, "bold") ), 
            sg.Button("Sair!", button_color="orange red", key="-SAIR-", font=("Helvetica", 10, "bold"))]]
selected_bot = items[0]

columnChatbot = [
                    [sg.Text("Bot: ", font=("Helvetica", 10, "bold"), background_color="red")],
                    [sg.Text(selected_bot.boas_vindas())],
                    [sg.Text("Digite um comando:")], 
                    [sg.Input()], 
                    [sg.Column([[sg.Button("Enviar", key="-ENVIARCOMANDO-")]], 
                        justification="right")]
                ]

columnInput = []

sg.theme('DarkBlue3')
layout = [[sg.Column(column1, justification="center", key="_COL01_"), 
           sg.VerticalSeparator(), 
           sg.Column(column2, vertical_alignment='top', justification="center", key="-COL02-", expand_x=True), 
           sg.Column(columnChatbot, vertical_alignment='top', justification="center", background_color="LightSteelBlue4", key=("Page", "-CHATBOT-"), visible=False),
        ],
          [sg.Column(column3, justification="right")]]

window = sg.Window('ChatBOT', layout=layout)
page = items[0].nome

while True:

    event, values = window.read()
        
    if event == '_SELECT_BOT_':
        print("selecionar")
        talk_with_chatbot(selected_bot)
    if event == sg.WIN_CLOSED or event == "-SAIR-":
        break
    elif event in list(map(lambda x: x.nome, items)):
        window[("Page", page)].update(visible=False)
        page = event
        selected_bot = get_bot(items, event)
        window[("Page", page)].update(visible=True)
        select_bot(items, event)

window.close()