from view.tela_sistema import TelaSistema
from view.menu import Menu

class TelaEnfermeiro():
    
    def __init__(self, controlador):
        opcoes_enfermeiro = {
            0: 'Voltar',
            1: 'Cadastrar enfermeiro',
            2: 'Excluir enfermeiro',
            3: 'Alterar info enfermeiro',
            4: 'Listar enfermeiros'
        }
        self.__menu = Menu('\033[36:41mOpções Enfermeiros\033[m ====', opcoes_enfermeiro)
        self.__controlador = controlador
    
    def abre_tela_enfermeiro(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                terminar = True
            elif opcao == 1:
                self.__controlador.incluir_enfermeiro()
            elif opcao == 2:
                try:
                    self.__controlador.deletar_enfermeiro()
                except Exception:
                    print('Não há enfermeiro com essa matrícula.')
            elif opcao == 3:
                try:
                    self.__controlador.alterar_enfermeiro()
                except Exception:
                    print('Não há enfermeiro com essa matrícula.')
            elif opcao == 4:
                self.mostrar_enfermeiros()

    def info_enfermeiro(self):
        print('\033[32:40m= = = Adicionar Enfermeiro = = =\033[m')
        nome_enfermeiro = self.nome_enfermeiro()
        rua = self.rua_enfermeiro()
        num_casa = self.num_casa_enfermeiro()
        matricula = self.matricula_enfermeiro()
        print('*=*=*=*')
        return {'nome': nome_enfermeiro, 'rua': rua, 'num_casa': num_casa, 'matricula': matricula}
    
    def alterar_enfermeiro(self):
        matricula = self.matricula_enfermeiro()
        return {'matricula': matricula}

    def info_alterar_enfermeiro(self):
        print('\033[32:41m= = = Alterar Enfermeiro = = =\033[m')
        print('Adicione as novas informações do enfermeiro...')
        nome_enfermeiro = self.nome_enfermeiro()
        rua = self.rua_enfermeiro()
        num_casa = self.num_casa_enfermeiro()
        matricula = self.matricula_enfermeiro()
        return {'nome': nome_enfermeiro, 'rua': rua, 'num_casa': num_casa, 'matricula': matricula}

    def info_deletar_enfermeiro(self):
        print('\033[35:40m= = = Excluir Enfermeiro = = =\033[m')
        matricula = self.matricula_enfermeiro()
        return {'matricula': matricula}

    def mostrar_enfermeiros(self):
        print('\033[34:40m= = = Enfermeiros Cadastrados = = =\033[m')
        for p in self.__controlador.lista_enfermeiros():
            print(p)
        print('*=*=*=*')
    
    def nome_enfermeiro(self):
        leu = False
        while not leu:
            try:
                nome_enfermeiro = input('Qual o nome do enfermeiro? ')
                nome_enfermeiro = nome_enfermeiro.title()
                novo = nome_enfermeiro.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception
            except Exception:
                print('Um nome deve conter apenas letras.')
        return nome_enfermeiro

    def rua_enfermeiro(self):
        leu = False
        while not leu:
            try:
                rua_enfermeiro = input('Qual o nome da rua onde resida? ')
                rua_enfermeiro = rua_enfermeiro.title()
                novo = rua_enfermeiro.replace(' ', 'x')
                if novo.isalpha():
                    leu = True
                if leu is False:
                    raise Exception()
            except Exception:
                print('Um nome deve conter apenas letras.')
        return rua_enfermeiro

    def num_casa_enfermeiro(self):
        leu = False
        while not leu:
            try:
                num_casa = int(input('Qual o número da residência? '))
                leu = True
            except ValueError:
                print('Digite apenas números.')
        return num_casa

    def matricula_enfermeiro(self):
        leu = False
        while not leu:
            try:
                matricula = input('Digite sua matrícula (6 números): ')
                if not matricula.isnumeric():
                    raise Exception
                if len(matricula) != 6:
                    raise Exception
            except Exception:
                print('Matrícula é definida por 6 dígitos númericos.')
            else:
                leu = True
        return matricula
