from model.vacina import Vacina
from model.enfermeiro import Enfermeiro 
from model.paciente import Paciente

class Agendamento:
    def __init__(self, data: str, horario: str, paciente: Paciente, enfermeiro: Enfermeiro
                 vacina: Vacina):
        self.__data = data
        self.__horario = horario
        self.__pacientes = []
        self.__enfermeiros = []
        self.__vacinas = []
        self.__vacinados_primeira = []
        self.__vacinados_segunda = []
    
    @property
    def data(self):
        return self.__data