from view.tela_agendamento import TelaAgendamento 
from model.agendamento import Agendamento 

class ControlAgendamento():
    def __init__(self):
        self.__agendamentos = []
        self.__tela_agendamento = TelaAgendamento(self)
    
    def opcoes_agendamento(self):
        self.__tela_agendamento.abre_tela_agendamento()

    def incluir_agendamento_padrao(self):
        agendamento = Agendamento('13/04/2021', '09:00', )

    def incluir_agendamento(self):
        pass

    def deletar_agendamento(self):
        pass

    def alterar_agendamento(self):
        self.deletar_agendamento()
        self.incluir_agendamento()

    def lista_agendamentos(self):
        return self.__pacientes
