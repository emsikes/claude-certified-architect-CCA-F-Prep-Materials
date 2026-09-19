# Graders

Three general types: **code**, **model**, and **human**.

---

## 1. Code graders

Programmatically evaluate the result.

**Useful for:**

- Checking output length
- Verifying output does / doesn't contain certain words
- Syntax validation
- Readability scores

## 2. Model graders

Ask a model to assign a score to the output, or compare two versions.

**Useful for:**

- Response quality
- Quality of instruction following
- Completeness
- Helpfulness
- Safety

## 3. Human graders

Ask a human to assign a score to the output, or compare two versions.

**Useful for:**

- General response quality
- Comprehensiveness
- Depth
- Conciseness
- Relevance

---

## Evaluation criteria

### Format

- Should return only JSON, Python, Regex, etc.
- Should not include any additional explanation

### Valid syntax

- Produced JSON, Python, Regex, etc. should have valid syntax

### Task following

- Response should directly and clearly address the user's task
- Generated code should be accurate