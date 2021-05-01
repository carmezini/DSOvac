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
    
    def opcoes_agendamento(self):
        self.__tela_agendamento.abre_tela_agendamento()

    def incluir_agendamento(self):
        paciente = self.__tela_agendamento.info_agendamento()
        enfermeiro = self.__controlador_sistema.obtem_enfermeiro()
        vacina = self.__controlador_sistema.obtem_vacina()
        data = self.__tela_agendamento.info_data()

    def deletar_agendamento(self):
        info = self.__tela_agendamento.info_deletar_agendamento()
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
