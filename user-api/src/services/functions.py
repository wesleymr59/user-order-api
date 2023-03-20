import re

class FunctionsAux():
    def validar_email(self, email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex, email):
            return True
        else:
            return False

    def validar_telefone(self, telefone):
        regex = r'^[1-9]{2}9?[0-9]{8}$'
        if re.match(regex, telefone):
            return True
        else:
            return False

    def validar_cpf(self, cpf):
        regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if re.match(regex, cpf):
            return True
        else:
            return False