from flask import Blueprint

bp = Blueprint("version", __name__)


def init_app(app):
    app.register_blueprint(bp)


@bp.route("/version", methods=["GET"])
def version():
    return "v1"
