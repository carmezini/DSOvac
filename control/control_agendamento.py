from view.tela_agendamento import TelaAgendamento 
from model.agendamento import Agendamento

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
        pass

    def deletar_agendamento(self):
        info = self.__tela_agendamento.info_deletar_agendamento()
        for agendamento in self.__agendamentos:
            if info['cpf'] == agendamento.paciente.cpf:
                self.__agendamentos.remove(agendamento)

    def alterar_agendamento(self):
        pass

    def lista_agendamentos(self):
        return self.__agendamentos
    
    def num_vacinados_primeira_dose(self):
        return len(self.__vacinados_primeira_dose)
    
    def num_vacinados_segunda_dose(self):
        return len(self.__vacinados_segunda_dose)