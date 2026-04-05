# Python Inventory Management System

## Setup

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python main.py
```

## Running Tests

```bash
python -m pytest
```

## File Structure

```
├── main.py                  # Entry point
├── requirements.txt
├── assets/
│   └── inventory.csv        # Default inventory data file
├── core/
│   ├── models.py            # Item, Electronics, and Grocery classes
│   ├── inventory.py         # Inventory class with add/remove/update logic
│   ├── exceptions.py        # Custom exception hierarchy
│   └── utils.py             # Utility functions (filter, sort, etc.)
├── interface/
│   └── cli.py               # Interactive command-line interface
└── tests/
    ├── test_models.py        # Unit tests for models
    └── test_inventory.py     # Unit tests for inventory and utilities
```