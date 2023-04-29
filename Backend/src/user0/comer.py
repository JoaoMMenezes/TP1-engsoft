import lib.haveLunch as hv
import lib.tokenBalance as tb
import re

"""
entrada: {"Matricula": 300000000}

saida:  "ok"

"""
def parseComer(raw_dados):
    matricula_regex = r'"Matricula":\s*(\d+)'
    match = re.search(matricula_regex, raw_dados)
    matricula = int(match.group(1))
    return matricula

def comer(acesso, matricula) -> None:
    fichas = tb.GetToken(matricula, acesso ).getToken()
    hv.HaveLunch(matricula, fichas,acesso).haveLunch()


    
