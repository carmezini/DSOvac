from tela_sistema import TelaSistema
from menu import Menu
from control.control_vacina import ControlVacina

class TelaVacina():
    
    def __init__(self, controlador):
        opcoes_vacina = {
            0: 'Voltar',
            1: 'Cadastrar Vacina',
            2: 'Excluir Vacina',
            3: 'Alterar info vacina',
            4: 'Listar Vacinas',
        }
        self.__menu = Menu('Opções Vacina', opcoes_vacina)
        self.__controlador = controlador
    
    def interaja(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                TelaSistema.inicie()
            elif opcao == 1:
                self.__controlador.incluir_vacina()
            elif opcao == 2:
                self.__controlador.deletar_vacina()
            elif opcao == 3:
                self.__controlador.alterar_vacinas()
            elif opcao == 4:
                pass
    
    def info_vacina(self):
        nome_vacina = input('Qual o nome do fabricante? ')
        qtd = int(input('Quantas doses deseja informar? '))
        return {'nome': nome_vacina, 'qtd': qtd}
