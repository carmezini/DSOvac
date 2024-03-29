from view.tela_sistema import TelaSistema
from control.control_agendamento import ControlAgendamento
from control.control_enfermeiro import ControlEnfermeiro
from control.control_paciente import ControlPaciente
from control.control_vacina import ControlVacina
from control.control_posto_de_saude import ControlPostoDeSaude
import random as rd

class ControlSistema():
    def __init__(self):
        self.__controlador_agendamento = ControlAgendamento(self)
        self.__controlador_enfermeiro = ControlEnfermeiro()
        self.__controlador_paciente = ControlPaciente()
        self.__controlador_vacina = ControlVacina()
        self.__controlador_posto_de_saude = ControlPostoDeSaude()
        self.__tela_sistema = TelaSistema(self)

    def inicia_sistema(self):
        self.__tela_sistema.inicie()
    
    def cria_posto(self):
        nome_posto = self.__controlador_posto_de_saude.nome()
        self.__controlador_paciente.incluir_paciente_padrao()
        self.__controlador_enfermeiro.incluir_enfermeiro_padrao()
        self.__controlador_vacina.incluir_vacina_padrao()
        self.__controlador_posto_de_saude.armazena_posto(nome_posto)
    
    def opcoes_paciente(self):
        self.__controlador_paciente.opcoes_paciente()
    
    def opcoes_enfermeiro(self):
        self.__controlador_enfermeiro.opcoes_enfermeiro()
    
    def opcoes_vacina(self):
        self.__controlador_vacina.opcoes_vacina()
    
    def opcoes_agendamento(self):
        self.__controlador_agendamento.opcoes_agendamento()
    
    def relaciona_agendamento(self):
        lista_enfermeiro = self.__controlador_enfermeiro.lista_enfermeiros()
        rd.shuffle(lista_enfermeiro)
        enfermeiro = lista_enfermeiro[0]
        lista_vacina = self.__controlador_vacina.lista_vacinas()
        rd.shuffle(lista_vacina)
        vacina = lista_vacina[0]
        return {'enfermeiro': enfermeiro,
                'vacina': vacina}

    def retorna_lista_paciente(self):
        lista_paciente = self.__controlador_paciente.lista_pacientes()
        return lista_paciente

    def relatorio_geral(self):
        nome_posto = self.__controlador_posto_de_saude.exibir_posto()
        num_pacientes = self.__controlador_paciente.num_pacientes()
        num_enfermeiros = self.__controlador_enfermeiro.num_enfermeiros()
        qtd_vacinas = self.__controlador_vacina.qtd_vacinas()
        vacinados_primeira_dose = self.__controlador_agendamento.num_vacinados_primeira_dose()
        vacinados_segunda_dose = self.__controlador_agendamento.num_vacinados_segunda_dose()
        return {'nome': nome_posto,
                'num_pacientes': num_pacientes,
                'num_enfermeiros': num_enfermeiros,
                'qtd_vacinas': qtd_vacinas,
                'uma_dose': vacinados_primeira_dose,
                'duas_doses': vacinados_segunda_dose}

    def control_enfermeiro(self):
        return self.__controlador_enfermeiro.lista_enfermeiros()

    def control_vacina(self):
        return self.__controlador_vacina.lista_vacinas()
