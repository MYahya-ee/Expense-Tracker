# Expense Tracker CLI

A command-line app to log, view, filter, and export personal expenses. Data persists locally in a JSON file.

---

## Features

- Add expenses with a name, amount, category, and auto-generated timestamp
- View all expenses in a formatted table
- Filter expenses by category
- View a summary of total spent per category
- Remove a single expense by ID
- Wipe all expenses at once
- Export a full report to a `.txt` file

---

## Getting Started

**Requirements:** Python 3.10+

```bash
git clone https://github.com/MYahya-ee/Expense-Tracker.git
cd Expense-Tracker
python main.py
```

No external libraries needed — only Python's standard library is used.

---

## Usage

On running the app you'll see a menu:

```
========= Expense Tracker =========
1. Add Expense
2. View All Expenses
3. Filter by Category
4. View Summary
5. Remove Expense
6. Remove all
7. Export Report (.txt)
0. Quit
===================================
```

Enter the number of the option you want and follow the prompts.

---

## Data Storage

All expenses are saved locally in `python.json` in the following format:

```json
[
  {
    "Name": "Water bottle",
    "Id": "7a931",
    "amount": 150.0,
    "date": "01:12 15/08",
    "category": "beverages"
  }
]
```

The exported report is saved as `report.txt` in the same directory.

---

## Built With

- `json` — data persistence
- `uuid` — unique expense IDs
- `datetime` — auto timestamps

---

## What I Learned

Built as a practice project to solidify core Python concepts — OOP, file I/O, JSON handling, exceptions, and working with libraries and modules.
