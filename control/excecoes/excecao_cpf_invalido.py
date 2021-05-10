class ComCPFInvalidoException(Exception):
    def __init__(self):
        super().__init__('CPF são 11 dígitos númericos.')