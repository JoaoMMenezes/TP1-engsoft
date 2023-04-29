import lib.signUser0 as siu
import json

"""
entrada: {"Matricula":2019070094, "Senha":123456, "Nome":"Leonel", "ValorFicha":5.6, "Email":"nelsim@gmail.com"} 

saida:  "Cadastrado!"

"""

def parseSignIn(raw_dados):
    jsonData = json.loads(raw_dados)
    return jsonData["Matricula"], jsonData["Senha"], jsonData["Nome"], jsonData["ValorFicha"], jsonData["Email"]

def signIn(acesso, matricula, senha, nome, valorFicha, email) -> None:
    siu.User(matricula, senha, nome, valorFicha, acesso, email).signInUser0()
