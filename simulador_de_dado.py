# Simulador de Dado
#simular uso de um dado gerando um valor de 1 - 6

import random

import PySimpleGUI as sg


class simuladorDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        #criar layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),
             sg.Button('não')]
        ]



    def Iniciar(self):
        # criar uma janela

        self.janela = sg.Window('simulador de dado', layout=self.layout)
        # ler os valores da tela

        self.eventos, self.valores = self.janela.Read()

        # fazer alguma coisa com esses valore
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.gerarValorDoDado()
            elif self.eventos == 'n' or self.eventos == 'não':
                print('Agradecemos sua participação')
            else:
                print('favor digitar sim ou nao')
        except:
            print('Ocorreu um erro ao receber sua resposta')



           
    def gerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
        
simulador = simuladorDado()
simulador.Iniciar()
        
        