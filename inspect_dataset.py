
import pandas as pd
import glob
import os

# Find CSV file
files = glob.glob("data/raw/*.csv")

if not files:
    print("No CSV file found!")
else:
    file = files[0]
    print("Dataset:", os.path.basename(file))

    # Load dataset
    try:
        df = pd.read_csv(file, encoding="utf-8", low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(file, encoding="latin-1", low_memory=False)

    # Dataset information
    print("\n1. DATASET SHAPE")
    print(df.shape)

    print("\n2. COLUMN NAMES")
    print(df.columns.tolist())

    print("\n3. FIRST 5 RECORDS")
    print(df.head())

    print("\n4. MISSING VALUES")
    print(df.isnull().sum())

    print("\n5. DATA TYPES")
    print(df.dtypes)

    print("\n6. DUPLICATE RECORDS")
    print(df.duplicated().sum())

print("\n7. QUEUE DISTRIBUTION")
print(df['queue'].value_counts())

print("\n8. PRIORITY DISTRIBUTION")
print(df['priority'].value_counts())

print("\n9. TICKET TYPE DISTRIBUTION")
print(df['type'].value_counts())

print("\n10. LANGUAGE DISTRIBUTION")
print(df['language'].value_counts())

print("\n11. ENGLISH IT SUPPORT TICKETS")
it_df = df[
    (df['language'].str.lower() == 'en') &
    (df['queue'].str.contains('IT Support', case=False, na=False))
]

print("Number of English IT Support tickets:", len(it_df))

print("\n12. SAMPLE IT SUPPORT TICKETS")
print(it_df[['subject', 'body', 'queue', 'priority']].head(10).to_string(index=False))

print("\n13. IT SUPPORT PRIORITY DISTRIBUTION")
print(it_df['priority'].value_counts())

print("\n14. IT SUPPORT TYPE DISTRIBUTION")
print(it_df['type'].value_counts())

print("\n15. SUBJECT MISSING IN IT SUPPORT")
print(it_df['subject'].isnull().sum())

print("\n16. IT SUPPORT SAMPLE ANSWERS")
print(it_df[['body', 'answer']].head(3).to_string(index=False))

print("\n17. QUEUE AND PRIORITY")
print(pd.crosstab(it_df['queue'], it_df['priority']))
