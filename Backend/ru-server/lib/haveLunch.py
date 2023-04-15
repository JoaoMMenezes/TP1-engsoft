import sys
sys.path.insert(0, r'.\TP1-engsoft\Backend\ru-server\utils')
from dbframe import update_1_element
from dbacess import ServerAcess

class HaveLunch():
    def __init__(self, matricula: int, ficha: int, acesso:ServerAcess):
        self.matricula = matricula
        self.acesso = acesso
        self.ficha = ficha

    def haveLunch(self) -> None:
        assert self.ficha > 0 , "No balance for lunch."
        self.ficha -= 1 
        update_1_element("dbo.Usuario0", self.acesso.connection, "Fichas", str(self.ficha), "Matricula", str(self.matricula))
