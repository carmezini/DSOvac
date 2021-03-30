from control_vacina import ControlVacina

class TelaVacina():
    
    def __init__(self):
        opcoes = {
            0: Voltar
            1: Cadastrar Vacina
            2: Excluir Vacina
            3: Alterar info vacina
            4: Listar Vacinas
        }
        self.__menu = Menu('Opções Vacina', opcoes)
    
    def interaja(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                pass
            elif opcao == 1:
                nome_vacina = input('Qual o nome do fabricante? ')
                qtd = int(input('Quantas doses deseja adicionar? '))
                control_vacina.add_vacina(Vacina(nome_vacina, qtd))
                print('{} doses da vacina {} foram adicionadas ao estoque'.format(qtd, nome_vacina))
            elif opcao == 2:
                nome_vacina = input('Qual o nome do fabricante? ')
                qtd = int(input('Quantas doses deseja excluir? '))
                control_vacina.del_vacina(Vacina(nome_vacina, qtd))
                print('{} doses da vacina {} foram excluídas do estoque'.format(qtd, nome_vacina))
            elif opcao == 3:
                control_vacina.setter_vacina()
            elif opcao == 4:
                print('Vacinas em estoque: ')
                control_vacina.get_vacinas()