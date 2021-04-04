from view.tela_posto_de_saude import TelaPostoDeSaude 
from model.posto_de_saude import PostoDeSaude 

class ControlPostoDeSaude():
    def __init__(self):
        self.__nome_posto = ''
        self.__tela_posto = TelaPostoDeSaude()
    
    def armazena_posto(self, posto):
        self.__posto = PostoDeSaude(posto)
    
    def exibir_posto(self):
        return self.__posto

    def nome(self):
        self.__nome_posto = self.__tela_posto.nome()