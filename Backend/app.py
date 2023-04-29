from flask import Flask, jsonify, request
import json
import re

import lib.haveLunch as hv
import lib.tokenBalance as tb
from utils.dbacess import ServerAcess

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def login():
    return jsonify({"teste": "oi"})

@app.route("/havelunch", methods = ["POST"])
def haveLunch():
    try:
        raw_dados  = request.data.decode('utf-8')
        print(raw_dados)
        matricula_regex = r'"Matricula":\s*(\d+)'
        match = re.search(matricula_regex, raw_dados)
        matricula = int(match.group(1))
        print(matricula)
        acesso = ServerAcess("LAPTOP-4BELV735", "credito_ru")
        fichas = tb.GetToken(matricula, acesso ).getToken()
        print(fichas)
        hv.HaveLunch(300000000, fichas,acesso).haveLunch()

    except ValueError:
        print("erro")
    return jsonify({"teste": "executado"})



if __name__ == "__main__":
    app.run(debug=True)


    