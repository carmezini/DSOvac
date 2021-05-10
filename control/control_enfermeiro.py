from view.tela_enfermeiro import TelaEnfermeiro
from model.enfermeiro import Enfermeiro
from model.DAO.enfermeiro_DAO import EnfermeiroDAO

class ControlEnfermeiro():
    def __init__(self, controlador_sistema):
        self.__enfermeiros_DAO = EnfermeiroDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_enfermeiro = TelaEnfermeiro(self)
    
    def abre_tela_enfermeiro(self):
        opcoes = {1: self.incluir_enfermeiro,
                  2: self.deletar_enfermeiro,
                  3: self.alterar_enfermeiro,
                  4: self.lista_enfermeiros,
                  0: self.encerra_sistema,
                  6: self.volta
                }

        while True:
            opcao = self.__tela_enfermeiro.opcoes_tela_enfermeiro()
            funcao = opcoes[opcao]
            funcao()

    def incluir_enfermeiro(self):
        info = self.__tela_enfermeiro.incluir_enfermeiro()
        tem_enfermeiro = False
        for enfermeiro in self.__enfermeiros_DAO.get_all():
            if info['matricula'] == enfermeiro.matricula:
                tem_enfermeiro = True
        if tem_enfermeiro is False:
            enfermeiro = Enfermeiro(info['nome_enfermeiro'], info['rua_enfermeiro'], info['num_casa_enfermeiro'], info['matricula'])
            self.__enfermeiros_DAO.add(enfermeiro)
            self.__tela_enfermeiro.sucesso_incluir()
        else:
            self.__tela_enfermeiro.erro_matricula()

    def deletar_enfermeiro(self):
        info = self.__tela_enfermeiro.deletar_enfermeiro()
        tem_enfermeiro = False
        for enfermeiro in self.__enfermeiros_DAO.get_all():
            if enfermeiro.matricula == info['matricula']:
                self.__enfermeiros_DAO.remove(enfermeiro.matricula)
                tem_enfermeiro = True
                self.__tela_enfermeiro.sucesso_deletar()
                break
        if tem_enfermeiro is False:
            self.__tela_enfermeiro.erro_sem_matricula()

    def alterar_enfermeiro(self):
        matricula = self.__tela_enfermeiro.alterar_enfermeiro()
        tem_enfermeiro = False
        for enfermeiro in self.__enfermeiros_DAO.get_all():
            if enfermeiro.matricula == matricula['matricula']:
                info = self.__tela_enfermeiro.info_setter_enfermeiro()
                enfermeiro.nome = info['nome_enfermeiro']
                enfermeiro.rua = info['rua_enfermeiro']
                enfermeiro.num_casa = info['num_casa_enfermeiro']
                enfermeiro.matricula = info['matricula']
                self.__enfermeiros_DAO.update(matricula['matricula'], enfermeiro)
                tem_enfermeiro = True
                self.__tela_enfermeiro.sucesso_alterar()
                break
        if tem_enfermeiro is False:
            self.__tela_enfermeiro.erro_sem_matricula()

    def num_enfermeiros(self):
        return len(self.__enfermeiros_DAO.get_all())

    def lista_enfermeiros(self):
        enfermeiros = []
        for enfermeiro in self.__enfermeiros_DAO.get_all():
            enfermeiros.append({'nome_enfermeiro': enfermeiro.nome, 'matricula': enfermeiro.matricula})
        self.__tela_enfermeiro.mostrar_enfermeiros(enfermeiros)

    def listar_enfermeiros(self):
        lista = self.__enfermeiros_DAO.get_all()
        lista_n = []
        for enfermeiro in lista:
            lista_n.append(enfermeiro)
        return lista_n

    def volta(self):
        self.__controlador_sistema.abre_tela()

    def encerra_sistema(self):
        self.__controlador_sistema.encerra_sistema()
