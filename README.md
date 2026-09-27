# Personal Finance Tracker

A beginner Python command-line project for recording income and expenses, reviewing transaction history, and viewing simple financial summaries.

## Features

- Add income and expenses with a category and description.
- Keep a current balance and transaction history.
- Save and load the balance and transactions in a local JSON file (`finance_data.json`).
- Filter transaction history by today, this week, this month, or all transactions.
- Summarize income, expenses, and net change for a selected month and year.
- Show expense totals by category.
- Calculate compound growth from an initial amount, interest rate, and number of periods.
- Plot a cumulative balance line with Matplotlib.
- Reset saved finance data after confirmation.

## Requirements

- Python 3
- Matplotlib

Install Matplotlib with:

```bash
python -m pip install matplotlib
```

## Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Make sure a valid `finance_data.json` file is present in that folder. The program loads this file when it starts and currently does not create it automatically.
4. Run:

```bash
python main.py
```

The JSON file stores the current balance and transaction records. Keep it private if it contains real financial information. For a public repository, use an empty or fabricated sample file rather than personal records.

## Data format

The application expects a JSON object with a `current_balance` value and a `transactions` list. Each transaction has a type, amount, category, date, and description. Dates use the ISO format `YYYY-MM-DD`.

For a clean first run, create `finance_data.json` in the project folder with this starter content:

```json
{
  "current_balance": 0,
  "transactions": []
}
```

## Project notes

This is a learning project and a basic local command-line tool. It does not connect to a bank or provide financial advice. The balance chart is currently refreshed when income is added; adding an expense saves the transaction but does not call the chart refresh function. The add-income and add-expense amounts are read as integers without input validation.

## Built with

- Python (`json`, `datetime`, `calendar`, `os`, and `time`)
- Matplotlib
