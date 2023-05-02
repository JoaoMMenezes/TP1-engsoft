
import lib.tokenBalance as tb
import json
"""
entrada: {"Matricula":"300000000"}

saida:  {"Saldo":8}

"""
def parseBalance(raw_dados):
    dados = json.loads(raw_dados)
    return dados["Matricula"]

def balance(acesso, matricula) -> None:
    return tb.GetToken(matricula, acesso ).getToken()

