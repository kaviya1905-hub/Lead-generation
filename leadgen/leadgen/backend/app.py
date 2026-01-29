from flask import Flask, request, render_template, redirect, url_for, session
from tasks import generate_questions_async
from models import get_companies
from llm import generate_icp_questions

app = Flask(
    __name__,
    template_folder="templates",   # Flask will load HTML from /app/templates inside container
    static_folder="static"         # For CSS/JS from /app/static
)

app.secret_key = "supersecretkey123"


# -------------------- Home Page -------------------- #
@app.route("/")
def home():
    return render_template("index.html")


# -------------------- Generate Questions -------------------- #
@app.route("/generate_questions", methods=["POST"])
def generate_questions_route():
    persona = request.form.get("persona").strip()
    industry = request.form.get("industry").strip()

    task = generate_questions_async.delay(persona, industry)
    return redirect(url_for("check_task", task_id=task.id, persona=persona, industry=industry))


# -------------------- Check Celery Task -------------------- #
@app.route("/check_task/<task_id>")
def check_task(task_id):
    task = generate_questions_async.AsyncResult(task_id)

    if task.state == "PENDING":
        return render_template("loading.html", task_id=task_id)

    if task.state == "SUCCESS":
        persona = request.args.get("persona")
        industry = request.args.get("industry")

        return render_template(
            "questions.html",
            questions=task.get(),
            persona=persona,
            industry=industry
        )

    return "Task Failed, check celery logs"


# -------------------- Submit Answers -------------------- #
@app.route("/submit_answers", methods=["POST"])
def submit_answers():
    persona = request.form.get("persona")
    industry = request.form.get("industry")

    print("\n===========================")
    print("🔍 Persona Received:", persona)
    print("🔍 Industry Received:", industry)

    companies = get_companies(persona, industry)
    print("📌 Companies Found:", companies)
    print("===========================\n")

    return render_template("results.html", companies=companies)


# -------------------- Run Server -------------------- #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
