# Task 9 - Robot Access with LangGraph + Prolog

This project replicates the LangGraph symbolic logic pipeline from Aiea-Auditor, using a new knowledge base about robot access in a smart facility.

---

## 🧠 Knowledge Base

Stored in `rules.pl`, this Prolog file defines robot permissions for entering certain zones. It includes restricted zones and access rules.

---

## 📁 Files

| File              | Description                                  |
|-------------------|----------------------------------------------|
| `main.py`         | Runs the LangGraph pipeline                  |
| `graphchain.py`   | LangGraph edge and state logic               |
| `functions.py`    | Nodes for Prolog querying and LLM reasoning  |
| `rules.pl`        | Prolog knowledge base                        |
| `examples.json`   | Sample queries to test your agent            |

---

## ✅ Run an Example

```bash
python main.py

Or interactively:
query = input("Enter a Prolog query: ")

Sample input (from exmaples.json):
{
  "query": "can_access(iris, storage)",
  "expected": "true"
}

