from view.tela_agendamento import TelaAgendamento 
from model.agendamento import Agendamento

class ControlAgendamento():
    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela_agendamento = TelaAgendamento(self)
        self.__controlador_sistema = controlador_sistema
        self.__lista_data = ['10/04/2021', '11/04/2021', '12/04/2021', '13/04/2021', '14/04/2021'
                             '15/04/2021', '16/04/2021', '17/04/2021', '18/04/2021', '19/04/2021']
        self.__lista_hora = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00',
                             '17:00', '18:00']
    
    def opcoes_agendamento(self):
        self.__tela_agendamento.abre_tela_agendamento()

    def incluir_agendamento(self):
        dict_enf_vac = self.__controlador_sistema.relaciona_agendamento()
        dict_cpf_paciente = self.__tela_agendamento.info_agendamento()
        lista_pacientes = self.__controlador_sistema.retorna_lista_paciente()
        for paciente in lista_pacientes:
            if dict_cpf_paciente['cpf_paciente'] == paciente.cpf:
                agendamento = Agendamento(self.__lista_data[0], self.__lista_hora[0], paciente, dict_enf_vac['enfermeiro'], dict_enf_vac['vacina'])
                self.__agendamentos.append(agendamento)
                self.__lista_hora.pop(0)

    def deletar_agendamento(self):
        info = self.__tela_agendamento.info_deletar_agendamento()
        for agendamento in self.__agendamentos:
            if info['cpf'] == agendamento.paciente.cpf:
                self.__agendamentos.remove(agendamento)

    def alterar_agendamento(self):
        self.deletar_agendamento()
        self.incluir_agendamento()

    def lista_agendamentos(self):
        return self.__agendamentos
