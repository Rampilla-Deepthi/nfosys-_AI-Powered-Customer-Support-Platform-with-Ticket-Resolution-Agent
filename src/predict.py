
import joblib
from severity import assess_severity
from knowledge_retrieval import retrieve_solution
from resolution_validation import validate_resolution
from resolution_generator import generate_resolution

# Load trained models
queue_model = joblib.load("models/queue_model.pkl")
type_model = joblib.load("models/type_model.pkl")
priority_model = joblib.load("models/priority_model.pkl")

print("================================")
print("       SUPPORTPILOT AI")
print("================================")

# Get ticket from user
subject = input("Enter ticket subject: ")
body = input("Describe your problem: ")

ticket = subject + " " + body

# Predict ticket category
probabilities = queue_model.predict_proba([ticket])[0]
categories = queue_model.classes_

best_index = probabilities.argmax()
best_category = categories[best_index]
confidence = probabilities[best_index]

# Check category confidence
if confidence < 0.50:
    category = "Uncertain - Human Review Required"
else:
    category = best_category

# Display top 3 category predictions
top_indices = probabilities.argsort()[-3:][::-1]

# Predict ticket type and priority
ticket_type = type_model.predict([ticket])[0]
priority = priority_model.predict([ticket])[0]

# Assess ticket severity
severity = assess_severity(subject, body, priority)

# Retrieve relevant solution
solution = retrieve_solution(ticket)
generated_response = generate_resolution(ticket, solution, severity)

# Display final analysis
print("\n========== AI ANALYSIS ==========")

print("Ticket Category:", category)

print("\nTop 3 Category Predictions:")
for i in top_indices:
    print(categories[i], ":", round(probabilities[i] * 100, 2), "%")

print("\nTicket Type:", ticket_type)
print("Priority:", priority)
print("Severity:", severity)
print("\nSuggested Resolution:")
print(generated_response)
# Validate resolution
status = validate_resolution(solution)

print("\nFinal Ticket Status:", status)
print("================================")

