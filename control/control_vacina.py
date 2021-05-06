from model.vacina import Vacina
from view.tela_vacina import TelaVacina

class ControlVacina():
    def __init__(self, controlador_sistema):
        self.__vacinas = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_vacina = TelaVacina(self)

    def abre_tela_vacina(self):
        opcoes = {1: self.incluir_vacina,
                  2: self.deletar_vacina,
                  3: self.alterar_vacinas,
                  4: self.lista_vacinas,
                  0: self.encerra_sistema,
                  6: self.volta}
        
        while True:
            opcao = self.__tela_vacina.opcoes_tela_vacina()
            funcao = opcoes[opcao]
            funcao()

    def incluir_vacina_padrao(self):
        vacina1 = Vacina('DSOVAC', 100)
        vacina2 = Vacina('ButanVAC', 50)
        self.__vacinas.append(vacina1)
        self.__vacinas.append(vacina2)

    def incluir_vacina(self):
        info = self.__tela_vacina.incluir_vacina()
        tem_vacina = False
        for vacina in self.__vacinas:
            if info['nome'] == vacina.nome_fabricante:
                tem_vacina = True
        if tem_vacina is False:
            vacina = Vacina(info['nome'], info['qtd']) 
            self.__vacinas.append(vacina)
        else:
            raise Exception()

    def deletar_vacina(self):
        info = self.__tela_vacina.deletar_vacina()
        tem_vacina = False
        for vacina in self.__vacinas:
            if vacina.nome_fabricante == info['nome']:
                self.__vacinas.remove(vacina)
                tem_vacina = True
                break
        if tem_vacina is False:
            raise Exception()

    def alterar_vacinas(self):
        nome = self.__tela_vacina.alterar_vacina()
        tem_vacina = False
        for vacina in self.__vacinas:
            if nome['nome'] == vacina.nome_fabricante:
                info = self.__tela_vacina.info_setter_vacina()
                vacina.nome_fabricante = info['nome']
                vacina.quantidade = info['qtd']
                tem_vacina = True
                break
        if tem_vacina is False:
            raise Exception()

    def qtd_vacinas(self):
        qtd = 0
        soma = 0
        for vacina in self.__vacinas:
            qtd = vacina.quantidade
            soma = soma + qtd
        return soma
    
    def usa_dose(self):
        vacina.quantidade -= 1

    def lista_vacinas(self):
        vacinas = []
        for vacina in self.__vacinas:
            vacinas.append({'nome': vacina.nome_fabricante, 'qtd': vacina.quantidade})
        self.__tela_vacina.mostrar_vacinas(vacinas)

    def volta(self):
        self.__controlador_sistema.abre_tela()

    def encerra_sistema(self):
        self.__controlador_sistema.encerra_sistema()
