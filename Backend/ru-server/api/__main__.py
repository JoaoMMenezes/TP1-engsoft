from flask import jsonify, request, Response
from api import create_app

app = create_app()

@app.route("/", methods = ["GET"])
def landing():
    return jsonify("Olá!")

@app.route("/login", methods = ["POST"])
def login():
    data = request.data
    print(data)
    return  Response(status=204)
    #return jsonify(data)

if __name__ == "__main__":
    app.run(host = "127.0.0.1")