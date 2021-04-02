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
        self.__menu = Menu('\033[36:41mOpções Paciente\033[m ===', opcoes_paciente)
        self.__controlador = controlador
    

    def abre_tela_paciente(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                terminar = True
            elif opcao == 1:
                self.__controlador.incluir_paciente()
            elif opcao == 2:
                self.__controlador.deletar_paciente()
            elif opcao == 3:
                self.__controlador.alterar_paciente()
            elif opcao == 4:
                self.mostrar_pacientes()

    def info_paciente(self):
        print('\033[32:40m= = = Adicionar Paciente = = =\033[m')
        nome_paciente = input('Qual o nome do paciente? ')
        rua = input('Qual a rua onde resida? ')
        num_casa = int(input('Qual o número da residência? '))
        ano = int(input('Qual o ano de nascimento? '))
        cpf = input('Digite seu CPF (apenas números): ')
        print('*=*=*=*')
        return {'nome': nome_paciente, 'rua': rua, 'num_casa': num_casa, 'ano': ano, 'cpf': cpf}

    def info_deletar_paciente(self):
        print('\033[35:40m= = = Excluir Paciente = = =\033[m')
        cpf = input('Qual o CPF do paciente? ')
        return {'cpf': cpf}

    def mostrar_pacientes(self):
        print('\033[34:40m= = = Pacientes Cadastrados = = =\033[m')
        for p in self.__controlador.lista_pacientes():
            print(p)
        print('*=*=*=*')
