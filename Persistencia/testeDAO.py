import json

class JSONDAO:
    def __init__(self, file):
        self.__file = file
    
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file - file

    def read_data(self):
        with open(self.__file, 'r') as file:
            data = json.load(file)
            return data
        
    def write_data(self, data):
        with open(self.__file, 'w') as file:
            json.dump(data, file, indent=4)

    def list_comandos(self):
        data = self.read_data()
        return data.get('comandos', [])
    
    def add_comando(self, comando):
        data = self.read_data()
        comandos = data.get('comandos', [])
        comandos.append(comando)
        data['comando'] = comando
        self.write_data(data)

    def refresh_comando(self, pergunta, nova_informacao):
        data = self.read_data()
        comandos = data.get('comandos', [])
        for comando in comandos:
            if comando['pergunta'] == pergunta:
                comando.update(nova_informacao)
                break
        self.write_data(data)

    def delete_comando(self, pergunta):
        data = self.read_data()
        comandos = data.get('pessoas', [])
        comandos = [comando for comando in comandos if comando['pergunta'] != pergunta]
        data['comandos'] = comandos
        self.gravar_dados(data)

dao = JSONDAO('dados.json')