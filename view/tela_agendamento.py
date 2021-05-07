import PySimpleGUI as sg

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
        elif values['4']:
            opcao = 4
        elif values['5']:
            opcao = 5
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
            [sg.Radio('Alterar agendamento', "RD1", key='3', font=('Verdana', 13))],
            [sg.Radio('Listar agendamentos', "RD1", key='4', font=('Verdana', 13))],
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
        event,values = self.__window.Read()
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
    
    def alterar_agendamento(self):
        self.info_set_agendamento()
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
    
    def info_set_agendamento(self):
        sg.theme('LightBrown')
        layout = [
            [sg.Text('Alterar Agendamento', font=('Verdana', 14))],
            [sg.Text('Digite o CPF do paciente que deseja deletar: ')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def info_setter_agendamento(self):
        sg.theme('LightBrown')
        layout = [
            [sg.Text('Alterar Agendamento', font=('Helvica', 20))],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        self.nome(nome)
        cpf = values['cpf']
        self.cpf_paciente(cpf)
        self.close()
        return {'nome': nome, 'cpf': cpf}
    
    def mostrar_agendamentos(self, agendamentos):
        string = '---------------------------------------- \n\n'
        for agendamento in agendamentos:
            string = string + 'Nome: ' + agendamento['nome'] + ' CPF: ' + agendamento['cpf'] + ' Data: ' + agendamento['data'] + '\n\n'
        sg.Popup('Lista Agendamentos', string, font=('Verdana', 13))
