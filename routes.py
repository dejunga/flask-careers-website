from flask import Blueprint, render_template, jsonify
from .models import Job

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    jobs = Job.query.all()
    return render_template("home.html", jobs=[j.to_dict() for j in jobs])


@main_bp.route("/api/jobs")
def list_jobs():
    return jsonify([j.to_dict() for j in Job.query.all()])
