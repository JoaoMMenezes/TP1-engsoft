from flask import Flask, jsonify, request
#intaciar banco de dados
from utils.dbacess import ServerAcess
#
from src.user0.comer import comer, parseComer
from src.user0.signin import signIn, parseSignIn
from src.user0.depositoken import deposit, parseDeposit


app = Flask(__name__)

ACESSO = ServerAcess("LAPTOP-4BELV735", "credito_ru")

@app.route("/", methods = ["GET"])
def login():
    return jsonify({"teste": "oi"})

@app.route("/user0/havelunch", methods = ["POST"])
def haveLunch():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula = parseComer(raw_dados)
        comer(ACESSO, matricula)
    except ValueError:
        print("não conseguiu comer")
    return jsonify({"teste": "executado"})

@app.route("/user0/signin", methods = ["POST"])
def rotaSignIn():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula, senha, nome, valorFicha, email = parseSignIn(raw_dados)
        signIn(ACESSO.connection, matricula, senha, nome, valorFicha, email)
    except ValueError:
        print("Nao foi possivel cadastrar o usuario")
    return jsonify({"teste": "Usuário Cadastrado!"})

@app.route("/user0/deposittoken", methods = ["POST"])
def depositToken():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula, amount = parseDeposit(raw_dados)
        deposit(matricula, ACESSO, amount)
    except ValueError:
        print("nao foi possivel depositar")
    return jsonify({"Saldo depositado!"})




if __name__ == "__main__":
    app.run(debug=True)


    