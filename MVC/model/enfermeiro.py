from abstract_pessoa import Pessoa

class Enfermeiro(Pessoa):
    def __init__(self, nome: str, endereco: str, matricula: str):
        super().__init__()
        self.__nome = nome
        self.__endereco = endereco
        self.__matricula = matricula
    
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
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, str):
            self.__matricula = matricula

