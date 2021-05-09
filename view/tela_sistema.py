from view.menu import Menu
import PySimpleGUI as sg

class TelaSistema():
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador

    def opcoes_tela(self):
        self.window_posto()
        button, event, values = sg.read_all_windows()
        opcao = 0
        if values['0'] or button in (None, 'Cancelar') or sg.WIN_CLOSED == event:
            opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
        self.close()
        return opcao

    def close(self):
        self.__window.close()

    def exibir_relatorio_geral(self):
        sg.theme('TealMono')
        dic = self.__controlador.relatorio_geral()
        string = '---------------------------------------- \n\n'
        string = string + 'Número pacientes: ' + str(dic['num_pacientes']) + '\n\n'
        string = string + 'Número enfermeiros: ' + str(dic['num_enfermeiros']) + '\n\n'
        string = string + 'Número vacinas: ' + str(dic['qtd_vacinas']) + '\n\n'
        string = string + 'Número vacinados em primeira dose: ' + str(dic['uma_dose']) + '\n\n'
        string = string + 'Número vacinados em segunda dose: ' + str(dic['duas_doses']) + '\n\n'
        sg.Popup('Relatório Geral do Posto', string, font=('Verdana', 13))

    def window_posto(self):
        sg.theme('Material1')
        layout = [
            [sg.Text('Escolha sua opção', font=('Verdana', 16))],
            [sg.Text('----------------------------------------------------------')],
            [sg.Radio('Finalizar sistema',"RD1", key='0', font=('Verdana', 13))],
            [sg.Radio('Opções paciente',"RD1", key='1', font=('Verdana', 13))],
            [sg.Radio('Opções enfermeiro',"RD1", key='2', font=('Verdana', 13))],
            [sg.Radio('Opções vacina',"RD1", key='3', font=('Verdana', 13))],
            [sg.Radio('Opções agendamento',"RD1", key='4', font=('Verdana', 13))],
            [sg.Radio('Relatório geral do posto',"RD1", key='5', font=('Verdana', 13))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, size=(300, 300), finalize=True)
