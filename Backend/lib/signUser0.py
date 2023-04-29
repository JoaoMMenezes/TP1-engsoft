from utils.dbframe import insert_1_element

class User:
    def __init__(self, matricula:int , senha: int, nome: str, valorFicha: float, acesso, email = None):
        self.matricula = matricula
        self.senha = senha
        self.nome = nome
        self.ficha = 0
        self.valorFicha = valorFicha
        self.email = email
        self.acesso = acesso

    def signInUser0(self):
        assert ((self.matricula > 0) & (self.matricula < 10000000000))  , "Not valid registration"
        assert ((self.senha > 0) & (self.senha < 1000000))  , "Not valid passcode"
        assert ((self.valorFicha == 0.0) |
                (self.valorFicha == 1.0) | 
                (self.valorFicha == 2.0) |
                (self.valorFicha == 2.9) |
                (self.valorFicha == 5.6)
                ) , "Not valid TokenValue for User0"
        vetor = [self.matricula, self.senha, self.nome, self.ficha, self.valorFicha, self.email]
        insert_1_element(vetor, "dbo.Usuario0", self.acesso.connection)


"""
ACESSO = ServerAcess("LAPTOP-4BELV735", "credito_ru")
User(2019070094, 123456, "Leonel", 5.6, ACESSO, "nelsim@gmail.com").signInUser0()

"""
