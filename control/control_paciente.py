from view.tela_paciente import TelaPaciente 
from model.paciente import Paciente
from model.DAO.paciente_DAO import PacienteDAO

class ControlPaciente():

    def __init__(self, controlador_sistema):
        self.__pacientes_DAO = PacienteDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_paciente = TelaPaciente(self)
    
    def abre_tela_paciente(self):
        opcoes = {1: self.incluir_paciente,
                  2: self.deletar_paciente,
                  3: self.alterar_paciente,
                  4: self.lista_pacientes,
                  0: self.encerra_sistema,
                  6: self.volta
                 }

        while True:
            opcao = self.__tela_paciente.opcoes_tela_paciente()
            funcao = opcoes[opcao]
            funcao()

    def incluir_paciente(self):
        info = self.__tela_paciente.incluir_paciente()
        tem_paciente = False
        for paciente in self.__pacientes_DAO.get_all():
            if info['cpf'] == paciente.cpf:
                tem_paciente = True
        if tem_paciente is False:
            paciente = Paciente(info['nome'], info['rua'], info['num_casa'], info['ano'], info['cpf'])
            self.__pacientes_DAO.add(paciente)
            self.__tela_paciente.sucesso_incluir()
        else:
            self.__tela_paciente.erro_cpf()

    def deletar_paciente(self):
        info = self.__tela_paciente.deletar_paciente()
        tem_paciente = False
        for paciente in self.__pacientes_DAO.get_all():
            if paciente.cpf == info['cpf']:
                self.__pacientes_DAO.remove(paciente.cpf)
                tem_paciente = True
                self.__tela_paciente.sucesso_deletar()
                break
        if tem_paciente is False:
            self.__tela_paciente.erro_sem_cpf()

    def alterar_paciente(self):
        cpf = self.__tela_paciente.alterar_paciente()
        tem_paciente = False
        for paciente in self.__pacientes_DAO.get_all():
            if cpf['cpf'] == paciente.cpf:
                info = self.__tela_paciente.info_setter_paciente()
                paciente.nome = info['nome']
                paciente.rua = info['rua']
                paciente.num_casa = info['num_casa']
                paciente.ano = info['ano']
                paciente.cpf = info['cpf']
                self.__pacientes_DAO.update(cpf['cpf'], paciente)
                tem_paciente = True
                self.__tela_paciente.sucesso_alterar()
                break
        if tem_paciente is False:
            self.__tela_paciente.erro_sem_cpf()

    def num_pacientes(self):
        return len(self.__pacientes_DAO.get_all())

    def lista_pacientes(self):
        pacientes = []
        for paciente in self.__pacientes_DAO.get_all():
            pacientes.append({'nome': paciente.nome, 'cpf': paciente.cpf})
        self.__tela_paciente.mostrar_pacientes(pacientes)
    
    def listar_pacientes(self):
        lista = self.__pacientes_DAO.get_all()
        lista_n = []
        for paciente in lista:
            lista_n.append(paciente)
        return lista_n

    def volta(self):
        self.__controlador_sistema.abre_tela()
    
    def encerra_sistema(self):
        self.__controlador_sistema.encerra_sistema()
