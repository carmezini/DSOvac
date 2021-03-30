from view.tela_sistema import TelaSistema
import control_agendamento
import control_enfermeiro
import control_paciente
import control_vacina
import control_posto_de_saude

class ControlSistema():
    def __init__(self):
        self.__controlador_agendamento = ControlAgendamento()
        self.__controlador_enfermeiro = ControlEnfermeiro()
        self.__controlador_paciente = ControlPaciente()
        self.__controlador_vacina = ControlVacina()
        self.__controlador_posto_de_saude
        self.__tela_sistema = TelaSistema()

    def inicia_sistema(self):
        self.inicie()
    
    def finaliza_sistema(self):
        exit()