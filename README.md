# Python Utility Module

## Description
A reusable Python module containing commonly used functions for input validation, formatting, calculations, and file operations. It helps reduce code duplication and makes Python projects easier to maintain.

## Features
- **Input Validation:** Check numeric values, email formats, phone numbers, and numeric ranges.
- **Formatting:** Format currency, percentages, and title-case text.
- **Calculations:** Calculate percentages, averages, discounts, and taxes.
- **File Utilities:** Check file existence, retrieve file extensions, read and write text files, and list files by extension.
- **Reusable Functions:** Import utility functions into multiple Python projects.

## Project Structure
```text
python_utils/
├── utils.py
├── main.py
└── README.md
```

## Requirements
- Python 3.6 or later
- No external libraries required

## Installation and Setup
1. Download or clone the project.
2. Place `utils.py` in your project directory.
3. Import the module into your Python program.

```python
import utils
```

## Usage Examples

### 1. Input Validation
```python
import utils

print(utils.is_number("123.5"))
print(utils.is_valid_email("student@example.com"))
print(utils.is_valid_phone("9876543210"))
print(utils.is_in_range(75, 0, 100))
```

### 2. Formatting
```python
print(utils.format_currency(12500))
print(utils.format_percentage(87.456))
print(utils.format_title("python utility module"))
```

### 3. Calculations
```python
print(utils.calculate_percentage(25, 100))
print(utils.calculate_average([10, 20, 30, 40]))
print(utils.calculate_discount(1000, 15))
print(utils.calculate_tax(1000, 18))
```

### 4. File Operations
```python
utils.write_text_file("data/sample.txt", "Hello, Python!")

print(utils.file_exists("data/sample.txt"))
print(utils.get_file_extension("report.pdf"))
print(utils.read_text_file("data/sample.txt"))
print(utils.list_files("data", ".txt"))
```

## Running the Project
Run the demonstration program from your terminal:

```bash
python main.py
```

Ensure that `utils.py` and `main.py` are in the same directory.

## Error Handling
- `is_number()` returns `False` for values that cannot be converted to numbers.
- `calculate_percentage()` raises a `ValueError` if the whole is zero.
- `calculate_average()` raises a `ValueError` if the list is empty.
- `calculate_discount()` rejects negative prices and discounts outside the range of 0–100.
- File operations may raise exceptions if files or folders cannot be accessed.

## Learning Objectives
- Understand Python modules and imports.
- Create reusable functions.
- Validate user data.
- Separate calculations from the main program.
- Work with files using `pathlib`.
- Handle errors with exceptions.

## Future Improvements
- Add date and time utilities.
- Add password-strength validation.
- Add JSON file utilities.
- Add logging and automated unit tests.

## License
This project is available for educational and personal use.
