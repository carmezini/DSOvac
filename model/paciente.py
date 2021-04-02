from model.abstract_pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome: str, rua: str, num_casa: int, ano: int, cpf: str):
        super().__init__()
        self.__nome = nome
        self.__rua = rua
        self.__num_casa = num_casa
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
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua):
        if isinstance(rua, str):
            self.__rua = rua
    
    @property
    def num_casa(self):
        return self.__num_casa
    
    @num_casa.setter
    def num_casa(self, num_casa):
        if isinstance(num_casa, int):
            self.__num_casa = num_casa

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if isinstance(ano, int):
            self.__ano = ano
    
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf

    def __str__(self):
        return 'Nome: {}  CPF: {}'.format(self.__nome, self.__cpf)