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
            elif opcao == 2:
                self.__controlador.deletar_agendamento()
            elif opcao == 3:
                self.__controlador.alterar_agendamento()
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
    
    def mostrar_agendamentos(self):
        print('\033[34:40m= = = Agendamentos Cadastradas = = =\033[m')
        for a in self.__controlador.lista_agendamentos():
            print(a)
        print('*=*=*=*')
    
    def cpf_paciente(self):
        leu = False
        while not leu:
            cpf_paciente = input('Qual o CPF do paciente (apenas números): ')
            if cpf_paciente.isnumeric():
                if len(cpf_paciente) == 11:
                    leu = True
            if leu is False:
                print('CPF são 11 dígitos númericos.')
        return cpf_paciente

    def info_data(self):
        terminar = False
        data = {
            0: '10/04/2021',
            1: '11/04/2021',
            2: '12/04/2021',
            4: '13/04/2021',
            5: '14/04/2021',
            6: '15/04/2021',
            7: '16/04/2021'
        }
        while not terminar:
            menu = Menu('Data Agendamento ===', data)
            opcao = menu.pergunte()
            if opcao == 0:
                return data[0]
            elif opcao == 1:
                return data[1]
            elif opcao == 2:
                return data[2]
            elif opcao == 3:
                return data[3]
            elif opcao == 4:
                return data[4]
            elif opcao == 5:
                return data[5]
            elif opcao == 6:
                return data[6]
            elif opcao == 7:
                return data[7]
        
    def info_hora(self):
        terminar = False
        hora = {
            0: '08:00',
            1: '09:00',
            2: '10:00',
            3: '11:00',
            4: '13:00',
            5: '14:00',
            6: '15:00',
            7: '16:00',
            8: '17:00',
            9: '18:00'
        }
        while not terminar:
            menu = Menu('Hora Agendamento ===', hora)
            opcao = menu.pergunte()
            if opcao == 0:
                return hora[0]
            elif opcao == 1:
                return hora[1]
            elif opcao == 2:
                return hora[2]
            elif opcao == 3:
                return hora[3]
            elif opcao == 4:
                return hora[4]
            elif opcao == 5:
                return hora[5]
            elif opcao == 6:
                return hora[6]
            elif opcao == 7:
                return hora[7]
            elif opcao == 8:
                return hora[8]
            elif opcao == 9:
                return hora[9]
