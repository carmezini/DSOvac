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
                try:
                    self.__controlador.deletar_paciente()
                except Exception:
                    print('Não há paciente com esse CPF.')
            elif opcao == 3:
                try:
                    self.__controlador.alterar_paciente()
                except Exception:
                    print('Não há paciente com esse CPF.')
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

    def alterar_paciente(self):
        cpf = self.cpf_paciente()
        return {'cpf': cpf}

    def info_alterar_paciente(self):
        print('\033[32:41m= = = Alterar Paciente = = =\033[m')
        print('Adicione as novas informações do paciente...')
        nome_paciente = self.nome_paciente()
        rua = self.rua_paciente()
        num_casa = self.num_casa_paciente()
        ano = self.ano_paciente()
        cpf = self.cpf_paciente()
        return {'nome': nome_paciente, 'rua': rua, 'num_casa': num_casa, 'ano': ano, 'cpf': cpf}

    def info_deletar_paciente(self):
        print('\033[35:40m= = = Excluir Paciente = = =\033[m')
        cpf = self.cpf_paciente()
        return {'cpf': cpf}

    def mostrar_pacientes(self):
        print('\033[34:40m= = = Pacientes Cadastrados = = =\033[m')
        for p in self.__controlador.lista_pacientes():
            print(p)
        print('*=*=*=*')

    def nome_paciente(self):
        leu = False
        while not leu:
            try:
                nome_paciente = input('Qual o nome do paciente? ')
                nome_paciente = nome_paciente.title()
                novo = nome_paciente.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception
            except Exception:
                print('Um nome deve conter apenas letras.')
        return nome_paciente

    def rua_paciente(self):
        leu = False
        while not leu:
            try:
                rua_paciente = input('Qual o nome da rua onde resida? ')
                rua_paciente = rua_paciente.title()
                novo = rua_paciente.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception()
            except Exception:
                print('Um nome deve conter apenas letras.')
        return rua_paciente

    def num_casa_paciente(self):
        leu = False
        while not leu:
            try:
                num_casa = int(input('Qual o número da residência? '))
                leu = True
            except ValueError:
                print('Digite apenas números.')
        return num_casa

    def cpf_paciente(self):
        leu = False
        while not leu:
            try:
                cpf_paciente = input('Qual o CPF do paciente (apenas números): ')
                if not cpf_paciente.isnumeric():
                    raise Exception
                if len(cpf_paciente) != 11:
                    raise Exception
            except Exception:
                print('CPF são 11 dígitos númericos.')
            else:
                leu = True
        return cpf_paciente
    
    def ano_paciente(self):
        leu = False
        while not leu:
            try:
                ano = int(input('Qual o ano de nascimento? '))
                if 2021 > ano < 1871:
                    raise Exception
            except Exception:
                print('O ano deve ser um número entre 1871 e 2021.')
            else:
                leu = True     
        return ano  
