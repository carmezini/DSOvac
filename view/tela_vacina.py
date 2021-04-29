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
                try:
                    self.__controlador.incluir_vacina()
                except Exception:
                    print('Não foi possível adicionar a vacina.')
                else:
                    print('Vacina adicionada com sucesso.')
            elif opcao == 2:
                try:
                    self.__controlador.deletar_vacina()
                except Exception:
                    print('A vacina informada não consta no estoque.')
                else:
                    print('Vacina deletada com sucesso.')
            elif opcao == 3:
                try:
                    self.__controlador.alterar_vacinas()
                except Exception:
                    print('A vacina informada não consta no estoque.')
                else:
                    print('Vacina alterada com sucesso.')
            elif opcao == 4:
                self.mostrar_vacinas()

    def info_vacina(self):
        print('\033[32:40m= = = Adicionar Vacina = = =\033[m')
        nome = self.nome_vacina()
        qtd = self.quantidade_vacina()
        print('*=*=*=*')
        return {'nome': nome, 'qtd': qtd}

    def alterar_vacina(self):
        nome = self.nome_vacina()
        return {'nome': nome}

    def info_alterar_vacina(self):
        print('\033[32:41m= = = Alterar Vacina = = =\033[m')
        print('Adicione as novas informações da vacina...')
        nome = self.nome_vacina()
        qtd = self.quantidade_vacina()
        return {'nome': nome, 'qtd': qtd}
    
    def info_deletar_vacina(self):
        print('\033[35:40m= = = Excluir Vacina = = =\033[m')
        nome = input('Qual o nome do fabricante? ')
        return {'nome': nome}
    
    def mostrar_vacinas(self):
        print('\033[34:40m= = = Vacinas Cadastradas = = =\033[m')
        for v in self.__controlador.lista_vacinas():
            print(v)
        print('*=*=*=*')

    def nome_vacina(self):
        nome = input('Digite o nome do fabricante? ')
        return nome

    def quantidade_vacina(self):
        leu = False
        while not leu:
            try:
                qtd = int(input('Quantas doses deseja informar? '))
                leu = True
            except ValueError:
                print('Digite apenas números inteiros.')
        return qtd
