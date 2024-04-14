import json
import pprint as pp
from datetime import datetime as dt

class Cliente:
    "Estanciando cliente"

    def __init__(self, a_nome, a_cpf, a_endereco, a_conta=None):

        self._nome = self.validar_tipo_var_str(a_nome)
        self._cpf = self.validar_tipo_var_str(a_cpf)
        self._endereco =self.validar_tipo_var_str(a_endereco)

        self._conta = a_conta

    def validar_tipo_var_str(self, variavel):
        "Validar a variavel de entrada"

        if not isinstance(variavel, str):
            raise TypeError("Erro de tipo: Esperava uma String")
        return variavel



    def get_nome(self):
        "Obetem o nome"
        return self._nome

    def get_cpf(self):
        "Obtem o CPF"
        return self._cpf

    def get_endereco(self):
        "Obtem o endereço"
        return self._endereco

    def obj_add_bd(self):
        conta_info = None
        if self._conta is not None:
            conta_info = {
            "tipo": self._conta.get_tipo(),
            "Agencia": self._conta.get_agencia(),
            "Numero": self._conta.get_numero()
            }

        else:
            conta_info = "Cliente não possui conta"

        cliente_info = {
        "Nome": self.get_nome(),
        "CPF": self.get_cpf(),
        "Endereco": self.get_endereco(),
        "Data": dt.now().strftime("%d/%m/%Y"),
        "Conta": conta_info
        }

        return cliente_info


    def __str__(self):
        conta_info = None
        if self._conta is not None:
            conta_info = {
            "tipo": self._conta.get_tipo(),
            "Agencia": self._conta.get_agencia(),
            "Numero": self._conta.get_numero(),
            
            }

        else:
            conta_info = "Cliente não possui conta"

        cliente_info = {
        "Nome": self.get_nome(),
        "CPF": self.get_cpf(),
        "Endereco": self.get_endereco(),
        "Conta": conta_info
        }

        return json.dumps(cliente_info)

       # f"Nome: {self.get_nome()} \nCPF: {self.get_cpf()} \nEndereço:{self.get_endereco()}\nConta: {conta}"

class Conta:
    "asdasdasdsadsdsadas "
    def __init__(self,a_tipo, a_agencia, a_numero):
        self._tipo = self.validar_tipo_var_str(a_tipo)
        self._agencia = self.validar_tipo_var_str(a_agencia)
        self._numero = self.validar_tipo_var_str(a_numero)

    def validar_tipo_var_str(self, variavel):
        "Validar a variavel de entrada"

        if not isinstance(variavel, str):
            raise TypeError("Erro de tipo: Esperava uma String")
        return variavel


    def get_tipo(self):
        "Retorna o tipo da conta"
        return self._tipo

    def get_agencia(self):
        "Retorna a agencia"
        return self._agencia

    def get_numero(self):
        "Retorna o numero da conta"
        return self._numero

    def obj_add_bd(self):
        "Retorna um dict para ser add no mongo db"
        conta_info = {
            "Tipo": self.get_tipo(),
            "Agencia": self.get_agencia(),
            "Número": self.get_numero(),
            "Data": dt.now().strftime("%d/%m/%Y")
            }

        return conta_info

    def __str__(self):
        conta = f"""
    "Tipo": {self.get_tipo()},
    "Agencia": {self.get_agencia()},
    "Número": {self.get_numero()}
"""

        return conta



