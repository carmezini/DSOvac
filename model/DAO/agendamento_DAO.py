from model.DAO.abstract_DAO import DAO
from model.agendamento import Agendamento

class AgendamentoDAO(DAO):
    def __init__(self):
        super().__init__('agendamentos.pkl')
    
    def add(self, agendamento: Agendamento):
        if (isinstance(agendamento, Agendamento)) and (agendamento is not None):
            super().add(agendamento.paciente, agendamento)

    def get(self, key):
        return super().get(key)

    def update(self, key, agendamento: Agendamento):
        self.remove(key)
        self.add(agendamento)

    def remove(self, key):
        return super().remove(key)