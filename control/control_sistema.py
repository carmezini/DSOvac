from view.tela_sistema import TelaSistema
from control.control_agendamento import ControlAgendamento
from control.control_enfermeiro import ControlEnfermeiro
from control.control_paciente import ControlPaciente
from control.control_vacina import ControlVacina
from control.control_posto_de_saude import ControlPostoDeSaude
import random as rd

class ControlSistema():
    __instance = None

    def __init__(self):
        self.__controlador_agendamento = ControlAgendamento(self)
        self.__controlador_enfermeiro = ControlEnfermeiro(self)
        self.__controlador_paciente = ControlPaciente(self)
        self.__controlador_vacina = ControlVacina(self)
        self.__controlador_posto_de_saude = ControlPostoDeSaude()
        self.__tela_sistema = TelaSistema(self)
    
    def __new__(cls):
        if ControlSistema.__instance is None:
            ControlSistema.__instance = object.__new__(cls)
        return ControlSistema.__instance

    def inicia_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {1: self.opcoes_paciente,
                  2: self.opcoes_enfermeiro,
                  3: self.opcoes_vacina,
                  4: self.opcoes_agendamento,
                  5: self.__tela_sistema.exibir_relatorio_geral,
                  0: self.encerra_sistema
                 }
        while True:
            opcao = self.__tela_sistema.opcoes_tela()
            funcao = opcoes[opcao]
            funcao()              

    def encerra_sistema(self):
        exit(0)

    def opcoes_paciente(self):
        self.__controlador_paciente.abre_tela_paciente()

    def opcoes_enfermeiro(self):
        self.__controlador_enfermeiro.abre_tela_enfermeiro()

    def opcoes_vacina(self):
        self.__controlador_vacina.abre_tela_vacina()

    def opcoes_agendamento(self):
        self.__controlador_agendamento.abre_tela_agendamento()

    def relatorio_geral(self):
        num_pacientes = self.__controlador_paciente.num_pacientes()
        num_enfermeiros = self.__controlador_enfermeiro.num_enfermeiros()
        qtd_vacinas = self.__controlador_vacina.qtd_vacinas()
        vacinados_primeira_dose = self.__controlador_agendamento.num_vacinados_primeira_dose()
        vacinados_segunda_dose = self.__controlador_agendamento.num_vacinados_segunda_dose()
        return {'num_pacientes': num_pacientes,
                'num_enfermeiros': num_enfermeiros,
                'qtd_vacinas': qtd_vacinas,
                'uma_dose': vacinados_primeira_dose,
                'duas_doses': vacinados_segunda_dose}

    def listar_enfermeiros(self):
        return self.__controlador_enfermeiro.listar_enfermeiros()

    def listar_vacinas(self):
        return self.__controlador_vacina.listar_vacinas()

    def listar_pacientes(self):
        return self.__controlador_paciente.listar_pacientes()

    def obtem_enfermeiro(self):
        lista_enfermeiro = self.__controlador_enfermeiro.listar_enfermeiros()
        rd.shuffle(lista_enfermeiro)
        enfermeiro = lista_enfermeiro[0]
        return enfermeiro
    
    def obtem_vacina(self):
        lista_vacina = self.__controlador_vacina.listar_vacinas()
        rd.shuffle(lista_vacina)
        vacina = lista_vacina[0]
        return vacina