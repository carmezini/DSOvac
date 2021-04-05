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
        self.__menu = Menu('\033[36:41mOpções Paciente\033[m ====', opcoes_paciente)
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
        nome_paciente = self.nome_paciente()
        rua = self.rua_paciente()
        num_casa = self.num_casa_paciente()
        ano = self.ano_paciente()
        cpf = self.cpf_paciente()
        print('*=*=*=*')
        return {'nome': nome_paciente, 'rua': rua, 'num_casa': num_casa, 'ano': ano, 'cpf': cpf}
    
    def nome_paciente(self):
        leu = False
        while not leu:
            nome_paciente = input('Qual o nome do paciente? ')
            nome_paciente = nome_paciente.title()
            novo = nome_paciente.replace(' ', 'x')
            if novo.isalpha():
                leu = True
            if leu is False:
                print('Um nome deve conter apenas letras.')
        return nome_paciente

    def rua_paciente(self):
        leu = False
        while not leu:
            rua_paciente = input('Qual o nome da rua onde resida? ')
            rua_paciente = rua_paciente.title()
            novo = rua_paciente.replace(' ', 'x')
            if novo.isalpha():
                leu = True
            if leu is False:
                print('Um nome deve conter apenas letras.')
        return rua_paciente

    def cpf_paciente(self):
        leu = False
        while not leu:
            cpf_paciente = input('Qual o CPF do paciente (apenas números): ')
            if cpf_paciente.isnumeric():
                if len(cpf_paciente) == 11:
                    leu = True
            if leu is False:
                print('CPF são 11 dígitos númericos.')
        return cpf_paciente
    
    def ano_paciente(self):
        leu = False
        while not leu:
            try:
                ano = int(input('Qual o ano de nascimento? '))
                if 1871 < ano < 2021:
                    leu = True
            except ValueError:
                print('Digite apenas números.')
            if leu is False:
                print('O ano deve ser entre 1871 e 2021.')          
        return ano  

    def info_deletar_paciente(self):
        print('\033[35:40m= = = Excluir Paciente = = =\033[m')
        cpf = self.cpf_paciente()
        return {'cpf': cpf}
    
    def num_casa_paciente(self):
        leu = False
        while not leu:
            try:
                num_casa = int(input('Qual o número da residência? '))
                leu = True
            except ValueError:
                print('Digite apenas números.')
        return num_casa

    def mostrar_pacientes(self):
        print('\033[34:40m= = = Pacientes Cadastrados = = =\033[m')
        for p in self.__controlador.lista_pacientes():
            print(p)
        print('*=*=*=*')
