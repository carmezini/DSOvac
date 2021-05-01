from view.menu import Menu
import PySimpleGUI as sg

class TelaSistema():
    def __init__(self, controlador):
        self.init_components()
        self.__window = None
        self.__controlador = controlador

    def inicie(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['0'] or button in (None, 'Cancelar'):
            self.close()
        elif values['1']:
            self.__controlador.opcoes_paciente()
        elif values['2']:
            self.__controlador.opcoes_enfermeiro()
        elif values['3']:
            self.__controlador.opcoes_vacina()
        elif values['4']:
            self.__controlador.opcoes_agendamento()
        elif values['5']:
            self.exibir_relatorio_geral()
        self.close()
    
    def exibir_relatorio_geral(self):
        dic = self.__controlador.relatorio_geral()
        print(dic['nome'])
        print('Número pacientes: ', dic['num_pacientes'])
        print('número enfermeiros: ', dic['num_enfermeiros'])
        print('Número vacinas: ', dic['qtd_vacinas'])
        print('Número de vacinados em primeira dose: ', dic['uma_dose'])
        print('Número de vacinados em segunda dose: ', dic['duas_doses'])
    
    def close(self):
        self.__window.close()
    
    def init_components(self):
        sg.change_look_and_feel('DarkTeal4')
        layout = [
            [sg.Text('Posto de vacinação', font=('Helvica', 20))],
            [sg.Text('Escolha sua opção', font=('Helvica', 15))],
            [sg.Radio('Destruir posto',"RD1", key='0')],
            [sg.Radio('Opções paciente',"RD1", key='1')],
            [sg.Radio('Opções enfermeiro',"RD1", key='2')],
            [sg.Radio('Opções vacina',"RD1", key='3')],
            [sg.Radio('Opções agendamento',"RD1", key='4')],
            [sg.Radio('Relatório geral do posto',"RD1", key='5')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)
