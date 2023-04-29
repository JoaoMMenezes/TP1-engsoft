import json
from utils.dbframe import SQL2df
"""
entrada: {"Matricula":300000000 ,"Senha":555467}

saida: {"Tipo":0, "Sucesso":Nome:"vinicius troll", "Fichas":68 }


tipo -> 0 , 1, 2
Sucesso -> 1(sim) ou 0 (Nao)
se usuario for 1 2 o campo fichas recebe -1
"""
def parseLogar(raw_dados):
    dados = json.loads(raw_dados)
    matricula = dados["Matricula"]
    senha = dados["Senha"]
    return matricula, senha

def identificarUser(matricula):
    tipo = 0
    #checar se é inteiro (user 0)
    if isinstance(matricula, int):
        tipo = 0
    elif "1_" in matricula:
        tipo = 1
    else:
        tipo =2
    return tipo

def buscarUser(acesso, tipo, matricula):
    if tipo == 0:
        comando = "select Nome, Fichas from dbo.Usuario0 where Matricula ="+ str(matricula)
        dados = SQL2df(comando, acesso.connection, 0)[0]
        return dados[0], dados[1]
    elif tipo == 1:
        comando = "select Nome from dbo.Usuario1 where Usuario =\'"+ matricula +"\'"
        dados = SQL2df(comando, acesso.connection, 0)[0]
        return dados, -1
    else:
        comando = "select Nome from dbo.Usuario2 where Usuario =\'"+ matricula +"\'"
        dados = SQL2df(comando, acesso.connection, 0)[0]
        return dados, -1
