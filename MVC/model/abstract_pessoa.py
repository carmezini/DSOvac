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
    def endereco(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome: str):
        pass

    @endereco.setter
    @abstractmethod
    def endereco(self, endereco: str):
        pass