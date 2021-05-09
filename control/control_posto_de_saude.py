from view.tela_posto_de_saude import TelaPostoDeSaude 
from model.posto_de_saude import PostoDeSaude 

class ControlPostoDeSaude():
    __instance = None

    def __init__(self):
        self.__tela_posto = TelaPostoDeSaude(self)

    def __new__(cls):
        if ControlPostoDeSaude.__instance is None:
            ControlPostoDeSaude.__instance = object.__new__(cls)
        return ControlPostoDeSaude.__instance
    
    def exibir_posto(self):
        return self.__posto

    def nome(self):
        nome = self.__tela_posto.nome()
        return nome

    def armazena_posto(self, nome_posto):
        self.__posto = PostoDeSaude(nome_posto)
    