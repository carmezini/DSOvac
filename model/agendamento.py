from model.vacina import Vacina
from model.enfermeiro import Enfermeiro 
from model.paciente import Paciente

class Agendamento:
    def __init__(self, data: str, paciente: Paciente, enfermeiro: Enfermeiro, vacina: Vacina):
        self.__data = data
        self.__paciente = paciente
        self.__enfermeiro = enfermeiro
        self.__vacina = vacina

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        if isinstance(data, str):
            self.__data = data

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente

    @property
    def enfermeiro(self):
        return self.__enfermeiro
    
    @enfermeiro.setter
    def enfermeiro(self, enfermeiro):
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        if isinstance(vacina, Vacina):
            self.__vacina = vacina

    def __str__(self):
        return 'Paciente: {} Enfermeiro -> {} Vacina -> {} Data: {}'.format(self.__paciente,
                self.__enfermeiro, self.__vacina, self.__data)