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
        dict_enf_vac = self.__controlador_sistema.relaciona_agendamento()
        dict_cpf_paciente = self.__tela_agendamento.info_agendamento()
        lista_pacientes = self.__controlador_sistema.retorna_lista_paciente()
        data = self.__tela_agendamento.info_data()
        hora = self.__tela_agendamento.info_hora()
        tem_paciente = False
        ja_tem_hora_data = False
        for paciente in lista_pacientes:
            if dict_cpf_paciente['cpf_paciente'] == paciente.cpf:
                tem_paciente = True
                break
        if tem_paciente is False:
            raise Exception
        for agendamento in self.__agendamentos:
            if data == agendamento.data:
                if hora == agendamento.hora:
                    ja_tem_hora_data = True
        if ja_tem_hora_data is False and tem_paciente is True:
            dia = data[0:2]
            dia = int(dia)
            mes = data[3:5]
            mes = int(mes)
            ano = data[6:10]
            ano = int(ano)
            dia += 20
            soma = 0
            if dia > 30:
                soma = dia - 30
                dia = soma
                mes += 1
                if mes > 12:
                    mes = 1
                    ano += 1
        data_segunda_dose = '{}/0{}/{}'.format(str(dia), str(mes), str(ano))
        agendamento = Agendamento(data, hora, paciente, dict_enf_vac['enfermeiro'], dict_enf_vac['vacina'])
        self.__agendamentos.append(agendamento)
        vacina = dict_enf_vac['vacina']
        vacina.usa_dose()
        reagendamento = Agendamento(data_segunda_dose, hora, paciente, dict_enf_vac['enfermeiro'], dict_enf_vac['vacina'])
        self.__agendamentos.append(reagendamento)
        vacina = dict_enf_vac['vacina']
        vacina.usa_dose()
        if paciente not in self.__vacinados_primeira_dose:
            self.__vacinados_primeira_dose.append(paciente)
        else:
            self.__vacinados_primeira_dose.remove(paciente)
            self.__vacinados_segunda_dose.append(paciente)


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
    
    def num_vacinados_primeira_dose(self):
        return len(self.__vacinados_primeira_dose)
    
    def num_vacinados_segunda_dose(self):
        return len(self.__vacinados_segunda_dose)