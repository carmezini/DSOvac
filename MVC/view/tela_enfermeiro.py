from controller.control_paciente import ControlPaciente 
from view.tela_sistema import TelaSistema
from view.menu import Menu

class TelaEnfermeiro():
    def __init__(self, controlador):
        opcoes_enfermeiro = {
            0: 'Voltar',
            1: 'Cadastrar enfermeiro',
            2: 'Excluir enfermeiro',
            3: 'Alterar info enfermeiro',
            4: 'Listar pacientes'
        }
        self.__menu = Menu('Opções Enfermeiro', opcoes_enfermeiro)
        self.__controlador = controlador
    
    def abre_tela_enfermeiro(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                TelaSistema.inicie()
            elif opcao == 1:
                self.__controlador.incluir_enfermeiro()
            elif opcao == 2:
                self.__controlador.deletar_enfermeiro()
            elif opcao == 3:
                self.__controlador.alterar_enfermeiro()
            elif opcao == 4:
                self.listar_enfermeiro()
    
    def info_enfermeiro(self):
        nome_enfermeiro = input('Qual o nome do enfermeiro: ')
        endereco = input('Qual a rua e o número onde resida? '))
        matricula = input('Digite a matrícula do profissional: '))
        return {'nome': nome_enfermeiro, 'endereco': endereco, 'matricula': matricula}
    
    def listar_enfermeiros(self):
        print(self.__controlador.lista_enfermeiros())
