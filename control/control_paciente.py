from view.tela_paciente import TelaPaciente 
from model.paciente import Paciente

class ControlPaciente():
    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_paciente = TelaPaciente(self)
    
    def abre_tela_paciente(self):
        opcoes = {1: self.incluir_paciente,
                  2: self.deletar_paciente,
                  3: self.alterar_paciente,
                  4: self.lista_pacientes,
                  0: self.encerra_sistema,
                  6: self.volta
                 }
        while True:
            opcao = self.__tela_paciente.opcoes_tela_paciente()
            funcao = opcoes[opcao]
            funcao()

    def incluir_paciente_padrao(self):
        paciente1 = Paciente('Artur Carmezini', 'Felipe Neves', 268, 1999, '07429362958')
        paciente2 = Paciente('James Harden', 'AV. Santa Catarina', 13, 1991, '31233412436')
        paciente3 = Paciente('LeBron James', 'Los Angeles', 23, 1990, '32143829896')
        paciente4 = Paciente('Stephen Curry', 'Av. Oakland', 30, 1990, '32137090545')
        paciente5 = Paciente('Damian Lillard', 'st. Oregon', 30, 1993, '09104823098')
        self.__pacientes.append(paciente2)
        self.__pacientes.append(paciente1)
        self.__pacientes.append(paciente3)
        self.__pacientes.append(paciente4)
        self.__pacientes.append(paciente5)

    def incluir_paciente(self):
        info = self.__tela_paciente.incluir_paciente()
        tem_paciente = False
        for paciente in self.__pacientes:
            if info['cpf'] == paciente.cpf:
                tem_paciente = True
        if tem_paciente is False:
            paciente = Paciente(info['nome'], info['rua'], info['num_casa'], info['ano'], info['cpf'])
            self.__pacientes.append(paciente)
        else:
            raise Exception()

    def deletar_paciente(self):
        info = self.__tela_paciente.deletar_paciente()
        tem_paciente = False
        for paciente in self.__pacientes:
            if paciente.cpf == info['cpf']:
                self.__pacientes.remove(paciente)
                tem_paciente = True
                break
        if tem_paciente is False:
            raise Exception()

    def alterar_paciente(self):
        cpf = self.__tela_paciente.alterar_paciente()
        tem_paciente = False
        for paciente in self.__pacientes:
            if cpf['cpf'] == paciente.cpf:
                info = self.__tela_paciente.info_setter_paciente()
                paciente.nome = info['nome']
                paciente.rua = info['rua']
                paciente.num_casa = info['num_casa']
                paciente.ano = info['ano']
                paciente.cpf = info['cpf']
                tem_paciente = True
                break
        if tem_paciente is False:
            raise Exception()

    def num_pacientes(self):
        return len(self.__pacientes)

    def lista_pacientes(self):
        pacientes = []
        for paciente in self.__pacientes:
            pacientes.append({'nome': paciente.nome, 'cpf': paciente.cpf})
        self.__tela_paciente.mostrar_pacientes(pacientes)

    def close(self):
        self.__tela_paciente.close()
    
    def volta(self):
        self.__controlador_sistema.abre_tela()
    
    def encerra_sistema(self):
        self.__controlador_sistema.encerra_sistema()