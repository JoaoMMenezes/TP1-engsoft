import lib.tokenDeposit as td
import lib.tokenBalance as tb
import json
"""
entrada: {"Matricula":3019070094,"Amount":50}

saida:  "Depósito com sucesso!"

"""
def parseDeposit(raw_dados):
    jsonData = json.loads(raw_dados)
    return jsonData["Matricula"], jsonData["Amount"]

def deposit(matricula, acesso, amount) -> None:
    ficha = tb.GetToken(matricula, acesso).getToken()
    td.DepositToken(matricula, ficha, acesso).depositToken(amount)


    
