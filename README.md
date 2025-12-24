# Python Automation – Crypto Price Reporting

## Overview
A production-style Python automation tool that fetches real-time crypto prices,
processes and validates the data, and generates CSV and JSON reports via a CLI interface.

This project demonstrates:
- API integration
- Data processing with pandas
- CLI design
- Logging
- Unit testing & mocking
- Clean project structure

## Tech Stack
- Python 3.10+
- requests
- pandas
- pytest

## Project Structure
```text
python-automation-project/
├── src/
│   ├── client.py
│   ├── processor.py
│   ├── reporter.py
│   └── main.py
├── tests/
└── README.md

```

## Installation
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt

## Usage
python -m src.main --coin bitcoin --currency usd --output reports


## Outputs:

reports/prices.csv

reports/prices.json

## Testing
pytest



