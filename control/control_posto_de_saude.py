from view.tela_posto_de_saude import TelaPostoDeSaude 
from model.posto_de_saude import PostoDeSaude 

class ControlPostoDeSaude():
    def __init__(self):
        self.__posto = None
    
    def armazena_posto(self, posto):
        self.__posto = posto
