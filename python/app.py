from flask import Flask, jsonify
from python.models.project import Project

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    proj = Project("Margaret", "sistem andromedev",
                   "projeto opensource", 1, "juan", "renan", ["back", "front"])
    return jsonify(proj.__dict__), 200


if __name__ == "__main__":
    app.run()
