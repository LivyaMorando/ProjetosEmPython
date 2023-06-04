# Simulador de dado - dado de RPG
#Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self): #definição das configurações iniciais
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        #layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        
    def Iniciar(self): 
        #janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #ler valores da tela e fazer algo com os valores
        #while True:
        try:
            self.evento, self.valores = self.janela.Read()
            if self.evento == 'Sim':
                self.GerarValorDoDado() 
            elif self.evento == 'Não':
                print('Agradecemos sua participação')
                    #break
            else:
                print("Favor difitar Sim ou Não")
        except:
                print('Ocorreu um erro ao receber sua resposta')
        
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo)) 

simulador = SimuladorDeDado() 
simulador.Iniciar()
