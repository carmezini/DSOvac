from view.tela_paciente import TelaPaciente 
from model.paciente import Paciente 

class ControlPaciente():
    def __init__(self):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente(self)
    
    def opcoes_paciente(self):
        self.__tela_paciente.abre_tela_paciente()

    def incluir_paciente(self):
        info = self.__tela_paciente.info_paciente()
        paciente = Paciente(info['nome'], info['endereco'], info['ano'], info['cpf'])
        if paciente not in self.__pacientes:
            self.__pacientes.append(paciente)

    def deletar_paciente(self):
        info = self.__tela_paciente.info_paciente()
        paciente = Paciente(info['nome'], info['endereco'], info['ano'], info['cpf'])
        if paciente in self.__pacientes:
            self.__pacientes.remove(paciente)
    
    def alterar_paciente(self):
        self.deletar_paciente()
        self.incluir_paciente()
    
    @property
    def lista_pacientes(self):
        return self.__pacientes
