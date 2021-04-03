from view.menu import Menu

class TelaSistema():
    def __init__(self, controlador):
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
        self.__menu_com_posto = Menu('\033[35:40mPosto de Saúde\033[m ====', opcoes_com_posto)
        self.__menu_sem_posto = Menu('\033[32:40mMenu Principal\033[m ====', opcoes_sem_posto)
        self.__controlador = controlador
    
    def inicie(self):
        terminar = False
        while not terminar:
            if self.__posto is None:
                menu = self.__menu_sem_posto
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    posto = self.__controlador.cria_posto()
                    self.__posto = True
            else:
                menu = self.__menu_com_posto
                opcao = menu.pergunte()
                if opcao == 0:
                    terminar = True
                elif opcao == 1:
                    self.__controlador.opcoes_paciente()
                elif opcao == 2:
                    self.__controlador.opcoes_enfermeiro()
                elif opcao == 3:
                    self.__controlador.opcoes_vacina()
                elif opcao == 4:
                    self.__controlador.opcoes_agendamento()
                elif opcao == 5:
                    pass
        
    def info_posto(self):
        nome_posto = input('Qual o nome do bairro que o posto abrange? ')
        nome_posto = 'Posto de Saúde ' + nome_posto
        return nome_posto