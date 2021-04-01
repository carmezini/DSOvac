from view.tela_enfermeiro import TelaEnfermeiro 
from model.enfermeiro import Enfermeiro 

class ControlEnfermeiro():
    def __init__(self):
        self.__enfermeiros = []
        self.__tela_enfermeiro = TelaEnfermeiro(self)

    def opcoes_enfermeiro(self):
        self.__tela_enfermeiro.abre_tela_enfermeiro()

    def incluir_enfermeiro(self):
        info = self.__tela_enfermeiro.info_enfermeiro()
        enfermeiro = Enfermeiro(info['nome'], info['endereco'], info['matricula'])
        if enfermeiro not in self.__enfermeiros:
            self.__enfermeiros.append(enfermeiro)

    def deletar_enfermeiro(self):
        info = self.__tela_enfermeiro.info_enfermeiro()
        enfermeiro = Enfermeiro(info['nome'], info['endereco'], info['matricula'])
        if enfermeiro in self.__enfermeiros:
            self.__enfermeiros.remove(enfermeiro)

    def alterar_enfermeiro(self):
        self.deletar_enfermeiro()
        self.incluir_enfermeiro()

    @property
    def lista_enfermeiros(self):
        return self.__enfermeiros
