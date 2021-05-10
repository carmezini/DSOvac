from model.DAO.abstract_DAO import DAO
from model.paciente import Paciente

class PacienteDAO(DAO):
    def __init__(self):
        super().__init__('pacientes.pkl')

    def add(self, paciente: Paciente):
        if (isinstance(paciente.cpf, str)) and (paciente is not None) \
            and isinstance(paciente, Paciente):
            super().add(paciente.cpf, paciente)

    def get(self, key):
        return super().get(key)

    def update(self, key, paciente: Paciente):
        self.remove(key)
        self.add(paciente)

    def remove(self, key):
        return super().remove(key)