from view.tela_paciente import TelaPaciente 
from model.paciente import Paciente 

class ControlPaciente():
    def __init__(self):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()

    def add_paciente(self):
        paciente = Paciente(info['nome'], info['endereco'], info['ano'], info['cpf'])
        self.__pacientes.append(paciente)
    
    def del_paciente(self):
        paciente = Paciente(info['nome'], info['endereco'], info['ano'], info['cpf'])
        if paciente in self.__pacientes:
            self.__pacientes.remove(paciente)
    
    def altera_paciente(self, paciente: Paciente):
        if paciente in self.__pacientes:
            self.del_paciente
            self.add_paciente
        