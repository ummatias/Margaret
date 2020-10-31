from flask import Flask, jsonify
from python.models.user import User
from python.models.project import Project

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    proj = Project("Margaret", "sistem andromedev", "projeto opensource", "back","aaa","aaa")
    return jsonify(proj.__dict__)

@app.route("/subs", methods=["GET"])
def test():
    sub = User("Caio","caio.caio@ccc.ufcg.edu.br","caio#1313")
    return jsonify(sub.__dict__)

if __name__ == "__main__":
    app.run()