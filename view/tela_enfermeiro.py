from view.tela_sistema import TelaSistema
import PySimpleGUI as sg

class TelaEnfermeiro():
    
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador
    
    def opcoes_tela_enfermeiro(self):
        self.window_enfermeiro()
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
    
    def nome_enfermeiro(self, nome_enfermeiro):
        leu = False
        while not leu:
            try:
                nome_enfermeiro = nome_enfermeiro.title()
                novo = nome_enfermeiro.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception
            except Exception:
                sg.Popup('Um nome deve conter apenas letras.')
                nome_enfermeiro = sg.popup_get_text('Digite o nome novamente: ')
        return nome_enfermeiro

    def rua_enfermeiro(self, rua_enfermeiro):
        leu = False
        while not leu:
            try:
                rua_enfermeiro = rua_enfermeiro.title()
                novo = rua_enfermeiro.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception()
            except Exception:
                sg.Popup('Um nome deve conter apenas letras.')
                rua = sg.popup_get_text('Digite o nome da rua novamente: ')
        return rua_enfermeiro

    def num_casa_enfermeiro(self, num_casa_enfermeiro):
        leu = False
        while not leu:
            try:
                if not num_casa_enfermeiro.isnumeric():
                    raise ValueError
            except ValueError:
                sg.PopupOK('Digite apenas números.')
                num_casa_enfermeiro = sg.popup_get_text('Digite o número da casa novamente: ')
            else:
                leu = True
        return num_casa_enfermeiro

    def matricula(self, matricula):
        leu = False
        while not leu:
            try:
                if not matricula.isnumeric():
                    raise Exception
                if len(matricula) != 6:
                    raise Exception
            except Exception:
                sg.Popup('Matrícula é definida por 6 dígitos númericos.')
                sg.popup_get_text('Digite a matrícula novamente: ')
            else:
                leu = True
        return matricula
    
    def window_enfermeiro(self):
        sg.theme('LightGreen6')
        layout = [
            [sg.Text('Escolha sua opção', font=('Verdana', 16))],
            [sg.Text('----------------------------------------------------------')],
            [sg.Radio('Incluir enfermeiro', "RD1", key='1', font=('Verdana', 13))],
            [sg.Radio('Excluir enfermeiro', "RD1", key='2', font=('Verdana', 13))],
            [sg.Radio('Alterar info enfermeiro', "RD1", key='3', font=('Verdana', 13))],
            [sg.Radio('Listar enfermeiros', "RD1", key='4', font=('Verdana', 13))],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Opções enfermeiro', layout=layout, size=(300, 300), finalize=True)

    def incluir_enfermeiro(self):
        self.info_add_enfermeiro()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_enfermeiro()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                nome_enfermeiro = values['nome_enfermeiro']
                self.nome_enfermeiro(nome_enfermeiro)
                rua_enfermeiro = values['rua_enfermeiro']
                self.rua_enfermeiro(rua_enfermeiro)
                num_casa_enfermeiro = values['num_casa_enfermeiro']
                self.num_casa_enfermeiro(num_casa_enfermeiro)
                matricula = values['matricula']
                self.matricula(matricula)
                leu = True
                self.close()
        if leu is True:
            return {'nome_enfermeiro': nome_enfermeiro, 'rua_enfermeiro': rua_enfermeiro, 'num_casa_enfermeiro': num_casa_enfermeiro, 'matricula': matricula}

    def info_add_enfermeiro(self):
        sg.theme('LightGreen6')
        layout = [
            [sg.Text('Incluir Enfermeiro', font=('Helvica', 20))],
            [sg.Text('Nome:', size=(20,1)), sg.InputText('', key='nome_enfermeiro')],
            [sg.Text('Rua:', size=(20,1)), sg.InputText('', key='rua_enfermeiro')],
            [sg.Text('Nº casa:', size=(20,1)), sg.InputText('', key='num_casa_enfermeiro')],
            [sg.Text('Matricula (6 números):', size=(20,1)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def deletar_enfermeiro(self):
        self.info_del_enfermeiro()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_enfermeiro()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                matricula = values['matricula']
                self.matricula(matricula)
                leu = True
                self.close()
        if leu is True:
            return {'matricula': matricula}

    def info_del_enfermeiro(self):
        sg.theme('LightGreen6')
        layout = [
            [sg.Text('Excluir Enfermeiro', font=('Helvica', 20))],
            [sg.Text('Digite a matrícla do enfermeiro que deseja deletar: ')],
            [sg.Text('Matrícula (Apenas Nº):', size=(20,1)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def alterar_enfermeiro(self):
        self.info_set_enfermeiro()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_enfermeiro()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                matricula = values['matricula']
                self.matricula(matricula)
                leu = True
                self.close()
        if leu is True:
            return {'matricula': matricula}

    def info_set_enfermeiro(self):
        sg.theme('LightGreen6')
        layout = [
            [sg.Text('Alterar Enfermeiro', font=('Helvica', 20))],
            [sg.Text('Digite a matrícla do enfermeiro que deseja deletar: ')],
            [sg.Text('Matrícula (Apenas Nº):', size=(20,1)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def info_setter_enfermeiro(self):
        sg.theme('LightGreen6')
        layout = [
            [sg.Text('Alterar Enfermeiro', font=('Helvica', 20))],
            [sg.Text('Nome:', size=(20,1)), sg.InputText('', key='nome_enfermeiro')],
            [sg.Text('Rua:', size=(20,1)), sg.InputText('', key='rua_enfermeiro')],
            [sg.Text('Nº casa:', size=(20,1)), sg.InputText('', key='num_casa_enfermeiro')],
            [sg.Text('Matricula (Apenas Números):', size=(20,1)), sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)
        button, values = self.__window.Read()
        nome_enfermeiro = values['nome_enfermeiro']
        self.nome_enfermeiro(nome_enfermeiro)
        rua_enfermeiro = values['rua_enfermeiro']
        self.rua_enfermeiro(rua_enfermeiro)
        num_casa_enfermeiro = values['num_casa_enfermeiro']
        self.num_casa_enfermeiro(num_casa_enfermeiro)
        matricula = values['matricula']
        self.matricula(matricula)
        self.close()
        return {'nome_enfermeiro': nome_enfermeiro, 'rua_enfermeiro': rua_enfermeiro, 'num_casa_enfermeiro': num_casa_enfermeiro, 'matricula': matricula}

    def mostrar_enfermeiros(self, enfermeiros):
        string = '---------------------------------------- \n\n'
        for enfermeiro in enfermeiros:
            string = string + 'Nome: ' + enfermeiro['nome_enfermeiro'] + ' Matricula: ' + enfermeiro['matricula'] + '\n\n'
        sg.Popup('Lista Enfermeiros', string, font=('Verdana', 13))
