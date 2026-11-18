
# SupportPilot – AI-Powered IT Support Ticket Resolution Agent

## 1. Project Overview

SupportPilot is an AI-powered IT support ticket management system that automates ticket classification, priority prediction, severity assessment, knowledge retrieval, and resolution generation.

It helps employees receive faster troubleshooting suggestions while allowing unresolved or uncertain tickets to be escalated to human IT support.

## 2. Objectives

- Automate IT support ticket classification.
- Predict ticket type and priority using Machine Learning.
- Assess ticket severity.
- Retrieve relevant solutions from a knowledge base.
- Generate structured support responses.
- Validate resolutions through employee feedback.
- Escalate unresolved tickets to human support.
- Store and monitor tickets through an admin dashboard.

## 3. System Architecture

Employee submits ticket
        |
        v
    Ticket Intake
        |
        v
  AI Ticket Classification
        |
        v
 Priority and Severity Assessment
        |
        v
  Knowledge Retrieval
        |
        v
 Resolution Generation
        |
        v
 Employee Feedback
       / \
      /   \
    Yes    No
     |      |
     v      v
 Resolved  Escalated
     \      /
      \    /
       v  v
   SQLite Database
        |
        v
   Admin Dashboard

## 4. Key Features

- Ticket submission through a web interface.
- ML-based category, type, and priority prediction.
- Rule-based severity assessment.
- TF-IDF-based knowledge retrieval.
- Template-based resolution response generation.
- Employee feedback and ticket status updates.
- Human review flag for low-confidence category predictions.
- SQLite ticket storage.
- Admin dashboard displaying all tickets.

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Pandas | Data preprocessing |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction and retrieval |
| Logistic Regression | Ticket classification |
| Flask | Web application |
| SQLite | Database |
| HTML | Frontend |

## 6. Dataset

Dataset: Customer IT Support – Multilingual Ticket Dataset

Source: https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets

- Original records: 28,587
- English records retained: 16,335
- Features used: Ticket text, queue, type, priority, and answer.
- Missing subject values were handled during preprocessing.
- Records without answers were removed.

## 7. Machine Learning Models

Three Logistic Regression models were trained:

1. Ticket Category Prediction
2. Ticket Type Prediction
3. Ticket Priority Prediction

### Baseline Evaluation Results

| Model | Accuracy |
|---|---:|
| Category Classification | 49.92% |
| Ticket Type Prediction | 84.48% |
| Priority Prediction | 60.09% |

Low-confidence category predictions are flagged for human decision.

Severity assessment currently uses rule-based logic because the dataset does not contain severity labels.

## 8. Project Structure

```text
SupportPilot/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── queue_model.pkl
│   ├── type_model.pkl
│   └── priority_model.pkl
│
├── notebooks/
│
├── src/
│   ├── app.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── predict.py
│   ├── severity.py
│   ├── knowledge_retrieval.py
│   ├── resolution_generator.py
│   ├── resolution_validation.py
│   └── database.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── status.html
│   └── dashboard.html
│
├── static/
├── requirements.txt
├── .gitignore
└── README.md
```

## 9. Installation and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/Rampilla-Deepthi/nfosys-_AI-Powered-Customer-Support-Platform-with-Ticket-Resolution-Agent.git
```

### Step 2: Open the project folder

```bash
cd nfosys-_AI-Powered-Customer-Support-Platform-with-Ticket-Resolution-Agent
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python src/app.py
```

### Step 5: Open in browser

http://127.0.0.1:5000

## 10. Application Workflow

1. Employee submits an IT support ticket.
2. The ML models predict ticket category, type, and priority.
3. The severity module assesses ticket severity.
4. The knowledge retrieval module searches for a relevant solution.
5. A structured support response is generated.
6. Employee confirms whether the solution worked.
7. The ticket is marked Resolved or Escalated.
8. Ticket information is stored in SQLite.
9. The admin dashboard displays submitted tickets and their statuses.

## 11. Future Enhancements

- Improve ticket classification accuracy.
- Integrate a generative AI model for dynamic resolution generation.
- Add authentication for employees and administrators.
- Improve dashboard analytics and visualizations.
- Add email notifications for escalated tickets.
- Introduce a larger IT-specific knowledge base.

## 12. Project Status

Core ticket processing, ML predictions, Flask integration, resolution feedback, SQLite storage, and the admin dashboard have been implemented.
