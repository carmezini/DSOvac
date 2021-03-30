from controller.control_paciente import ControlPaciente 
from view.tela_sistema import TelaSistema
from view.menu import Menu

class TelaPaciente():
    
    def __init__(self):
        opcoes_paciente = {
            0: Voltar
            1: Cadastrar paciente
            2: Excluir paciente
            3: Alterar info paciente
            4: Listar pacientes
        }
        self.__menu = Menu('Opções Paciente', opcoes_paciente)
    
    def interaja(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                TelaSistema.inicie()
            elif opcao == 1:
                self.cadastro_paciente
            elif opcao == 2:
                self.exclui_paciente
            elif opcao == 3:
                pass
            elif opcao == 4:
                self.
    
    def cadastro_paciente(self):
        nome_paciente = input('Qual o nome do paciente? ')
        endereco = input('Qual a rua e o número onde resida? '))
        ano = int(input('Qual o ano de nascimento? '))
        cpf = int(input('Digite seu CPF (apenas números): '))
        print('O paciente {} foi adicionado.'.format(nome_paciente))

        return {'nome': nome_paciente, 'endereco': endereco, 'ano': ano, 'cpf': cpf}
    
    def exclui_paciente(self):
        nome_vacina = input('Qual o nome do fabricante? ')
        qtd = int(input('Quantas doses deseja excluir? '))
        control_vacina.del_vacina(Vacina(nome_vacina, qtd))
        print('{} doses da vacina {} foram excluídas do estoque'.format(qtd, nome_vacina))

    def altera_paciente(self):
        print('Digite as informações do paciente: ')
        self.cadastro_paciente
        print('Digite as novas informações do paciente: ')
        self.cadastro_paciente

    def lista_pacientes(self, info):
        print('Nome': info['nome'])
        print('Endereço': info['endereco'])
        print('Ano nascimento': info['ano'])
        print('CPF': info['cpf'])