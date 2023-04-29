from flask import Flask, jsonify, request
#intaciar banco de dados
from utils.dbacess import ServerAcess
#
from src.user0.comer import comer, parseComer

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



if __name__ == "__main__":
    app.run(debug=True)


    