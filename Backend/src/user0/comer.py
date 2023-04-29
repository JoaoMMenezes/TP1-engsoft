import lib.haveLunch as hv
import lib.tokenBalance as tb
import json
"""
entrada: {"Matricula":3019070094}

saida:  "ok"

"""
"""def parselogar(raw_dados):
    dados = json.loads(raw_dados)
    senha = dados["Senha"]
    matricula = dados["Matricula"]
    return matricula, senha"""
def parseComer(raw_dados):
    dados = json.loads(raw_dados)
    return dados["Matricula"]

def comer(acesso, matricula) -> None:
    fichas = tb.GetToken(matricula, acesso ).getToken()
    hv.HaveLunch(matricula, fichas,acesso).haveLunch()


    
