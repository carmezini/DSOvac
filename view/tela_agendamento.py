from view.menu import Menu

class TelaAgendamento():
    def __init__(self, controlador):
        opcoes_agendamento = {
            0: 'Voltar',
            1: 'Cadastrar Agendamento',
            2: 'Excluir Agendamento',
            3: 'Alterar Agendamento',
            4: 'Listar agendamentos'
        }
        self.__menu = Menu('\033[36:41mOpcões Agendamento\033[m ====', opcoes_agendamento)
        self.__controlador = controlador
    
    def abre_tela_agendamento(self):
        terminar = False
        while not terminar:
            menu = self.__menu
            opcao = menu.pergunte()
            if opcao == 0:
                terminar = True
            elif opcao == 1:
                try:
                    self.__controlador.incluir_agendamento()
                except Exception:
                    print('Paciente ainda não cadastrado.')
                else:
                    print('Agendamento marcado com sucesso.')
            elif opcao == 2:
                try:
                    self.__controlador.deletar_agendamento()
                except Exception:
                    print('Não foi possível deletar esse agendamento.')
                else:
                    print('Agendamento cancelado com sucesso.')
            elif opcao == 3:
                try:
                    self.__controlador.alterar_agendamento()
                except Exception:
                    print('Não foi possível alterar esse agendamento.')
                else:
                    print('Agendamento alterado com sucesso.')
            elif opcao == 4:
                self.mostrar_agendamentos()
    
    def info_agendamento(self):
        print('\033[32:40m= = = Adicionar Agendamento = = =\033[m')
        cpf_paciente = self.cpf_paciente()
        print('*=*=*=*')
        return {'cpf_paciente': cpf_paciente}

    def info_deletar_agendamento(self):
        print('\033[35:40m= = = Excluir Agendamento = = =\033[m')
        cpf_paciente = self.cpf_paciente()
        return {'cpf': cpf_paciente}
    
    def alterar_agendamento(self):
        print('\033[35:41m= = = Alterar Agendamento = = =\033[m')
        cpf_paciente = self.cpf_paciente()
        return {'cpf': cpf_paciente}
    
    def mostrar_agendamentos(self):
        print('\033[34:40m= = = Agendamentos Cadastradas = = =\033[m')
        for a in self.__controlador.lista_agendamentos():
            print(a)
        print('*=*=*=*')
    
    def cpf_paciente(self):
        leu = False
        while not leu:
            try:
                cpf_paciente = input('Qual o CPF do paciente (apenas números): ')
                if not cpf_paciente.isnumeric():
                    raise Exception
                if len(cpf_paciente) != 11:
                    raise Exception
            except Exception:
                print('CPF são 11 dígitos númericos.')
            else:
                leu = True
        return cpf_paciente

    def info_data(self):
        pass
