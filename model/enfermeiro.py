from model.abstract_pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init__(self, nome: str, rua: str, num_casa: int, matricula: str):
        super().__init__()
        self.__nome = nome
        self.__rua = rua
        self.__num_casa = num_casa
        self.__matricula = matricula
    
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
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, str):
            self.__matricula = matricula
    
    def __str__(self):
        return 'Nome: {}  Matrícula: {}'.format(self.__nome, self.__matricula)
