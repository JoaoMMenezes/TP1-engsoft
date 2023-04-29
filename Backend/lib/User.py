import sys
sys.path.insert(0, r'.\TP1-engsoft\Backend\ru-server\utils')
from dbframe import SQL2df
from dbacess import

# Abstract class for user
class User:
    def __init__(self, senha: int, nome: str, ficha: int, valorFicha: float, email = None, telefone: int):
        self.senha = senha
        self.nome = nome
        self.ficha = ficha
        self.valorFicha = valorFicha
        self.email = email
        self.telefone = telefone

# Abstract 
class UserFactory:
    def create_user(self, senha, nome, ficha, valorFicha, email, telefone):
        pass

# Concrete class for student
class Aluno(User):
    def __init__(self, senha, nome, ficha, valorFicha, email, telefone, matricula):
        super().__init__(senha, nome, ficha, valorFicha, email, telefone)
        self.matricula = matricula

# Concrete class for employee
class Funcionario(User):
    def __init__(self, senha, nome, ficha, valorFicha, email, telefone, registro):
        super().__init__(senha, nome, ficha, valorFicha, email, telefone)
        self.registro = registro

# Concrete factory for student
class AlunoFactory(UserFactory):
    def create_user(self, senha, nome, ficha, valorFicha, email, telefone):
        return Aluno(senha, nome, ficha, valorFicha, email, telefone, matricula="")

# Concrete factory for employee
class FuncionarioFactory(UserFactory):
    def create_user(self, senha, nome, ficha, valorFicha, email, telefone):
        return Funcionario(senha, nome, ficha, valorFicha, email, telefone, registro="")
"""
# Instance examples
# Student
aluno_factory = AlunoFactory()
aluno = aluno_factory.create_user(senha=123456, nome="Nelson Troll", ficha=1, valorFicha=50.0, email="nelson@dino.com", telefone=123456789, matricula="12345")

# Employee
funcionario_factory = FuncionarioFactory()
funcionario = funcionario_factory.create_user(senha=567890, nome="Vinícius Seguidor de Nelson", ficha=2, valorFicha=80.0, email="vinicius@laele.com", telefone=987654321, registro="101112")
"""
