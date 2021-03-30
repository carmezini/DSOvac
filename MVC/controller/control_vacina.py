from model.vacina import Vacina
from view.vacina import TelaVacina

class ControlVacina():
    def __init__(self):
        self.__vacinas = []
    
    def add_vacina(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            for _ in range(qtd):
                self.__vacinas.append(vacina)
    
    def del_vacina(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            for i in self.__vacinas(qtd):
                if vacina.nome_fabricante == i.nome_fabricante:
                    self.__vacinas.remove(i.nome_fabricante)
    
    def setter_vacina(self):
        pass

    def get_vacinas(self):
        return self.__vacinas
        