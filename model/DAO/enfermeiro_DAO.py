from model.DAO.abstract_DAO import DAO
from model.enfermeiro import Enfermeiro

class EnfermeiroDAO(DAO):
    def __init__(self):
        super().__init__('enfermeiros.pkl')
    
    def add(self, enfermeiro: Enfermeiro):
        if (isinstance(enfermeiro.matricula, str)) and (enfermeiro is not None) \
            and isinstance(enfermeiro, Enfermeiro):
            super().add(enfermeiro.matricula, enfermeiro)

    def get(self, key):
        return super().get(key)

    def update(self, key, enfermeiro: Enfermeiro):
        self.remove(key)
        self.add(enfermeiro)

    def remove(self, key):
        return super().remove(key)