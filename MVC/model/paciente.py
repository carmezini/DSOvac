from abstract_pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome: str, endereco: str, ano: int, cpf: int):
        super().__init__()
        self.__nome = nome
        self.__endereco = endereco
        self.__ano = ano
        self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        if isinstance(endereco, str):
            self.__endereco = endereco
    
    @property
    def ano(self):
        return self.__ano
    
    @ano_nascimento.setter
    def ano_nascimento(self, ano):
        if isinstance(ano, int):
            self.__ano = ano
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf
