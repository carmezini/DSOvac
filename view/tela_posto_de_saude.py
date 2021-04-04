class TelaPostoDeSaude():
    def __init__(self):
        def __init__(self, controlador):
            self.__controlador = controlador
        
    
    def nome(self):
        nome = input('Qual o nome do bairro que o posto abrange? ')
        print('*=*=*=*')
        print('Posto de Saúde {} criado!'.format(nome))
        return nome