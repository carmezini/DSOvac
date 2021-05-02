from view.menu import Menu
import PySimpleGUI as sg

class TelaSistema():
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador

    def opcoes_tela(self):
        self.window_posto()
        button, values = self.__window.Read()
        window, event, values = sg.read_all_windows()
        opcao = 0
        if values['0'] or button in (None, 'Cancelar') or sg.WIN_CLOSED == event:
            opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        self.close()
        return opcao
    
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
            [sg.Button('Continuar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)
