
import utils

# Validation
print(utils.is_number("123.5"))
print(utils.is_valid_email("student@example.com"))
print(utils.is_valid_phone("9876543210"))
print(utils.is_in_range(75, 0, 100))

# Formatting
print(utils.format_currency(12500))
print(utils.format_percentage(87.456))
print(utils.format_title("python utility module"))

# Calculations
print(utils.calculate_percentage(25, 100))
print(utils.calculate_average([10, 20, 30, 40]))
print(utils.calculate_discount(1000, 15))
print(utils.calculate_tax(1000, 18))

# File utilities
utils.write_text_file("data/sample.txt", "Hello, Python!")

print(utils.file_exists("data/sample.txt"))
print(utils.get_file_extension("report.pdf"))
print(utils.read_text_file("data/sample.txt"))
print(utils.list_files("data", ".txt"))
