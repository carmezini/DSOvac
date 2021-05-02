from view.tela_sistema import TelaSistema
from view.menu import Menu
import PySimpleGUI as sg

class TelaPaciente():
    
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador
        self.init_opcoes()

    def abre_tela_paciente(self):
        terminar = False
        while not terminar:
            self.init_opcoes()
            button, values = self.__window.Read()
            if values['0'] or button in (None, 'Cancelar'):
                self.close()
            if values['1']:
                try:
                    self.__controlador.incluir_paciente()
                except Exception:
                    sg.Popup('Já há um paciente com esse CPF cadastrado.')
                else:
                    sg.Popup('Paciente cadastrado com sucesso.')
            if values['2']:
                try:
                    self.__controlador.deletar_paciente()
                except Exception:
                    sg.PopupError('Ainda não há um paciente com esse CPF cadastrado.')
                else:
                    sg.Popup('Paciente excluido com sucesso.')
            if values['3']:
                try:
                    self.__controlador.alterar_paciente()
                except Exception:
                    sg.Popup('Ainda não há um paciente com esse CPF cadastrado.')
                else:
                    sg.Popup('Paciente alterado com sucesso.')
            if values['4']:
                self.__controlador.lista_pacientes()
            self.close()

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
                sg.Popup('Um nome deve conter apenas letras.')
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
               sg.Popup('Um nome deve conter apenas letras.')
        return rua

    def num_casa_paciente(self, num_casa):
        leu = False
        while not leu:
            try:
                if not num_casa.isnumeric():
                    raise ValueError
            except ValueError:
                sg.Popup('Digite apenas números.')
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
                sg.PopupOK('CPF são 11 dígitos númericos.')
                cpf = sg.popup_get_text('Digite o CPF novamente: ')
            else:
                leu = True
        return cpf
    
    def ano_paciente(self, ano):
        ano = int(ano)
        leu = False
        while not leu:
            try:
                if 2021 > ano < 1871:
                    raise Exception
            except Exception:
                Sg.Popup('O ano deve ser um número entre 1871 e 2021.')
            else:
                leu = True     
        return ano  

    def init_opcoes(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('= = = Opções Paciente = = =', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir paciente', "RD1", key='1')],
            [sg.Radio('Excluir paciente', "RD1", key='2')],
            [sg.Radio('Alterar info paciente', "RD1", key='3')],
            [sg.Radio('Listar pacientes', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)

    def incluir_paciente(self):
        self.info_add_paciente()
        leu = False
        while not leu:
            button, values = self.__window.Read()
            nome = values['nome']
            self.nome(nome)
            rua = values['rua']
            self.rua_paciente(rua)
            num_casa = values['num_casa']
            self.num_casa_paciente(num_casa)
            ano = values['ano']
            self.ano_paciente(ano)
            cpf = values['cpf']
            self.cpf_paciente(cpf)
            leu = True
        if leu is True:
            return {'nome': nome, 'rua': rua, 'num_casa': num_casa, 'ano': ano, 'cpf': cpf}

    def info_add_paciente(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('= = = Incluir Paciente = = =', font=('Helvica', 20))],
            [sg.Text('Nome:', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Text('Rua:', size=(20,1)), sg.InputText('', key='rua')],
            [sg.Text('Nº casa:', size=(20,1)), sg.InputText('', key='num_casa')],
            [sg.Text('Ano Nacimento:', size=(20,1)), sg.InputText('', key='ano')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)
    
    def deletar_paciente(self):
        self.info_del_paciente()
        button, values = self.__window.Read()
        cpf = values['cpf']
        self.cpf_paciente(cpf)
        return {'cpf': cpf}
    
    def info_del_paciente(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('= = = Excluir Paciente = = =', font=('Helvica', 20))],
            [sg.Text('Digite o CPF do paciente que deseja deletar: ')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)

    def alterar_paciente(self):
        self.info_set_paciente()
        button, values = self.__window.Read()
        cpf = values['cpf']
        self.cpf_paciente(cpf)
        return {'cpf': cpf}
    
    def info_set_paciente(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('= = = Alterar Paciente = = =', font=('Helvica', 20))],
            [sg.Text('Digite o CPF do paciente que deseja deletar: ')],
            [sg.Text('CPF (Apenas Números):', size=(20,1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)

    def info_setter_paciente(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('= = = Alterar Paciente = = =', font=('Helvica', 20))],
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
        self.nome(nome)
        rua = values['rua']
        self.rua_paciente(rua)
        num_casa = values['num_casa']
        self.num_casa_paciente(num_casa)
        ano = values['ano']
        self.ano_paciente(ano)
        cpf = values['cpf']
        self.cpf_paciente(cpf)
        return {'nome': nome, 'rua': rua, 'num_casa': num_casa, 'ano': ano, 'cpf': cpf}
    
    def mostrar_pacientes(self, pacientes):
        string = ''
        for paciente in pacientes:
            string = string + 'Nome: ' + paciente['nome'] + ' CPF: ' + paciente['cpf'] + '\n\n'
        sg.Text('= = = Lista de Pacientes', font=('Helvica', 20))
        sg.Popup('Posto de Saúde', string)
        
