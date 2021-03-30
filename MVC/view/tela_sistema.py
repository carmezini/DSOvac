from menu import Menu

class TelaSistema():
    def __init__(self):
        self.__posto = None
        opcoes_com_posto = {
            0: 'Destruir posto',
            1: 'Opções paciente',
            2: 'Opções enfermeiro',
            3: 'Opções vacina',
            4: 'Opções agendamento',
            5: 'Relatório geral do posto'
        }
        opcoes_sem_posto = {
            0: 'Sair',
            1: 'Criar posto'
        }
        self.__menu_com_posto = Menu('=== Menu Principal ===', opcoes_com_posto)
        self.__menu_sem_posto = Menu('=== Menu Principal ===', opcoes_sem_posto)
    
    def inicie(self):
        terminar = False
        while not terminar:
            if self.__posto is None:
                menu = self.__menu_sem_posto
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    pass
            else:
                menu = self.__menu_com_posto
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    pass
                elif opcao == 2:
                    pass
                elif opcao == 3:
                    pass
                elif opcao == 4:
                    pass
                elif opcao == 5:
                    pass