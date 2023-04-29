from flask import Flask, jsonify, request
#intaciar banco de dados
from utils.dbacess import ServerAcess
#
from src.user0.comer import comer, parseComer
from src.user1.signin import signIn, parseSignIn
from src.user1.depositoken import deposit, parseDeposit


from src.Login.logar import parseLogar, identificarUser, buscarUser, conferirSenha


app = Flask(__name__)

ACESSO = ServerAcess("LAPTOP-4BELV735", "credito_ru")

@app.route("/", methods = ["GET"])
def HelloPage():
    return jsonify({"teste": "oi"})

@app.route("/login", methods = ["POST"])
def login():
    #definir para não entrar como default
    sucesso = 0
    #pegar o post
    raw_dados  = request.data.decode('utf-8')
    #pegar os dados do db
    try:
        matricula, senhaInserida = parseLogar(raw_dados)
    except:
        return jsonify({"Tipo":0, "Sucesso":sucesso, "Nome":"nada"})
    
    tipo = identificarUser(matricula)

    try:
        senhaReal, nome = buscarUser(ACESSO.connection, tipo, matricula)
    except:
        return jsonify({"Tipo":tipo, "Sucesso":sucesso, "Nome":"nada"})
    sucesso = conferirSenha(senhaInserida, senhaReal)
    
    return jsonify({"Tipo":tipo, "Sucesso":sucesso, "Nome":nome})

@app.route("/user0/havelunch", methods = ["POST"])
def haveLunch():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula = parseComer(raw_dados)
        comer(ACESSO, matricula)
    except ValueError:
        print("não conseguiu comer")
    return jsonify({"teste": "executado"})

@app.route("/user1/signin", methods = ["POST"])
def rotaSignIn():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula, senha, nome, valorFicha, email = parseSignIn(raw_dados)
        signIn(ACESSO, matricula, senha, nome, valorFicha, email)
    except ValueError:
        print("Nao foi possivel cadastrar o usuario")
    return jsonify({"teste": "Usuário Cadastrado!"})

@app.route("/user1/deposittoken", methods = ["POST"])
def depositToken():
    try:
        raw_dados  = request.data.decode('utf-8')
        matricula, amount = parseDeposit(raw_dados)
        deposit(matricula, ACESSO, amount)
    except ValueError:
        print("nao foi possivel depositar")
    return jsonify({"Mensagem":"Saldo depositado!"})




if __name__ == "__main__":
    app.run(debug=True)


    