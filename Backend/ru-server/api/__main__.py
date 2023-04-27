from flask import jsonify
from api import create_app

app = create_app()

@app.route("/", methods = ["GET"])
def landing():
    return jsonify("Olá!")

if __name__ == "__main__":
    app.run(host = "127.0.0.1")