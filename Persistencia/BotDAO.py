from Persistencia.DAO import DAO


class BotDAO(DAO):
    def __init__(self):
        super().__init__('nome_empresa.json')

    def add(self, id ,nome_empresa):
        super().cache[id] = nome_empresa
        self.dump()
    
    def remove(self, nome_empresa):
        return super().remove(nome_empresa)