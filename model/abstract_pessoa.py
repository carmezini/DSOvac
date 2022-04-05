from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @property
    @abstractmethod
    def nome(self):
        pass

    @property
    @abstractmethod
    def rua(self):
        pass
    
    @property
    @abstractmethod
    def num_casa(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        pass

    @rua.setter
    @abstractmethod
    def rua(self, rua: str):
        pass

    @num_casa.setter
    @abstractmethod
    def num_casa(self, num_casa: int):
        pass