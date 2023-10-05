import json

from Bots.BotFeliz import BotFeliz
from Bots.BotNerdola import BotNerdola
from Bots.BotZangado import BotZangado

from SistemaChatBot.Comando import Comando


class Model(object):
    # A __lista_bots vai ser inicializada como uma lista vazia
    # __bot também vai ser inicializado sem valor
    def __init__(self) -> None: # Adicionar lista_bots como parametro depois
        self.__empresa = 'CrazyBots'
        self.__lista_bots = [
            BotFeliz('Felizinho'),
            BotNerdola('Nerdolinha'),
            BotZangado('Zangadinho')
            ]
        self.__bot = BotNerdola('Nerdolasso') #self.__lista_bots[2]
        self.__comando = None

    # Função para dar boas-vindas ao usuário
    def boas_vindas(self) -> str:
        return f'Olá, este é o sistema de chatbots da {self.__empresa}!'

    # Função que retorna uma string com todos os bots disponíveis no momento
    def menu(self) -> str:
        bots_disponiveis = f'Estes são os bots disponíveis:\n\n'
        for i, bot in enumerate(self.__lista_bots, start=1):
            bots_disponiveis += f'{i} - {bot.nome}\n{bot.apresentacao()}\n\n'
        return bots_disponiveis

    # Função que possibilita o usuário a escolher o bot desejado
    # Esta função verifica se o valor digitado está no range da lista
    # Esta função também verifica se o valor recebido é um inteiro, caso não seja uma exceção é levantada
    def escolher_bot(self) -> None:
        while True:
            try:
                opcao = int(input('Digite o número do chatbot desejado: '))
                if 1 <= opcao <= len(self.__lista_bots):
                    self.__bot = self.__lista_bots[opcao-1]
                else:
                    print('Bot inválido.')
            except ValueError:
                print('Por favor, insira um número inteiro.')

    # Esta função mostra os comando do bot escolhido
    def mostrar_comandos_bot(self):
        return self.__bot.mostra_comandos()

    # Essa função vai ler o comando desejado do usuário e armazenar na
    # variável self.__comando da classe para que possa ser executada pela
    # função executar_comando() quando for necessário
    def ler_comando(self) -> None:
        while True:
            try:
                comando = int(input('Digite o número do comando desejado: '))

                if comando == -1:
                    break

                if 1 <= comando <= len(self.__bot.comandos):
                    self.__comando = comando - 1
                else:
                    print('Comando inválido.')
            except ValueError:
                print('Por favor, insira um número inteiro.')

    # Função para executar o comando desejado
    def executar_comando(self):
        self.__bot.executa_comando(self.__comando)

    def inicio(self) -> None:
        print(self.boas_vindas())
        print(self.menu())