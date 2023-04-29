from utils.dbframe import update_1_element, insert_1_element
from datetime import datetime

class HaveLunch():
    def __init__(self, matricula: int, ficha: int, acesso):
        self.matricula = matricula
        self.acesso = acesso
        self.ficha = ficha

    def insertClient(self) -> None:
        dia_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        vetor = [self.matricula, dia_atual]
        insert_1_element(vetor, "dbo.Clientes", self.acesso.connection)
        print(vetor)

    def haveLunch(self) -> None:
        assert self.ficha > 0 , "No balance for lunch."
        self.ficha -= 1 
        update_1_element("dbo.Usuario0", self.acesso.connection, "Fichas", str(self.ficha), "Matricula", str(self.matricula))
        self.insertClient()



"""tes = ServerAcess("LAPTOP-4BELV735", "credito_ru")
pegar = tb.GetToken(300000000, tes)
comer = HaveLunch(300000000, pegar.getToken(),tes )
comer.haveLunch()"""