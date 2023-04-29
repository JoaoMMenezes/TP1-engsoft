from utils.dbframe import connect

class ServerAcess():
    def __init__(self, servidor:str, banco_de_dados:str):
        self.servidor = servidor
        self.banco_de_dados = banco_de_dados
        self.connection = connect(self.servidor, self.banco_de_dados)