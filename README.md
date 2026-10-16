# FiscalRecall

Ask questions about a company's annual report (10-K) and get an answer with page citations you can actually check.

> **Status:** work in progress. I'm building this from scratch to properly learn retrieval: the core pieces (search, fusion, evaluation) are written by hand before any framework touches them.

## Why this exists

10-Ks are long. Usually 100+ pages of text, tables and footnotes. Ask a plain LLM something like *"What was 3M's capital expenditure in FY2018?"* and it'll happily give you a confident number. Sometimes the wrong one.

Retrieval fixes part of that by handing the model the real pages first. But finance questions are picky: *FY2018* vs *FY2019* or *operating income* vs *net income* look almost identical to semantic search, and that one detail is the whole answer. So FiscalRecall combines **keyword search (BM25)** for exact terms with **semantic search (embeddings)** for meaning, then checks that every answer is backed by the page it cites.

## How it works (planned)

1. **Parse** each 10-K into text, keeping page numbers
2. **Chunk** the text into searchable pieces
3. **Retrieve** with semantic search, keyword search, and a hybrid of both
4. **Rerank** the top results
5. **Answer** using only the retrieved pages, with page citations, and say "I don't know" when the filing doesn't support an answer
6. **Evaluate** every version on a public benchmark so each change is measured, not guessed

## Evaluation

Everything is tested on the open-source **FinanceBench** set: 150 real questions about public-company filings, each with a correct answer and the evidence page.

I'll report two things for each retrieval approach:

- **Retrieval hit rate**: did the right page show up in the results?
- **Answer accuracy**: was the final answer correct?

| Approach | Retrieval hit rate | Answer accuracy |
|---|---|---|
| Semantic only (baseline) | — | — |
| Keyword (BM25) only | — | — |
| Hybrid | — | — |
| Hybrid + reranking | — | — |

*Numbers get filled in as each stage is built.*

## Roadmap

- [x] Project setup
- [ ] PDF parsing with page numbers
- [ ] Chunking
- [ ] Semantic search baseline + first eval
- [ ] BM25 keyword search
- [ ] Hybrid search
- [ ] Reranking
- [ ] Citation checking + "I don't know" handling
- [ ] API + simple web UI
- [ ] Deployment

## Running it locally

```bash
git clone https://github.com/aayush24rai/fiscal-recall.git
cd fiscal-recall
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# benchmark questions + source filings (kept out of this repo)
git clone https://github.com/patronus-ai/financebench.git data/financebench
```

## Data and credits

- **FinanceBench** by [Patronus AI](https://github.com/patronus-ai/financebench), licensed CC BY-NC 4.0. This project uses its open-source sample for non-commercial evaluation only.
- Source documents are public SEC filings. They're downloaded locally and not committed to this repo.
