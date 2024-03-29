class Vacina:
    def __init__(self, nome_fabricante: str, quantidade: int):
        self.__nome_fabricante = nome_fabricante
        self.__quantidade = quantidade
    
    @property
    def nome_fabricante(self):
        return self.__nome_fabricante
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade

    @nome_fabricante.setter
    def nome_fabricante(self, nome_fabricante):
        if isinstance(nome_fabricante, str):
            self.__nome_fabricante = nome_fabricante
    
    def usa_dose(self):
        self.__quantidade -= 1

    def __str__(self):
        return 'Nome: {} '.format(self.__nome_fabricante)