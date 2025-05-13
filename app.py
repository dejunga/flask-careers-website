from flask import Flask, jsonify, render_template
from config import DevelopmentConfig
from models import db, Job

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db.init_app(app)

# Create tables on first run
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_jobs = Job.query.all()
    return render_template(
        "home.html",
        jobs=[job.to_dict() for job in all_jobs],
        company_name="Jobly",
    )


@app.route("/api/jobs")
def list_jobs():
    return jsonify([j.to_dict() for j in Job.query.all()])


if __name__ == "__main__":
    app.run(debug=True)
