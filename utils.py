
import re
from pathlib import Path


# =========================
# 1. INPUT VALIDATION
# =========================

def is_number(value):
    """Check whether a value can be converted to a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_email(email):
    """Check whether an email has a basic valid format."""
    if not isinstance(email, str):
        return False

    pattern = r"^[\w.+-]+@[\w-]+(?:\.[\w-]+)+$"
    return bool(re.fullmatch(pattern, email))


def is_valid_phone(phone):
    """Check whether a phone number has 10 digits."""
    if not isinstance(phone, str):
        return False

    digits = phone.strip()
    return digits.isdigit() and len(digits) == 10


def is_in_range(value, minimum, maximum):
    """Check whether a number lies within an inclusive range."""
    if not is_number(value):
        return False

    value = float(value)
    return minimum <= value <= maximum


# =========================
# 2. FORMATTING
# =========================

def format_currency(amount, symbol="₹"):
    """Format a number as currency."""
    return f"{symbol}{amount:,.2f}"


def format_percentage(value):
    """Format a number as a percentage."""
    return f"{value:.2f}%"


def format_title(text):
    """Convert text to title case."""
    return str(text).title()


# =========================
# 3. CALCULATIONS
# =========================

def calculate_percentage(part, whole):
    """Calculate what percentage part is of whole."""
    if whole == 0:
        raise ValueError("Whole cannot be zero.")

    return (part / whole) * 100


def calculate_average(numbers):
    """Calculate the average of a collection of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")

    return sum(numbers) / len(numbers)


def calculate_discount(price, discount_percent):
    """Calculate the final price after a discount."""
    if price < 0:
        raise ValueError("Price cannot be negative.")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    discount = price * discount_percent / 100
    return price - discount


def calculate_tax(amount, tax_percent):
    """Calculate tax on an amount."""
    if amount < 0 or tax_percent < 0:
        raise ValueError("Amount and tax rate cannot be negative.")

    return amount * tax_percent / 100


# =========================
# 4. FILE UTILITIES
# =========================

def file_exists(path):
    """Check whether a file exists."""
    return Path(path).is_file()


def get_file_extension(path):
    """Return the file extension, including the dot."""
    return Path(path).suffix


def read_text_file(path, encoding="utf-8"):
    """Read and return the contents of a text file."""
    return Path(path).read_text(encoding=encoding)


def write_text_file(path, content, encoding="utf-8"):
    """Write text to a file, creating parent folders if needed."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(str(content), encoding=encoding)


def list_files(folder, extension=None):
    """List files in a folder, optionally filtering by extension."""
    folder_path = Path(folder)

    if not folder_path.is_dir():
        raise NotADirectoryError(f"Folder not found: {folder}")

    files = [item for item in folder_path.iterdir() if item.is_file()]

    if extension:
        if not extension.startswith("."):
            extension = "." + extension

        files = [
            item for item in files
            if item.suffix.lower() == extension.lower()
        ]

    return files
