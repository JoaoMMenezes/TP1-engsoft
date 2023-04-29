from flask import jsonify, request, Response
from backend import create_app
import json
#import rotaHaveLunch as rhv

app = create_app()

@app.route("/", methods = ["GET"])
def landing():
    return jsonify("Olá!")

@app.route("/havelunch", methods = ["POST"])
def havelunch():
    data = request.data.decode('utf-8')
    dados = json.loads(data)
    matricula = str(dados["Matricula"])
    print(matricula)
    #rhv.rotaHaveLunch(matricula)
    #return  Response(status=204)
    return json.loads(matricula )

if __name__ == "__main__":
    app.run(host = "127.0.0.1")