from flask import Flask, jsonify, request
from python.models.project import Project

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get():
    proj = Project("Margaret", "sistem andromedev",
                   "projeto opensource", 1, "juan", "renan", ["back", "front"])
    return jsonify(proj.__dict__), 200


@app.route("/", methods=["POST"])
def post():
    data = request.get_json()

    return {"name": data["nome"]}, 200


@app.route("/", methods=["PUT"])
def put():
    data = request.get_json()

    return {"name": data["nome"]+"a"}


if __name__ == "__main__":
    app.run()
