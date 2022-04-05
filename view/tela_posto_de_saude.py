class TelaPostoDeSaude():
    def __init__(self, controlador):
        self.__controlador = controlador
        
    def nome(self):
        nome_posto = input('Qual o nome do bairro que o posto abrange? ')
        nome_posto = nome_posto.title()
        print('*=*=*=*')
        print('Posto de Saúde {} criado!'.format(nome_posto))
        return nome_posto
