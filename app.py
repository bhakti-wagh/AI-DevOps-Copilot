from flask import Flask, render_template, request
from agents.api_monitor import check_api
from agents.log_analyzer import analyze_logs
from agents.incident_detector import detect_incident
from agents.ai_suggestions import get_ai_suggestion

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/monitor", methods=["POST"])
def monitor():

    api_url = request.form["api_url"]

    api_result = check_api(api_url)

    log_result = analyze_logs("logs/sample.log")

    incident = detect_incident(log_result["errors"])

    return {
        "status": api_result["status"],
        "response_time": api_result["response_time"],
        "errors": log_result["errors"],
        "warnings": log_result["warnings"],
        "incident": incident
    }

if __name__ == "__main__":
    app.run(debug=True)