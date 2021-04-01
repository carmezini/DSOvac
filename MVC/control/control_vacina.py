from model.vacina import Vacina
from view.vacina import TelaVacina

class ControlVacina():
    def __init__(self):
        self.__vacinas = []
        self.__tela_vacina = TelaVacina(self)
    
    def opcoes_vacina(self):
        self.__tela_vacina.abre_tela_vacina()
    
    def incluir_vacina(self, qtd):
        info = self.__tela_vacina.info_vacina()
        vacina = Vacina(info['nome'])
        if vacina not in self.__vacinas:
            for _ in range(qtd):
                self.__vacinas.append(vacina)
    
    def deletar_vacina(self):
        info = self.__tela_vacina.info_vacina()
        vacina = Vacina(info['nome'])
        if vacina in self.__vacinas:
            self.__vacinas.remove(vacina)

    def alterar_vacinas(self):
        self.deletar_vacina()
        self.incluir_vacina()

    @property
    def lista_vacina(self):
        return self.__vacinas
        