import pandas as pd

pd.set_option("display.max_columns", None)

QUESTIONS_PATH = "data/financebench/data/financebench_open_source.jsonl"
DOCS_PATH = "data/financebench/data/financebench_document_information.jsonl"

questions = pd.read_json(QUESTIONS_PATH, lines=True)
docs = pd.read_json(DOCS_PATH, lines=True)

docs = docs.drop(columns=["company"])

df = pd.merge(questions, docs, on="doc_name")

print(f"Questions after merge: {len(df)}")
print(f"Unique documents: {df['doc_name'].nunique()}")

print("\nQuestions by type:")
print(df["question_type"].value_counts())

print("\nTop 10 companies by number of questions:")
print(df["company"].value_counts().head(10))

print(f"\nRows in the documents file: {len(docs)}")
print("Documents by type:")
print(docs["doc_type"].value_counts())

print("\nData quality checks:")
print(f"Unique doc names in documents file: {docs['doc_name'].nunique()}")
print(docs[docs["doc_name"].duplicated(keep=False)])
print(f"Questions using the duplicated Foot Locker doc: {(df['doc_name'] == 'FOOTLOCKER_2023_annualreport').sum()}")

samples = df.sample(3, random_state=42)

for _, row in samples.iterrows():
    print("\n" + "=" * 60)
    print(f"Company:  {row['company']}  ({row['doc_name']})")
    print(f"Type:     {row['question_type']}")
    print(f"Question: {row['question']}")
    print(f"Answer:   {row['answer']}")
    print(f"Evidence pieces: {len(row['evidence'])}")

    first = row["evidence"][0]
    page = first["evidence_page_num"]
    print(f"Page in your PDF viewer: {page + 1}")
    print(f"Evidence: {first['evidence_text'][:300]}")
