from flask import Flask, jsonify
from models.organization import Organization

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    return "Hello world!"


@app.route("/juan", methods=["GET"])
def juan():
    org = Organization("Juan", "", "", "", "")

    return jsonify(org.__dict__)


if __name__ == "__main__":
    app.run()
