import lib.getFinance as tb
import json
"""
entrada: {"DataInicio":"14-04-2023","DataFinal":"30-04-2023"}

saida:  "ok"

"""
def parseFinance(raw_dados):
    dados = json.loads(raw_dados)
    return dados["DataInicio"], dados["DataFinal"]

def financial(data_begin, data_end, acesso, option = 1):
    return tb.GetFinance(data_begin, data_end, acesso, option = option ).getFinance()


