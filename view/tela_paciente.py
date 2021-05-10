from view.tela_sistema import TelaSistema
import PySimpleGUI as sg
from control.excecoes.excecao_cpf_invalido import ComCPFInvalidoException
from control.excecoes.excecao_com_cpf import ComCPFException
from control.excecoes.excecao_sem_cpf import SemCPFException


class TelaPaciente():
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador

    def opcoes_tela_paciente(self):
        self.window_paciente()
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

    def nome(self, nome):
        leu = False
        while not leu:
            try:
                nome = nome.title()
                novo = nome.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception
            except Exception:
                sg.Popup('Um nome deve conter apenas letras.', title='Nome')
                nome = sg.popup_get_text('Digite o nome novamente: ', title='Nome')
        return nome

    def rua_paciente(self, rua):
        leu = False
        while not leu:
            try:
                rua = rua.title()
                novo = rua.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception()
            except Exception:
               sg.PopupOK('Um nome deve conter apenas letras.', title='Nome rua')
               rua = sg.popup_get_text('Digite o nome da rua novamente: ', title='Nome rua')
        return rua

    def num_casa_paciente(self, num_casa):
        leu = False
        while not leu:
            try:
                if not num_casa.isnumeric():
                    raise ValueError
            except ValueError:
                sg.PopupOK('Digite apenas números.', title='Nº casa')
                num_casa = sg.popup_get_text('Digite o número da casa novamente: ', title='Nº casa')
            else:
                leu = True
        return num_casa

    def cpf_paciente(self, cpf):
        leu = False
        while not leu:
            try:
                if not cpf.isnumeric():
                    raise Exception
                if len(cpf) != 11:
                    raise Exception
            except Exception:
                sg.PopupOK(ComCPFInvalidoException())
                cpf = sg.popup_get_text('Digite o CPF novamente: ', title='CPF')
            else:
                leu = True
        return cpf
    
    def ano_paciente(self, ano):
        ano = int(ano)
        leu = False
        while not leu:
            try:
                if 2021 > int(ano) < 1871:
                    raise Exception
            except Exception:
                sg.Popup('O ano deve ser um número entre 1871 e 2021.', title='Ano')
                ano = sg.popup_get_text('Digite o ano novamente: ', title='Ano')
            else:
                leu = True     
        return ano  

    def window_paciente(self):
        sg.theme('LightPurple')
        layout = [
            [sg.Text('Escolha sua opção', font=('Verdana', 16))],
            [sg.Text('----------------------------------------------------------')],
            [sg.Radio('Incluir paciente', "RD1", key='1', font=('Verdana', 13))],
            [sg.Radio('Excluir paciente', "RD1", key='2', font=('Verdana', 13))],
            [sg.Radio('Alterar info paciente', "RD1", key='3', font=('Verdana', 13))],
            [sg.Radio('Listar pacientes', "RD1", key='4', font=('Verdana', 13))],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Opções Paciente', layout=layout, size=(300, 300), finalize=True)

    def incluir_paciente(self):
        self.info_add_paciente()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_paciente()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                nome = values['nome']
                nome = self.nome(nome)
                rua = values['rua']
                rua = self.rua_paciente(rua)
                num_casa = values['num_casa']
                num_casa = self.num_casa_paciente(num_casa)
                ano = values['ano']
                ano = self.ano_paciente(ano)
                cpf = values['cpf']
                cpf = self.cpf_paciente(cpf)
                leu = True
                self.close()
        if leu is True:
            return {'nome': nome, 'rua': rua, 'num_casa': num_casa, 'ano': ano, 'cpf': cpf}

    def info_add_paciente(self):
        sg.theme('LightPurple')
        layout = [
            [sg.Text('Incluir Paciente', font=('Helvica', 20))],
            [sg.Text('Nome:', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Text('Rua:', size=(20,1)), sg.InputText('', key='rua')],
            [sg.Text('Nº casa:', size=(20,1)), sg.InputText('', key='num_casa')],
            [sg.Text('Ano Nacimento:', size=(20,1)), sg.InputText('', key='ano')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)
    
    def deletar_paciente(self):
        self.info_del_paciente()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_paciente()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                cpf = values['cpf']
                cpf = self.cpf_paciente(cpf)
                leu = True
                self.close()
        if leu is True:
            return {'cpf': cpf}

    def info_del_paciente(self):
        sg.theme('LightPurple')
        layout = [
            [sg.Text('Excluir Paciente', font=('Helvica', 20))],
            [sg.Text('Digite o CPF do paciente que deseja deletar: ')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def alterar_paciente(self):
        self.info_set_paciente()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_paciente()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                cpf = values['cpf']
                cpf = self.cpf_paciente(cpf)
                leu = True
                self.close()
        if leu is True:
            return {'cpf': cpf}

    def info_set_paciente(self):
        sg.theme('LightPurple')
        layout = [
            [sg.Text('Alterar Paciente', font=('Helvica', 20))],
            [sg.Text('Digite o CPF do paciente que deseja deletar: ')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def info_setter_paciente(self):
        sg.theme('LightPurple')
        layout = [
            [sg.Text('Alterar Paciente', font=('Helvica', 20))],
            [sg.Text('Nome:', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Text('Rua:', size=(20,1)), sg.InputText('', key='rua')],
            [sg.Text('Nº casa:', size=(20,1)), sg.InputText('', key='num_casa')],
            [sg.Text('Ano Nacimento:', size=(20,1)), sg.InputText('', key='ano')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        nome = self.nome(nome)
        rua = values['rua']
        rua = self.rua_paciente(rua)
        num_casa = values['num_casa']
        num_casa = self.num_casa_paciente(num_casa)
        ano = values['ano']
        ano = self.ano_paciente(ano)
        cpf = values['cpf']
        cpf = self.cpf_paciente(cpf)
        self.close()
        return {'nome': nome, 'rua': rua, 'num_casa': num_casa, 'ano': ano, 'cpf': cpf}
    
    def mostrar_pacientes(self, pacientes):
        string = '---------------------------------------- \n\n'
        for paciente in pacientes:
            string = string + 'Nome: ' + paciente['nome'] + ' CPF: ' + paciente['cpf'] + '\n\n'
        sg.Popup('Lista Pacientes', string, font=('Verdana', 13))

    def erro_cpf(self):
        sg.PopupOK(ComCPFException())
    
    def erro_sem_cpf(self):
        sg.PopupOK(SemCPFException())
    
    def sucesso_incluir(self):
        sg.PopupOK('Paciente cadastrado com sucesso.')

    def sucesso_deletar(self):
        sg.PopupOK('Paciente deletado com sucesso.')
    
    def sucesso_alterar(self):
        sg.PopupOK('Paciente alterado com sucesso.')
