from flask import Flask, jsonify, request
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/res", methods=["GET"])
def res():
    if request.method == "GET":
        data = {
            "ponum": 15,
            "lineitem": "keyboard",
        }

        return jsonify(data)


if __name__ == "__main__":
    port = os.environ.get("FLASK_PORT") or 8080
    port = int(port)

    app.run(port=port, host="0.0.0.0")
