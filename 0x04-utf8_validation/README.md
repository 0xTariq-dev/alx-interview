# UTF-8 Validation Interview Preparation

## Description
This directory contains the solutions to the problems of the UTF-8 Validation module.
The aim is to determine if a given data set represents a valid UTF-8 encoding.
- `0-validate_utf8.py`: Python function that determines if a given data set represents a valid UTF-8 encoding.
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

---

## Example

| data | result |
|------|--------|
| `[65]` | `True` |
| `[80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]` | `True` |
| `[229, 65, 127, 256]` | `False` |