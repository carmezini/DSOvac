from view.tela_sistema import TelaSistema
from control.control_agendamento import ControlAgendamento
from control.control_enfermeiro import ControlEnfermeiro
from control.control_paciente import ControlPaciente
from control.control_vacina import ControlVacina
from control.control_posto_de_saude import ControlPostoDeSaude

class ControlSistema():
    def __init__(self):
        self.__controlador_agendamento = ControlAgendamento()
        self.__controlador_enfermeiro = ControlEnfermeiro()
        self.__controlador_paciente = ControlPaciente()
        self.__controlador_vacina = ControlVacina()
        self.__controlador_posto_de_saude = ControlPostoDeSaude()
        self.__tela_sistema = TelaSistema(self)

    def inicia_sistema(self):
        self.__tela_sistema.inicie()
    
    def cria_posto(self):
        posto = self.__tela_sistema.info_posto()
        self.__controlador_paciente.incluir_paciente_padrao()
        self.__controlador_enfermeiro.incluir_enfermeiro_padrao()
        self.__controlador_vacina.incluir_vacina_padrao()
        self.__controlador_posto_de_saude.armazena_posto(posto)
    
    def opcoes_paciente(self):
        self.__controlador_paciente.opcoes_paciente()
    
    def opcoes_enfermeiro(self):
        self.__controlador_enfermeiro.opcoes_enfermeiro()
    
    def opcoes_vacina(self):
        self.__controlador_vacina.opcoes_vacina()
    
    def finaliza_sistema(self):
        exit()
