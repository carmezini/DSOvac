from controller.control_paciente import ControlPaciente 
from view.tela_sistema import TelaSistema
from view.menu import Menu

class TelaPaciente():
    
    def __init__(self, controlador):
        opcoes_paciente = {
            0: 'Voltar',
            1: 'Cadastrar paciente',
            2: 'Excluir paciente',
            3: 'Alterar info paciente',
            4: 'Listar pacientes'
        }
        self.__menu = Menu('Opções Paciente', opcoes_paciente)
        self.__controlador = controlador
    
    def abre_tela_paciente(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                TelaSistema.inicie()
            elif opcao == 1:
                self.__controlador.incluir_paciente()
            elif opcao == 2:
                self.__controlador.deletar_paciente()
            elif opcao == 3:
                self.__controlador.alterar_paciente()
            elif opcao == 4:
                self.listar_pacientes()
    
    def info_paciente(self):
        nome_paciente = input('Qual o nome do paciente? ')
        endereco = input('Qual a rua e o número onde resida? '))
        ano = int(input('Qual o ano de nascimento? '))
        cpf = int(input('Digite seu CPF (apenas números): '))
        return {'nome': nome_paciente, 'endereco': endereco, 'ano': ano, 'cpf': cpf}
    
    def listar_pacientes(self):
        print(self.__controlador.lista_pacientes())