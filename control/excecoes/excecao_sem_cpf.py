class SemCPFException(Exception):
    def __init__(self):
        super().__init__("CPF ainda não cadastrado!")