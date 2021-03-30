from tela_sistema import TelaSistema
from menu import Menu
from control.control_vacina import ControlVacina

class TelaVacina():
    
    def __init__(self):
        opcoes_vacina = {
            0: 'Voltar',
            1: 'Cadastrar Vacina',
            2: 'Excluir Vacina',
            3: 'Alterar info vacina',
            4: 'Listar Vacinas',
        }
        self.__menu = Menu('Opções Vacina', opcoes_vacina)
        self.__controlador = ControlVacina()
    
    def interaja(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                TelaSistema.inicie()
            elif opcao == 1:
                self.cadastro_vacina
            elif opcao == 2:
                self.exclui_vacina
            elif opcao == 3:
                self.altera_vacina
            elif opcao == 4:
                self.estoque_vacinas
    
    def cadastro_vacina(self):
        nome_vacina = input('Qual o nome do fabricante? ')
        qtd = int(input('Quantas doses deseja adicionar? '))
        self.__controlador.add_vacina(Vacina(nome_vacina), qtd)
        print('{} doses da vacina {} foram adicionadas ao estoque'.format(qtd, nome_vacina))
    
    def exclui_vacina(self):
        continuar = True
        while continuar:
            nome_vacina = input('Qual o nome do fabricante? ')
            continuar = 'y' == input('Tem certeza que deseja excluir {}? [y/n]'.format(nome_vacina))
            continuar = 'y' == input('Informar outra vacina? [y/n]')
            self.__controlador.del_vacina(Vacina(nome_vacina))
            input('Tecle ENTER para continuar.')
            print('A vacina {} foi excluída do estoque'.format(nome_vacina))
    
    def altera_vacina(self):
        pass

    def estoque_vacinas(self):
        pass
