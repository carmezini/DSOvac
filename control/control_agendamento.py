from view.tela_agendamento import TelaAgendamento 
from model.agendamento import Agendamento
from model.DAO.agendamento_DAO import AgendamentoDAO

class ControlAgendamento():
    def __init__(self, controlador_sistema):
        self.__agendamentos_DAO = AgendamentoDAO()
        self.__tela_agendamento = TelaAgendamento(self)
        self.__controlador_sistema = controlador_sistema
        self.__vacinados_primeira_dose = []
        self.__vacinados_segunda_dose = []
    
    def abre_tela_agendamento(self):
        opcoes = {1: self.incluir_agendamento,
                  2: self.deletar_agendamento,
                  3: self.lista_agendamentos,
                  0: self.encerra_sistema,
                  6: self.volta
                 }

        while True:
            opcao = self.__tela_agendamento.opcoes_tela_agendamento()
            funcao = opcoes[opcao]
            funcao()

    def incluir_agendamento(self):
        tem_cpf = False
        paciente_cpf = self.__tela_agendamento.incluir_agendamento()
        for agendamento in self.__agendamentos_DAO.get_all():
            if agendamento.paciente.cpf == paciente_cpf['cpf']:
                self.__tela_paciente.erro_cpf()
                tem_cpf = True
        if tem_cpf is False:
            dict_data = self.verifica_data()
            data = dict_data['data']
            hora = dict_data['hora']
            enfermeiro = self.__controlador_sistema.obtem_enfermeiro()
            vacina = self.__controlador_sistema.obtem_vacina()
            pacientes_cadastrados = self.__controlador_sistema.listar_pacientes()
            tem_paciente = True
            if tem_paciente is True:
                for paciente in pacientes_cadastrados:
                    if paciente_cpf['cpf'] == paciente.cpf:
                        agendamento = Agendamento(data, hora, paciente, enfermeiro, vacina)
                        self.__agendamentos_DAO.add(agendamento)
                        self.__vacinados_primeira_dose.append(paciente)
                        vacina.usa_dose()
                        break

    def deletar_agendamento(self):
        info = self.__tela_agendamento.deletar_agendamento()
        tem_agendamento = False
        for agendamento in self.__agendamentos_DAO.get_all():
            if info['cpf'] == agendamento.paciente.cpf:
                self.__agendamentos_DAO.remove(agendamento.paciente)
                tem_agendamento = True
                break
        if tem_agendamento is False:
            raise Exception()

    def lista_agendamentos(self):
        agendamentos = []
        for agendamento in self.__agendamentos_DAO.get_all():
            agendamentos.append({'nome': agendamento.paciente.nome, 'cpf': agendamento.paciente.cpf,
                                 'data': agendamento.data, 'hora': agendamento.hora,
                                 'enfermeiro': agendamento.enfermeiro.nome, 'vacina': agendamento.vacina.nome_fabricante
                                })
        self.__tela_agendamento.mostrar_agendamentos(agendamentos)

    def listar_agendamentos(self):
        lista = self.__agendamentos_DAO.get_all()
        lista_n = []
        for agendamento in lista:
            lista_n.append(agendamento)
        return lista_n
    
    def num_vacinados_primeira_dose(self):
        return len(self.__vacinados_primeira_dose)
    
    def num_vacinados_segunda_dose(self):
        return len(self.__vacinados_segunda_dose)

    def volta(self):
        self.__controlador_sistema.abre_tela()
    
    def encerra_sistema(self):
        self.__controlador_sistema.encerra_sistema()

    def verifica_data(self):
        tem_hora = True
        data = self.__tela_agendamento.calendar()
        hora = self.__tela_agendamento.hora()
        for agendamento in self.__agendamentos_DAO.get_all():
            if agendamento.data == data:
                if agendamento.hora == hora:
                    tem_hora = False
                    self.__tela_agendamento.erro_hora()
        if tem_hora is True:
            return {'data': data, 'hora': hora}

    def data_duas_doses(self, data):
        tem_hora = True
        hora = self.__tela_agendamento.hora()
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

        if tem_hora is True:
            return {'data': data_segunda_dose, 'hora': hora}

    def volta_agendamento(self):
        self.abre_tela_agendamento()