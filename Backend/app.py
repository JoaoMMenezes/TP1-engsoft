from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def login():
    return jsonify({"teste": "oi"})

if __name__ == "__main__":
    app.run(debug=True)