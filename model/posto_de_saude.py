from model.agendamento import Agendamento

class PostoDeSaude:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__agendamentos = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def agendamentos(self):
        return self.__agendamentos
