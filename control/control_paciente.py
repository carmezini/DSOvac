from view.tela_paciente import TelaPaciente 
from model.paciente import Paciente 

class ControlPaciente():
    def __init__(self):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente(self)
    
    def opcoes_paciente(self):
        self.__tela_paciente.abre_tela_paciente()

    def incluir_paciente_padrao(self):
        paciente1 = Paciente('Artur Carmezini', 'Felipe Neves', 268, 1999, '07429362958')
        paciente2 = Paciente('James Harden', 'AV. Santa Catarina', 13, 1991, '3123341243')
        paciente3 = Paciente('LeBron James', 'Los Angeles', 23, 1990, '3214382989')
        paciente4 = Paciente('Stephen Curry', 'Av. Oakland', 30, 1990, '321370905')
        paciente5 = Paciente('Damian Lillard', 'st. Oregon', 30, 1993, '3910482309')
        self.__pacientes.append(paciente2)
        self.__pacientes.append(paciente1)
        self.__pacientes.append(paciente3)
        self.__pacientes.append(paciente4)
        self.__pacientes.append(paciente5)

    def incluir_paciente(self):
        info = self.__tela_paciente.info_paciente()
        tem_paciente = False
        for paciente in self.__pacientes:
            if info['cpf'] == paciente.cpf:
                tem_paciente = True
        if tem_paciente is False:
            paciente = Paciente(info['nome'], info['rua'], info['num_casa'], info['ano'], info['cpf'])
            self.__pacientes.append(paciente)

    def deletar_paciente(self):
        info = self.__tela_paciente.info_deletar_paciente()
        for paciente in self.__pacientes:
            if paciente.cpf == info['cpf']:
                self.__pacientes.remove(paciente)

    def alterar_paciente(self):
        self.deletar_paciente()
        self.incluir_paciente()

    def num_pacientes(self):
        return len(self.__pacientes)

    def lista_pacientes(self):
        return self.__pacientes
