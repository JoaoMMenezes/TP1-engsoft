import json
from utils.dbframe import SQL2df

"""
 entrada: {"Matricula":"300000000", "Senha":"555467"}
{"Matricula":"2_ssss", "Senha":1111}
{"Matricula":"1_alfredo", "Senha":1111}

saida:  {"Tipo":0, "Sucesso":False, "Matricula":300000000,"Nome":"sjhdsah"}

Suecesso False-> ruim  True-> certo

"""
def parseLogar(raw_dados):
    dados = json.loads(raw_dados)
    return dados["Matricula"], dados["Senha"]

def identificarUser(matricula):
    tipo = 0
    if matricula.isdigit():
        tipo = 0
    elif "1_" in matricula:
        tipo =1 
    else:
        tipo =2
    return tipo


def buscarUser(acesso, tipo, matricula):
    if tipo == 0:
        comando = "select Senha, Nome from dbo.Usuario0 where Matricula = " + matricula
        dados = SQL2df(comando, acesso, option = 0)[0]
        #lista esta vazia
        return dados
    elif tipo == 1:
        comando = "select Senha, Nome from dbo.Usuario1 where Usuario = \'" + matricula +"\'"
        dados = SQL2df(comando, acesso, option = 0)[0]
        return dados
    else:
        comando = "select Senha, Nome from dbo.Usuario2 where Usuario = \'" + matricula +"\'"
        dados = SQL2df(comando, acesso, option = 0)[0]
        return dados
    
def conferirSenha(senha_inserida, senha_real):
    if(senha_inserida == str(senha_real)):
        return True
    else:
        return False

