from flask import Flask, jsonify
from project_controller import ProjectController

app = Flask(__name__)


@app.route("/")
def index():
    collections = ProjectController()
    collections.add_project('Margaret', 'O Margaret será desenvolvido para otimizar e auxiliar o processo de seleção e administração de organizações, projetos e inscritos para as futuras edições do Andromedev - evento organizado pela OpenDevUFCG, com o intuito de incentivar a participção de estudantes da Universidade Federal de Campina Grande em projetos open source.',
                            'Uma aplicação de otimização', 'Juan Barros', 'Matheus Alves', 'Web, Data Science')
    project = collections.projects[1]
    print(project)
    return jsonify(project)


if __name__ == "__main__":
    app.run()
