from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Grubisno Polje, Croatia",
        "salary": "$70,000",
    },
    {
        "id": 2,
        "title": "Data Engeneer",
        "location": "Zagreb, Croatia",
        "salary": "$30,000",
    },
    {
        "id": 3,
        "title": "Database administrator",
        "location": "Osijek, Croatia",
        "salary": "$100,000",
    },
    {
        "id": 4,
        "title": "Frontend Developer",
        "location": "Vinkovci, Croatia",
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Jobly")


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
