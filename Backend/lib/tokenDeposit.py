from utils.dbframe import update_1_element

class DepositToken():
    def __init__(self, matricula: int, ficha: int, acesso):
        self.matricula = matricula
        self.acesso = acesso
        self.ficha = ficha

    def depositToken(self, amount: int) -> None:
        assert amount > 0 , "Deposit token ficha should be greater than zero."
        self.ficha += amount
        assert self.ficha >= amount,  "Overflow occurred."
        update_1_element("dbo.Usuario0", self.acesso.connection, "Fichas", str(self.ficha), "Matricula", str(self.matricula))
