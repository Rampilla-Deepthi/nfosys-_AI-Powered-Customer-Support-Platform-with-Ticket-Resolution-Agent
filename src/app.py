
from flask import Flask, render_template, request
import joblib

from severity import assess_severity
from knowledge_retrieval import retrieve_solution
from resolution_generator import generate_resolution

from database import create_table, save_ticket, update_ticket_status, get_all_tickets

app = Flask(__name__, template_folder="../templates")

# Create database table
create_table()

# Load trained models
queue_model = joblib.load("models/queue_model.pkl")
type_model = joblib.load("models/type_model.pkl")
priority_model = joblib.load("models/priority_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit_ticket():

    subject = request.form["subject"]
    body = request.form["body"]

    ticket = subject + " " + body

    # Predict category
    probabilities = queue_model.predict_proba([ticket])[0]
    categories = queue_model.classes_

    best_index = probabilities.argmax()
    confidence = probabilities[best_index]

    if confidence < 0.50:
        category = categories[best_index] + " (Human Decision Needed)"
    else:
        category = categories[best_index]

    # Predict ticket type and priority
    ticket_type = type_model.predict([ticket])[0]
    priority = priority_model.predict([ticket])[0]

    # Assess severity
    severity = assess_severity(subject, body, priority)

    # Retrieve and generate resolution
    solution = retrieve_solution(ticket)
    response = generate_resolution(ticket, solution, severity)

    # Save ticket in database
    ticket_id = save_ticket(
        subject, body, category, ticket_type,
        priority, severity, response
    )

    return render_template(
        "result.html",
        category=category,
        ticket_type=ticket_type,
        priority=priority,
        severity=severity,
        response=response,
        ticket_id=ticket_id
    )


@app.route("/feedback", methods=["POST"])
def feedback():

    response = request.form["response"]
    ticket_id = request.form["ticket_id"]

    if response == "yes":
        status = "Resolved"
        message = "Ticket successfully resolved and closed!"
    else:
        status = "Escalated"
        message = "Ticket escalated to human IT support team!"

    # Update database
    update_ticket_status(ticket_id, status)

    tickets = get_all_tickets()

    return render_template(
        "status.html",
        status=status,
        message=message,
        tickets=tickets
    )
@app.route("/dashboard")
def dashboard():

    tickets = get_all_tickets()

    return render_template("dashboard.html", tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
