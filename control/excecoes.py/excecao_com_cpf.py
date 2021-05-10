class ComCPFException(Exception):
    def __init__(self):
        super().__init__("CPF já está agendado!")