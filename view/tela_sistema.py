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
        sg.theme('Reddit')
        dic = self.__controlador.relatorio_geral()
        string = ''
        string = string + 'Número pacientes: ' + str(dic['num_pacientes']) + '\n\n'
        string = string + 'Número enfermeiros: ' + str(dic['num_enfermeiros']) + '\n\n'
        string = string + 'Número vacinas: ' + str(dic['qtd_vacinas']) + '\n\n'
        string = string + 'Número vacinados em primeira dose: ' + str(dic['uma_dose']) + '\n\n'
        string = string + 'Número vacinados em segunda dose: ' + str(dic['duas_doses']) + '\n\n'
        sg.Popup('Posto de Saúde', string)

    def window_posto(self):
        sg.theme('Reddit')
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
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)
