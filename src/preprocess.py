
import pandas as pd

# Load original dataset
df = pd.read_csv("data/raw/aa_dataset-tickets-multi-lang-5-2-50-version.csv")

print("Original dataset:", df.shape)

# Keep all English tickets
df = df[df["language"] == "en"].copy()

# Fill missing subjects
df["subject"] = df["subject"].fillna("")

# Remove records with missing answers
df = df.dropna(subset=["answer"])

# Combine subject and body
df["text"] = df["subject"] + " " + df["body"]

# Keep required columns
df = df[["text", "queue", "type", "priority", "answer"]]

# Remove empty text
df = df[df["text"].str.strip() != ""]

# Save processed dataset
df.to_csv("data/processed/support_tickets.csv", index=False)

print("\nPreprocessing completed!")
print("Final dataset shape:", df.shape)

print("\nCategory distribution:")
print(df["queue"].value_counts())

print("\nTicket type distribution:")
print(df["type"].value_counts())

print("\nPriority distribution:")
print(df["priority"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())
