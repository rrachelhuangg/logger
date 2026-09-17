from datetime import date

from flask import Blueprint, jsonify, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html", today=date.today())

@bp.route("/api/health")
def health():
    return jsonify(status="ok", date=date.today().isoformat())


@bp.app_errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404
