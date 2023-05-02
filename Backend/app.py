from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
#intaciar banco de dados
from utils.dbacess import ServerAcess
#
from src.Login.logar import parseLogar, identificarUser, buscarUser, conferirSenha

from src.user0.comer import comer, parseComer
from src.user0.getbalance import balance, parseBalance

from src.user1.signin import signIn, parseSignIn
from src.user1.depositoken import deposit, parseDeposit
from src.user2.FinancialData import parseFinance, financial


app = Flask(__name__)
CORS(app)

ACESSO = ServerAcess("LAPTOP-4BELV735", "credito_ru")

################################################################################################
@app.route("/", methods = ["GET"])
def HelloPage():
    return jsonify({"teste": "oi"})

################################################################################################
#passar matricula
@app.route("/login", methods = ["POST"])
def login():
    #definir para não entrar como default
    #pegar o post
    raw_dados  = request.data.decode('utf-8')
    #pegar os dados do db
    try:
        matricula, senhaInserida = parseLogar(raw_dados)
    except:
        return jsonify({"tipo":0, "sucesso":False, "matricula":matricula,"nome":"nada"})
    
    tipo = identificarUser(matricula)

    try:
        senhaReal, nome = buscarUser(ACESSO.connection, tipo, matricula)
    except:
        return jsonify({"tipo":tipo, "sucesso":False, "matricula":matricula,"nome":"nada"})
    sucesso = conferirSenha(senhaInserida, senhaReal)
    
    return jsonify({"tipo":tipo, "sucesso":sucesso, "matricula":matricula, "nome":nome})

################################################################################################
@app.route("/user0/havelunch", methods = ["POST"])
def haveLunch():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula = parseComer(raw_dados)
        comer(ACESSO, matricula)
    except ValueError:
        return jsonify({"mensagem":False})
    return jsonify({"mensagem": True})

################################################################################################
@app.route("/user0/getbalance", methods = ["POST"])
def getBalance():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula = parseBalance(raw_dados)
        saldo = balance(ACESSO, matricula)
    except ValueError:
       return jsonify({"saldo": -1})
    return jsonify({"saldo": saldo})

################################################################################################
@app.route("/user1/signin", methods = ["POST"])
def rotaSignIn():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula, senha, nome, valorFicha, email = parseSignIn(raw_dados)
        print("/n/n")
        print(matricula)
        signIn(ACESSO, matricula, senha, nome, valorFicha, email)
    except ValueError:
        return jsonify({"mensagem":False})
    return jsonify({"mensagem": True})

################################################################################################
@app.route("/user1/deposittoken", methods = ["POST"])
def depositToken():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula, amount = parseDeposit(raw_dados)
        deposit(matricula, ACESSO, amount)
    except ValueError:
        return jsonify({"mensagem":False})
    return jsonify({"mensagem":True})
################################################################################################
@app.route("/user2/getfinance", methods = ["POST"])
def getFinancial():
    try:
        raw_dados  = request.data.decode('utf-8')
        data_inicio, data_final = parseFinance(raw_dados)
        arquivo = financial(data_inicio, data_final, ACESSO.connection, option = 1)
    except ValueError:
        return jsonify({"mensagem":"grafico não foi criado"})
    #return render_template("finance.html")
    return jsonify({"mensagem": "foi"})


if __name__ == "__main__":
    app.run(debug=True)


    