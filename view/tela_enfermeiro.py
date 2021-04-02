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
        self.__menu = Menu('\033[36:41mOpções Enfermeiros\033[m ===', opcoes_enfermeiro)
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
        nome_enfermeiro = input('Qual o nome do enfermeiro? ')
        rua = input('Qual a rua onde resida? ')
        num_casa = int(input('Qual o número da residência? '))
        matricula = input('Digite sua matrícula (apenas números): ')
        print('*=*=*=*')
        return {'nome': nome_enfermeiro, 'rua': rua, 'num_casa': num_casa, 'matricula': matricula}

    def info_deletar_enfermeiro(self):
        print('\033[35:40m= = = Excluir Enfermeiro = = =\033[m')
        matricula = input('Qual a matrícula do enfermeiro? ')
        return {'matricula': matricula}

    def mostrar_enfermeiros(self):
        print('\033[34:40m= = = Enfermeiros Cadastrados = = =\033[m')
        for p in self.__controlador.lista_enfermeiros():
            print(p)
        print('*=*=*=*')
