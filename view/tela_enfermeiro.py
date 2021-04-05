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
                self.__controlador.deletar_enfermeiro()
            elif opcao == 3:
                self.__controlador.alterar_enfermeiro()
            elif opcao == 4:
                self.mostrar_enfermeiros()

    def info_enfermeiro(self):
        print('\033[32:40m= = = Adicionar Enfermeiro = = =\033[m')
        nome_enfermeiro = self.nome_enfermeiro()
        rua = input('Qual a rua onde resida? ')
        num_casa = self.num_casa_enfermeiro()
        matricula = self.matricula_enfermeiro()
        print('*=*=*=*')
        return {'nome': nome_enfermeiro, 'rua': rua, 'num_casa': num_casa, 'matricula': matricula}
    
    def nome_enfermeiro(self):
        leu = False
        while not leu:
            nome_enfermeiro = input('Qual o nome do enfermeiro? ')
            nome_enfermeiro = nome_enfermeiro.title()
            novo = nome_enfermeiro.replace(' ', 'x')
            if novo.isalpha():
                leu = True
            if leu is False:
                print('Um nome deve conter apenas letras.')
        return nome_enfermeiro

    def rua_enfermeiro(self):
        leu = False
        while not leu:
            rua_enfermeiro = input('Qual o nome da rua onde resida? ')
            rua_enfermeiro = rua_enfermeiro.title()
            novo = rua_enfermeiro.replace(' ', 'x')
            if novo.isalpha():
                leu = True
            if leu is False:
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
            matricula = input('Digite sua matrícula (6 números): ')
            if matricula.isnumeric():
                if len(matricula) == 6:
                    leu = True
            if leu is False:
                print('Matrícula é definida por 6 dígitos númericos.')
        return matricula

    def info_deletar_enfermeiro(self):
        print('\033[35:40m= = = Excluir Enfermeiro = = =\033[m')
        matricula = self.matricula_enfermeiro()
        return {'matricula': matricula}

    def mostrar_enfermeiros(self):
        print('\033[34:40m= = = Enfermeiros Cadastrados = = =\033[m')
        for p in self.__controlador.lista_enfermeiros():
            print(p)
        print('*=*=*=*')
