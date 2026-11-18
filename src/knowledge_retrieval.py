
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge base
df = pd.read_csv("data/processed/knowledge_base.csv")

# Convert problems into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(df["problem"])


def retrieve_solution(ticket):

    ticket_vector = vectorizer.transform([ticket])

    scores = cosine_similarity(ticket_vector, vectors)[0]

    best_index = scores.argmax()
    best_score = scores[best_index]

    if best_score < 0.10:
        return "No matching solution found. Escalate to human support."

    return df.iloc[best_index]["solution"]
