# import tkinter as tk
# import datetime
# class ChatbotTkinter:
#     def __init__(self, bot_selected) -> None:
#         self.__bot_selected = bot_selected
        
#     @property
#     def bot_selected(self):
#         return self.__bot_selected
    
#     def selected_command_bot(self, selected): 
#         select_int_comm = -1
        
#         try:
#             select_int_comm = int(selected)
#         except:
#             select_int_comm = -1
            
#         for i, val in enumerate(self.bot_selected.comandos):
#             if (select_int_comm != -1 and select_int_comm == i+1) or selected == val.pergunta:
#                 return val
#         return None
    
#     def on_submit(self, input_field, output_field, event=None):
#         user_input = input_field.get()
#         output_field.config(state='normal')
#         output_field.insert('end', '\nUser: ' + user_input + '\n', 'red')
#         com_bot = self.selected_command_bot(user_input)
        
#         if user_input == str((len(self.bot_selected.comandos) + 1)) or user_input == "Não quero mais conversar!":
#             output_field.insert('end', self.bot_selected.despedida(), 'blue')
#         elif com_bot == None:
#             output_field.insert('end', 'Desculpe, mas não entendi o que disse.\n', 'blue')
#         else:
#             output_field.insert('end', com_bot.resposta, 'blue')
            
#         input_field.delete(0, 'end')
#         output_field.config(state='disabled')
        
#     def init(self):
#         root = tk.Tk()
#         root.title("Chatbot")

#         output_frame = tk.Frame(root)
#         output_frame.pack(side='top', fill='both', expand=True)

#         output_label = tk.Label(output_frame, text="Chatbot:")
#         output_label.pack(side='left', padx=5, pady=5)

#         output_field = tk.Text(output_frame)
#         output_field.pack(side='left', fill='both', expand=True, padx=5, pady=5)
#         output_field.config(state='disabled')
#         output_field.tag_config('blue', foreground='blue')
#         output_field.tag_config('red', foreground='red')
#         output_field.config(font=("Futura", 16))
        
#         output_field.config(state='normal')
#         output_field.insert('end', self.bot_selected.boas_vindas(), 'blue')
#         output_field.insert('end', "\nSelecione um comando para conversar comigo!", 'blue')
#         comandos_str = ''
#         for i, val in enumerate(self.bot_selected.comandos):
#             comandos_str += f"\n---> {i+1}: {val.pergunta}"
        
#         output_field.insert('end', comandos_str, 'blue')
#         output_field.insert('end', f"\n---> {len(self.bot_selected.comandos) + 1}: Não quero mais conversar!", 'blue')

#         input_frame = tk.Frame(root)
#         input_frame.pack(side='bottom', fill='x')

#         input_label = tk.Label(input_frame, text="User:")
#         input_label.pack(side='left', padx=5, pady=5)

#         input_field = tk.Entry(input_frame, width=150)
#         input_field.pack(side='left', padx=5, pady=5)
#         input_field.bind("<Return>", self.on_submit(input_field, output_field))

#         submit_button = tk.Button(input_frame, text="Submit", command=self.on_submit(input_field, output_field))
#         close_button = tk.Button(input_frame, text="Sair do Chat", command=root.destroy, background="red")
#         submit_button.pack(side='left')
#         close_button.pack(side='left')

#         root.mainloop()