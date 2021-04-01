from model.vacina import Vacina
from model.enfermeiro import Enfermeiro 
from model.paciente import Paciente

class Agendamento:
    def __init__(self, data: str, horario: str, paciente: Paciente, enfermeiro: Enfermeiro, vacina: Vacina):
        self.__data = data
        self.__horario = horario
        self.__pacientes = paciente
        self.__enfermeiro = enfermeiro
        self.__vacinas = vacina
    
    @property
    def data(self):
        return self.__data
    
    @property
    def horario(self):
        return self.__horario
    
    @property
    def paciente(self):
        return self.__paciente
    
    @property
    def enfermeiro(self):
        return self.__enfermeiro
    
    @property
    def vacina(self):
        return self.__vacina
