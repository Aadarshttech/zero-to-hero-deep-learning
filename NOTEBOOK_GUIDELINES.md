# 📐 Notebook Guidelines — Zero to Hero AI Engineer

> **This file defines the standard for every module notebook in this learning path.**  
> Before writing any notebook, read this file. Every rule here is mandatory.

---

## 🧭 Philosophy

> **"Understand it like you're explaining to a friend, then show it in code."**

Every notebook must follow this order of priority:

1. **Clarity first** — explain in plain, simple English
2. **Context always** — use real-life analogies and examples
3. **Code second** — only after the concept is fully explained
4. **Never skip notes** — every section, every concept, every component *must* have notes

---

## 📋 Mandatory Notebook Structure

Every `.ipynb` notebook **must** follow this exact structure, in this exact order:

```
1. Title Cell (Markdown)
2. Chapter Overview (Markdown)
3. Table of Contents (Markdown)
4. ─── For each Topic/Section ───
   a. Section Header (Markdown)
   b. Simple English Definition (Markdown)  ← MANDATORY
   c. Real-Life Analogy (Markdown)           ← MANDATORY
   d. Deep-Dive Notes (Markdown)             ← MANDATORY
   e. Key Concepts Table (Markdown)          ← MANDATORY
   f. Code Cell (if applicable)              ← optional, but must follow notes
5. Chapter Summary Table (Markdown)
6. Resources & Further Reading (Markdown)
7. Next Module Preview (Markdown)
```

---

## ✅ Rule 1 — Title Cell (Mandatory)

Every notebook must start with a title cell containing:

```markdown
# 📘 Module XX — [Module Name]
## Chapter X.Y — [Chapter Name]

> **Learning Path:** Zero to Hero — AI Engineer
> **Module:** XX of 18
> **Source:** [roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer)
> **Topics:** [Topic 1], [Topic 2], [Topic 3]...
> **Format:** Notes first → Code second

---
```

### ⚠️ Strict Numbering Rule — Never Use Leading Zeros With Decimals
- When a chapter has a sub-number / decimal point (`.`), **NEVER** include a leading zero before the point.
  - ✅ **Correct:** `Chapter 2.1`, `Chapter 2.2`, `Chapter 3.1`, `Chapter 4.1`, `Chapter 4.2`, `Chapter 4.3`, `Chapter 4.4`
  - ❌ **Forbidden:** `Chapter 02.1`, `Chapter 02.2`, `Chapter 03.1`, `Chapter 04.1`, `Chapter 04.2`, `Chapter 04.3`, `Chapter 04.4`
- **File Naming Standard:**
  - Files with sub-chapters must follow the exact unpadded pattern: `Chapter-X.Y-[Topic].ipynb`
  - ✅ **Correct:** `Chapter-2.1-Linear-Algebra.ipynb`, `Chapter-4.3-Unsupervised-Learning.ipynb`
  - ❌ **Forbidden:** `Chapter-02.1-Linear-Algebra.ipynb`, `Chapter-04.3-Unsupervised-Learning.ipynb`

---

## ✅ Rule 2 — Chapter Overview (Mandatory)

Immediately after the title, a "What you will learn" overview cell:

```markdown
## 🎯 What You Will Learn

By the end of this chapter, you will be able to:

- [ ] Explain [concept 1] in simple terms
- [ ] Describe [concept 2] with a real-world example
- [ ] Identify [concept 3] in a product context
- [ ] Write code that demonstrates [concept 4]

**Estimated Reading Time:** ~XX minutes
```

---

## ✅ Rule 3 — Table of Contents (Mandatory)

After the overview, a clickable TOC must list all topics:

```markdown
## 🗂️ Table of Contents

1. [Topic 1](#1-topic-1)
2. [Topic 2](#2-topic-2)
3. [Topic 3](#3-topic-3)
...
```

---

## ✅ Rule 4 — Section Notes Structure (Mandatory for EVERY Topic)

Every topic section **must** contain all of the following subsections.  
**None can be skipped.**

---

### 4a. Section Header

```markdown
---

## X. [Topic Name]

---
```

---

### 4b. 🗣️ Simple English Definition (MANDATORY)

Write the definition as if explaining to someone with **zero technical background**.  
Use short sentences. Avoid jargon. If you use a technical word, immediately explain it.

**Template:**

```markdown
### 🗣️ In Simple English

[Topic] is basically [one-line plain English definition].

Think of it this way: [one sentence analogy using everyday objects/situations].

The key point is: [the single most important thing to remember].
```

**Example (good ✅):**
```markdown
### 🗣️ In Simple English

An **API** is basically a waiter at a restaurant.

Think of it this way: You (the app) don't go into the kitchen (the server) yourself — 
you tell the waiter (the API) what you want, and the waiter brings it back to you.

The key point is: APIs let different software systems talk to each other without 
needing to know how the other one works internally.
```

**Example (bad ❌):**
```markdown
### Definition

An API is an application programming interface that enables 
inter-process communication between heterogeneous systems.
```

---

### 4c. 🌍 Real-Life Analogy (MANDATORY)

Every concept must have **at least one real-life analogy** from everyday life.  
Use familiar things: restaurants, supermarkets, airports, schools, phones, etc.

**Template:**

```markdown
### 🌍 Real-Life Example

**Scenario:** [Describe a familiar, everyday situation]

| Real Life | Tech Equivalent |
|-----------|----------------|
| [Real thing 1] | [Tech thing 1] |
| [Real thing 2] | [Tech thing 2] |
| [Real thing 3] | [Tech thing 3] |

**Why this matters:** [Connect the analogy back to what AI Engineers actually do]
```

**Example:**
```markdown
### 🌍 Real-Life Example

**Scenario:** Think of a Google search.

| Real Life | Tech Equivalent |
|-----------|----------------|
| You type a question into Google | User sends a query |
| Google searches billions of pages | Vector similarity search |
| Google returns the top 10 results | Retrieved chunks from vector DB |
| You read the results and form an answer | LLM generates a response |

**Why this matters:** RAG is literally how AI engineers make LLMs "search" 
your private documents the same way Google searches the web.
```

---

### 4d. 📖 Deep-Dive Notes (MANDATORY)

After the simple explanation and analogy, go deeper.  
This is where technical detail lives — but still written clearly.

**Required elements inside Deep-Dive Notes:**

1. **How it works** (step-by-step, numbered list)
2. **Key sub-concepts** (short bullet points with explanations)
3. **Visual diagram** (ASCII diagram or table showing relationships)
4. **Common misconceptions** (at least 1 myth vs. reality)
5. **When to use it** (practical guidance)

**Template:**

```markdown
### 📖 How It Works (Step by Step)

1. **Step 1:** [What happens first]
2. **Step 2:** [What happens next]
3. **Step 3:** [What the result is]

---

### 🔑 Key Concepts

| Concept | What It Means | Why It Matters |
|---------|---------------|----------------|
| [Term 1] | [Plain explanation] | [Practical importance] |
| [Term 2] | [Plain explanation] | [Practical importance] |

---

### 🗺️ Visual Overview

\```
[ASCII diagram showing how the components relate]
\```

---

### 🚫 Common Misconceptions

| ❌ Myth | ✅ Reality |
|--------|-----------|
| [Wrong belief 1] | [What's actually true] |
| [Wrong belief 2] | [What's actually true] |

---

### ✅ When to Use This

- Use when: [situation 1]
- Use when: [situation 2]
- Avoid when: [situation 3]
```

---

### 4e. 📊 Key Concepts Table (MANDATORY)

A summary table at the end of each section's notes — before the code cell.

```markdown
### 📊 Section Quick Reference

| Term | Definition | Example |
|------|-----------|---------|
| [Term 1] | [1-line definition] | [1-line example] |
| [Term 2] | [1-line definition] | [1-line example] |
```

---

### 4f. 💻 Code Cell (If Applicable)

Code cells come **after** all notes for that section.  
Every code cell must have:

1. A **comment header** explaining what the code demonstrates
2. **Inline comments** on every meaningful line
3. A **print output** that clearly shows the concept in action
4. No raw, uncommented code blocks

**Template:**

```python
# ✅ Code Demo: [What this demonstrates]
# Concept: [Which concept from the notes above this shows]
# -----------------------------------------------------------

# [Inline comment explaining what this line does]
variable = some_function()

# [Inline comment explaining the output]
print(f"Result: {variable}")
```

**Rules for code cells:**
- ✅ Always include a comment header
- ✅ Always produce visible output (print statements)
- ✅ If API keys are needed, show commented-out real code + working simulated version
- ✅ Prefer simple, readable code over clever, compact code
- ❌ Never dump raw code with no explanation
- ❌ Never write code before the notes for that section

---

## ✅ Rule 5 — Chapter Summary (Mandatory)

At the end of every notebook, a summary table covering all topics:

```markdown
---

## 📝 Chapter Summary

| Topic | Simple Definition | Key Takeaway |
|-------|------------------|--------------|
| [Topic 1] | [1-line plain English] | [Most important thing to remember] |
| [Topic 2] | [1-line plain English] | [Most important thing to remember] |
```

---

## ✅ Rule 6 — Resources (Mandatory)

At least 3–5 curated resources per module:

```markdown
## 🔗 Resources & Further Reading

| Resource | Type | Why Read It |
|----------|------|-------------|
| [Title](URL) | Article / Video / Book | [1-line reason] |
```

---

## ✅ Rule 7 — Next Module Preview (Mandatory)

End every notebook with a preview of the next topic:

```markdown
## ➡️ Next Module: [Module Name]

In the next module, you will learn about:
- [Topic 1]
- [Topic 2]

*Provide the next topic to the AI to generate Module XX.*

---
*Made with ❤️ | Zero to Hero — AI Engineer Learning Path*
```

---

## 🚦 Quality Checklist (Run Before Finalizing Any Notebook)

Before any notebook is considered complete, verify:

- [ ] Title cell present with all metadata
- [ ] "What you will learn" overview present
- [ ] Table of contents present and links work
- [ ] **Every section has a Simple English definition**
- [ ] **Every section has a Real-Life Analogy**
- [ ] **Every section has Deep-Dive Notes**
- [ ] **Every section has a Key Concepts table**
- [ ] Code cells (if any) come AFTER notes
- [ ] All code cells have comments and produce output
- [ ] Chapter Summary table at the end
- [ ] Resources section present
- [ ] Next Module preview present

---

## 📏 Writing Style Rules

| Rule | Do This ✅ | Not This ❌ |
|------|-----------|-----------|
| **Language** | Simple, conversational English | Dense academic writing |
| **Sentence length** | Short sentences (< 20 words preferred) | Long compound sentences |
| **Jargon** | Define immediately when used | Use without explanation |
| **Examples** | Real-world, relatable situations | Abstract or overly technical |
| **Tone** | Friendly, encouraging, like a mentor | Cold, textbook-style |
| **Analogies** | Everyday life (food, travel, school) | Other tech comparisons |

---

## 🗂️ File Naming Convention

```
Module-01-Introduction/
    Chapter-01-Introduction.ipynb

Module-02-Mathematics/
    Chapter-2.1-Linear-Algebra.ipynb
    Chapter-2.2-Calculus-and-Differentiation.ipynb

Module-04-Machine-Learning/
    Chapter-4.1-Core-ML-Concepts.ipynb
    Chapter-4.2-Classical-Algorithms.ipynb
    Chapter-4.3-Unsupervised-Learning.ipynb
    Chapter-4.4-Feature-Engineering.ipynb
```

- Use `Module-XX` prefix (zero-padded 2 digits) for module folders.
- **When a decimal point is present, NEVER use a leading zero:**
  - ✅ `Chapter-2.1-[Topic].ipynb`, `Chapter-4.3-[Topic].ipynb`
  - ❌ `Chapter-02.1-...`, `Chapter-04.3-...`
- For single-chapter standalone modules without decimals: `Chapter-01-Introduction.ipynb`
- Use kebab-case for folder and file names. No spaces in filenames.

---

*This guidelines file is the single source of truth for all notebooks in this repository.*  
*Last updated: October 2026*
