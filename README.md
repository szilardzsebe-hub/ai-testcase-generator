# AI-Assisted Test Case Generator

## Overview

This project is a Python-based tool that converts software requirements into structured test cases.
It generates **positive, negative, and boundary test scenarios** and exports them into **JSON and Excel formats**.

The goal of this project is to simulate a real QA automation workflow and prepare for future AI-assisted test design.

---

## Features

* Requirement-based test case generation
* Rule-based classification (password, login, registration)
* Structured test case output (ID, type, description, expected result)
* JSON export for data processing
* Excel export for QA-friendly reporting
* Modular Python architecture

---

## Example Input

User requirement:

```
User can reset password using email
```

---

## Example Output

| ID     | Type     | Description                                 | Expected Result            |
| ------ | -------- | ------------------------------------------- | -------------------------- |
| TC-001 | Positive | Verify password reset with valid email      | Email is sent successfully |
| TC-002 | Negative | Verify password reset with invalid email    | Error message displayed    |
| TC-003 | Boundary | Verify password reset with max email length | System handles input       |

---

## Tech Stack

* Python 3.13
* openpyxl (Excel export)
* JSON (data serialization)

---

## Project Structure

```

ai-testcase-generator/
│
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── generator.py
├── models.py
├── excel_exporter.py
└── output/
```

---

## How to Run

```bash
python main.py
```

---

## Future Improvements

* AI-based test case generation (LLM integration)
* Requirement analysis (missing edge cases detection)
* Coverage scoring system
* Web interface (FastAPI)
* Database storage (SQLite)

---

## Author

QA Engineer transitioning into Test Automation & AI-assisted QA tooling.
