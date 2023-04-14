import sys
sys.path.insert(0, r'.\TP1-engsoft\Backend\ru-server\utils')
from dbframe import connect

class ServerAcess():
    def __init__(self, servidor:str, banco_de_dados:str):
        self.servidor = servidor
        self.banco_de_dados = banco_de_dados
        self.connection = connect(self.servidor, self.banco_de_dados)