import PySimpleGUI as sg
import datetime as dt
from random import choice

class TelaAgendamento():
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador
    
    def opcoes_tela_agendamento(self):
        self.window_agendamento()
        button, event, values = sg.read_all_windows()
        opcao = 0
        if event == 'Voltar':
            opcao = 6
        elif event == sg.WIN_CLOSED:
            opcao = 0
        elif values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        self.close()
        return opcao
    
    def close(self):
        self.__window.Close()

    def cpf_paciente(self, cpf):
        leu = False
        while not leu:
            try:
                if not cpf.isnumeric():
                    raise Exception
                if len(cpf) != 11:
                    raise Exception
            except Exception:
                sg.PopupOK('CPF são 11 dígitos númericos.')
                cpf = sg.popup_get_text('Digite o CPF novamente: ')
            else:
                leu = True
        return cpf

    def window_agendamento(self):
        sg.theme('LightBrown')
        layout = [
            [sg.Text('Escolha sua opção', font=('Verdana', 16))],
            [sg.Text('----------------------------------------------------------')],
            [sg.Radio('Marcar agendamento', "RD1", key='1', font=('Verdana', 13))],
            [sg.Radio('Desmarcar agendamento', "RD1", key='2', font=('Verdana', 13))],
            [sg.Radio('Listar agendamentos', "RD1", key='3', font=('Verdana', 13))],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Opções Agendamento', layout=layout, size=(300, 300), finalize=True)

    def incluir_agendamento(self):
        self.info_add_agendamento()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_agendamento()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                cpf = values['cpf']
                self.cpf_paciente(cpf)
                leu = True
                self.close()
        if leu is True:
            return {'cpf': cpf}

    def info_add_agendamento(self):
        sg.theme('LightBrown')
        layout = [
            [sg.Text('Marcar Agendamento', font=('Helvica', 20))],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def calendar(self):
        sg.theme('LightBrown')
        layout = [[sg.T('Calendário')],
          [sg.In('', size=(20,1), key='input')],
          [sg.CalendarButton('Escolha a data', target='input', format=('%d/%m/%Y'), key='date')],
          [sg.Ok(key=1)]]

        self.__window = sg.Window('Calendário', grab_anywhere=False).Layout(layout)
        leu = False
        while not leu:
            event, values = self.__window.Read()
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_agendamento()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                data = values['input']
                leu = True
        self.__window.close()
        return data

    def deletar_agendamento(self):
        self.info_del_agendamento()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_agendamento()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                cpf = values['cpf']
                self.cpf_paciente(cpf)
                leu = True
                self.close()
        if leu is True:
            return {'cpf': cpf}

    def info_del_agendamento(self):
        sg.theme('LightBrown')
        layout = [
            [sg.Text('Desmarcar agendamento', font=('Verdana', 14))],
            [sg.Text('Digite o CPF do paciente para desmarcar: ')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def hora(self):
        hora = [
            '08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30',
            '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30',
            '17:00', '17:30']
        escolhido = choice(hora)
        return escolhido
    
    def erro_hora(self):
        sg.PopupOK('Segunda dose deverá ser tomada 20 dias após a primeira...', title='hora')
    
    def mostrar_agendamentos(self, agendamentos):
        string = '---------------------------------------- \n\n'
        for agendamento in agendamentos:
            string = string + 'Nome: ' + agendamento['nome'] + ' CPF: ' + agendamento['cpf'] + '\n\n'
            string = string + 'Data: ' + agendamento['data'] + ' Hora: ' + agendamento['hora'] + '\n\n'
            dict_data_hora = self.__controlador.data_duas_doses(agendamento['data'])
            data_duas = dict_data_hora['data']
            hora_duas = dict_data_hora['hora']
            string = string + 'Data 2ªdose: ' + data_duas + ' Hora: ' + hora_duas + '\n\n'
            string = string + 'Enfermeiro(a): ' + agendamento['enfermeiro'] + ' Vacina: ' + agendamento['vacina'] + '\n\n'
            string = string + '---------------------------------------- \n\n'
        sg.Popup('Lista Agendamentos', string, font=('Verdana', 10))
