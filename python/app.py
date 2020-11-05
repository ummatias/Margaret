from flask import Flask
from python.models.subscribed import Subscribed
from python.models.user import User
from python.models.project import Project
from python.controllers.project_controller import ProjectController

app = Flask(__name__)

@app.route('/', methods=['GET'])


def index():
    return 'rotas:   /subscribed   -   /project   -   /subs - /projectcontroller'

@app.route('/subscribed', methods=['GET'])
def subscriber():
    subscribed = Subscribed('All Might', 'arumaito.smash@ccc.ufcg.edu.br', 'Arumaito#4586', '2002.1', '')
    return subscribed.__dict__


@app.route("/project", methods=["GET"])
def project():
    proj = Project('Margaret', 'sistem andromedev', 'projeto opensource', 'back'"aaa","aaa")
    return proj.__dict__


@app.route("/subs", methods=["GET"])
def user():
    sub = User("Caio","caio.caio@ccc.ufcg.edu.br","caio#1313")
    return sub.__dict__

@app.route("/projectcontroller", methods=["GET"])
def show_projects():
    collections = ProjectController()
    collections.add_project('Margaret', 'O Margaret será desenvolvido para otimizar e auxiliar o processo de seleção e administração de organizações, projetos e inscritos para as futuras edições do Andromedev - evento organizado pela OpenDevUFCG, com o intuito de incentivar a participção de estudantes da Universidade Federal de Campina Grande em projetos open source.',
                            'Uma aplicação de otimização', 'Juan Barros', 'Matheus Alves', 'Web, Data Science')
    project = collections.projects[1]
    return project.__dict__

  
if __name__ == "__main__":
    app.run()
