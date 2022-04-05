from view.tela_sistema import TelaSistema
from view.menu import Menu

class TelaVacina():
    
    def __init__(self, controlador):
        opcoes_vacina = {
            0: 'Voltar',
            1: 'Cadastrar Vacina',
            2: 'Excluir Vacina',
            3: 'Alterar info vacina',
            4: 'Listar Vacinas'
        }
        self.__menu = Menu('\033[36:41mOpções Vacina\033[m ====', opcoes_vacina)
        self.__controlador = controlador
    
    def abre_tela_vacina(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                terminar = True
            elif opcao == 1:
                self.__controlador.incluir_vacina()
            elif opcao == 2:
                self.__controlador.deletar_vacina()
            elif opcao == 3:
                self.__controlador.alterar_vacinas()
            elif opcao == 4:
                self.mostrar_vacinas()

    def info_vacina(self):
        print('\033[32:40m= = = Adicionar Vacina = = =\033[m')
        nome_vacina = input('Qual o nome do fabricante? ')
        qtd = self.quantidade_vacina()
        print('*=*=*=*')
        return {'nome': nome_vacina, 'qtd': qtd}

    def quantidade_vacina(self):
        leu = False
        while not leu:
            try:
                qtd = int(input('Quantas doses deseja informar? '))
                leu = True
            except ValueError:
                print('Digite apenas números inteiros.')
        return qtd

    def info_deletar_vacina(self):
        print('\033[35:40m= = = Excluir Vacina = = =\033[m')
        nome_vacina = input('Qual o nome do fabricante? ')
        return {'nome': nome_vacina}
    
    def mostrar_vacinas(self):
        print('\033[34:40m= = = Vacinas Cadastradas = = =\033[m')
        for v in self.__controlador.lista_vacinas():
            print(v)
        print('*=*=*=*')