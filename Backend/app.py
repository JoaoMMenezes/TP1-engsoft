from flask import Flask, jsonify, request
#intaciar banco de dados
from utils.dbacess import ServerAcess
#
from src.user0.comer import comer, parseComer
from src.Login.logar import parseLogar, identificarUser, buscarUser, conferirSenha


app = Flask(__name__)

ACESSO = ServerAcess("LAPTOP-4BELV735", "credito_ru")

@app.route("/", methods = ["GET"])
def Home():
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



if __name__ == "__main__":
    app.run(debug=True)


    