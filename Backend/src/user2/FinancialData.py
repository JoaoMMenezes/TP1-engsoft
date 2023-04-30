import lib.getFinance as tb
import json
"""
entrada: {"DataInicio": "2023-04-14", "DataFinal": "2023-04-30"}

saida:  "ok"

"""
def parseFinance(raw_dados):
    dados = json.loads(raw_dados)
    return [dados["DataInicio"], dados["DataFinal"]]

def financial(data_begin, data_end, acesso, option = 1) -> None:
    return tb.GetFinance(data_begin, data_end, acesso, option = 1 ).getFinance()