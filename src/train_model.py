
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load processed dataset
df = pd.read_csv("data/processed/support_tickets.csv")

# Create models folder if it does not exist
os.makedirs("models", exist_ok=True)

# Define prediction targets
targets = ["queue", "type", "priority"]

for target in targets:

    print("\n===================================")
    print("Training model for:", target)
    print("===================================")

    # Input and output
    X = df["text"]
    y = df[target]

    # Split dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Create TF-IDF and Logistic Regression pipeline
    model = Pipeline([
        ("tfidf", TfidfVectorizer(
            stop_words="english",
            max_features=10000,
            ngram_range=(1, 2)
        )),
        ("classifier", LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        ))
    ])

    # Train model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate model
    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", round(accuracy * 100, 2), "%")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    # Save trained model
    joblib.dump(model, "models/" + target + "_model.pkl")

    print("Model saved successfully!")

print("\nAll three models trained successfully!")
