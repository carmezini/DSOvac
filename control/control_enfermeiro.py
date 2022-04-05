from view.tela_enfermeiro import TelaEnfermeiro
from model.enfermeiro import Enfermeiro

class ControlEnfermeiro():
    def __init__(self):
        self.__enfermeiros = []
        self.__tela_enfermeiro = TelaEnfermeiro(self)
    
    def opcoes_enfermeiro(self):
        self.__tela_enfermeiro.abre_tela_enfermeiro()

    def incluir_enfermeiro_padrao(self):
        enfermeiro1 = Enfermeiro('Thais Bardini', 'Gov. Celso Ramos', 32, '456546')
        enfermeiro2 = Enfermeiro('Jean Hauck', 'Aderbal Silva', 410, '322132')
        self.__enfermeiros.append(enfermeiro1)
        self.__enfermeiros.append(enfermeiro2)

    def incluir_enfermeiro(self):
        info = self.__tela_enfermeiro.info_enfermeiro()
        enfermeiro = Enfermeiro(info['nome'], info['rua'], info['num_casa'], info['matricula'])
        self.__enfermeiros.append(enfermeiro)

    def deletar_enfermeiro(self):
        info = self.__tela_enfermeiro.info_deletar_enfermeiro()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.matricula == info['matricula']:
                self.__enfermeiros.remove(enfermeiro)

    def alterar_enfermeiro(self):
        self.deletar_enfermeiro()
        self.incluir_enfermeiro()

    def num_enfermeiros(self):
        return len(self.__enfermeiros)

    def lista_enfermeiros(self):
        return self.__enfermeiros
