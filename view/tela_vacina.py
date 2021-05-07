from view.tela_sistema import TelaSistema
import PySimpleGUI as sg

class TelaVacina():
    
    def __init__(self, controlador):
        self.__window = None
        self.__controlador = controlador

    def opcoes_tela_vacina(self):
        self.window_vacina()
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

    def nome_vacina(self, nome):
        return nome

    def quantidade_vacina(self, qtd):
        leu = False
        while not leu:
            try:
                if not qtd.isnumeric():
                    raise ValueError
            except ValueError:
                sg.PopupOK('Digite apenas números inteiros.', title='Quantidade')
                qtd = sg.popup_get_text('Digite novamente: ', title='Quantidade')
            else:
                leu = True
        return int(qtd)

    def window_vacina(self):
        sg.theme('LightGrey')
        layout = [
            [sg.Text('Escolha sua opção', font=('Verdana', 16))],
            [sg.Text('----------------------------------------------------------')],
            [sg.Radio('Incluir vacina', "RD1", key='1', font=('Verdana', 13))],
            [sg.Radio('Excluir vacina', "RD1", key='2', font=('Verdana', 13))],
            [sg.Radio('Alterar info vacina', "RD1", key='3', font=('Verdana', 13))],
            [sg.Radio('Listar vacinas', "RD1", key='4', font=('Verdana', 13))],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Opções Vacina', layout=layout, size=(300, 300), finalize=True)

    def incluir_vacina(self):
        self.info_add_vacina()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_vacina()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                nome = values['nome']
                nome = self.nome_vacina(nome)
                qtd = values['qtd']
                qtd = self.quantidade_vacina(qtd)
                leu = True
                self.close()
            if leu is True:
                return {'nome': nome, 'qtd': qtd}

    def info_add_vacina(self):
        sg.theme('LightGrey')
        layout = [
            [sg.Text('Incluir Vacina', font=('Helvica', 20))],
            [sg.Text('Nome:', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Text('Quantidade:', size=(20,1)), sg.InputText('', key='qtd')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def deletar_vacina(self):
        self.info_del_vacina()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_vacina()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                nome = values['nome']
                nome = self.nome_vacina(nome)
                leu = True
                self.close()
        if leu is True:
            return {'nome': nome}

    def info_del_vacina(self):
        sg.theme('LightGrey')
        layout = [
            [sg.Text('Excluir Vacina', font=('Helvica', 20))],
            [sg.Text('Digite o nome da vacina que deseja deletar: ')],
            [sg.Text('Vacina: ', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def alterar_vacina(self):
        self.info_set_vacina()
        button, event, values = sg.read_all_windows()
        leu = False
        while not leu:
            if event == 'Voltar':
                self.close()
                self.__controlador.abre_tela_vacina()
            elif event == sg.WINDOW_CLOSED:
                self.__controlador.encerra_sistema()
            else:
                nome = values['nome']
                nome = self.nome_vacina(nome)
                leu = True
                self.close()
        if leu is True:
            return {'nome': nome}

    def info_set_vacina(self):
        sg.theme('LightGrey')
        layout = [
            [sg.Text('Alterar Vacina', font=('Helvica', 20))],
            [sg.Text('Digite o nome da vacina que deseja deletar: ')],
            [sg.Text('Vacina: ', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde', layout=layout, finalize=True)

    def info_setter_vacina(self):
        sg.theme('LightGrey')
        layout = [
            [sg.Text('Alterar Vacina', font=('Helvica', 20))],
            [sg.Text('Nome:', size=(20,1)), sg.InputText('', key='nome')],
            [sg.Text('Quantidade:', size=(20,1)), sg.InputText('', key='qtd')],
            [sg.Button('Confirmar'), sg.Cancel('Voltar')]
        ]
        self.__window = sg.Window('Posto de Saúde').Layout(layout)
        button, values = self.__window.Read()
        nome = values['nome']
        nome = self.nome_vacina(nome)
        qtd = values['qtd']
        qtd = self.quantidade_vacina(qtd)
        self.close()
        return {'nome': nome, 'qtd': qtd}

    def mostrar_vacinas(self, vacinas):
        string = '---------------------------------------- \n\n'
        for vacina in vacinas:
            string = string + 'Nome: ' + vacina['nome'] + ' Quantidade: ' + str(vacina['qtd']) + '\n\n'
        sg.Popup('Lista Vacinas', string, font=('Verdana', 13))

    def erro_vacina(self):
        sg.PopupOK('Vacina já existente...', title='Vacina')
    
    def erro_sem_vacina(self):
        sg.PopupOK('Vacina não existe...', title='Vacina')
    
    def sucesso_incluir(self):
        sg.PopupOK('Vacina cadastrada com sucesso.', title='Vacina')

    def sucesso_deletar(self):
        sg.PopupOK('Vacina deletada com sucesso.', title='Vacina')

    def sucesso_alterar(self):
        sg.PopupOK('Vacina alterada com sucesso.', title='Vacina')
