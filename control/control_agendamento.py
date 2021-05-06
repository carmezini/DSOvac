from view.tela_agendamento import TelaAgendamento 
from model.agendamento import Agendamento
import datetime as dt

class ControlAgendamento():
    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela_agendamento = TelaAgendamento(self)
        self.__controlador_sistema = controlador_sistema
        self.__vacinados_primeira_dose = []
        self.__vacinados_segunda_dose = []
    
    def abre_tela_agendamento(self):
        opcoes = {1: self.incluir_agendamento,
                  2: self.deletar_agendamento,
                  3: self.alterar_data_agendamento,
                  4: self.lista_agendamentos,
                  0: self.encerra_sistema,
                  6: self.volta
                 }

        while True:
            opcao = self.__tela_agendamento.opcoes_tela_agendamento()
            funcao = opcoes[opcao]
            funcao()

    def incluir_agendamento(self):
        paciente = self.__tela_agendamento.incluir_agendamento()
        data = self.__tela_agendamento.calendar()
        enfermeiro = self.__controlador_sistema.obtem_enfermeiro()
        vacina = self.__controlador_sistema.obtem_vacina()

    def deletar_agendamento(self):
        info = self.__tela_agendamento.deletar_agendamento()
        tem_agendamento = False
        for agendamento in self.__agendamentos:
            if info['cpf'] == agendamento.paciente.cpf:
                self.__agendamentos.remove(agendamento)
                tem_agendamento = True
                break
        if tem_agendamento is False:
            raise Exception()

    def alterar_data_agendamento(self):
        data_agendamento = self.__tela_agendamento.alterar_agendamento()
        tem_agendamento = False
        for agendamento in self.__agendamentos:
            if agendamento.agendamento == ['matricula']:
                info = self.__tela_agendamento.info_data()
                agendamento.data = info['data']
                tem_agendamento = True
                break
        if tem_agendamento is False:
            raise Exception()

    def lista_agendamentos(self):
        return self.__agendamentos
    
    def num_vacinados_primeira_dose(self):
        return len(self.__vacinados_primeira_dose)
    
    def num_vacinados_segunda_dose(self):
        return len(self.__vacinados_segunda_dose)

    def volta(self):
        self.__controlador_sistema.abre_tela()
    
    def encerra_sistema(self):
        self.__controlador_sistema.encerra_sistema()

