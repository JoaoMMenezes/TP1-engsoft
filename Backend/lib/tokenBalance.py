#importar bibliotecas

from utils.dbframe import SQL2df
#from dbacess import ServerAcess

"""class User01:
    def __init__(self, matricula:int , senha:int, nome:str ,ficha:int, valorFicha:float , email=None ) -> None:
        self.matricula = matricula
        self.senha = senha
        self.nome = nome
        self.valorFicha = valorFicha  
        self.email = email
        self.ficha = ficha"""


class GetToken(): 
    def __init__(self, matricula:int, acesso, ficha = 0):
        self.matricula = matricula
        self.acesso = acesso
        self.ficha = ficha

    def getToken(self):
        comando = "select Fichas from dbo.Usuario0 where Matricula = " + str(self.matricula) 
        self.ficha = SQL2df(comando, self.acesso.connection, 0)[0][0]
        return self.ficha


"""tes = ServerAcess("LAPTOP-4BELV735", "credito_ru")
pegar_ficha = GetToken(1000000000, tes)
fichas = pegar_ficha.getToken()
print(fichas)"""

