from model.DAO.abstract_DAO import DAO
from model.vacina import Vacina

class VacinaDAO(DAO):
    def __init__(self):
        super().__init__('vacinas.pkl')
    
    def add(self, vacina: Vacina):
        if (isinstance(vacina.nome_fabricante, str)) and (vacina is not None) \
            and isinstance(vacina, Vacina):
            super().add(vacina.nome_fabricante, vacina)

    def get(self, key):
        return super().get(key)

    def update(self, key, vacina: Vacina):
        self.remove(key)
        self.add(vacina)

    def remove(self, key):
        return super().remove(key)