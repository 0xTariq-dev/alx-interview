### Island Perimeter Challenge

# 🌴 Island Perimeter Function

This repository contains a Python function [`island_perimeter`](./0-island_perimeter.py) that calculates the perimeter of an island described by a grid. The grid contains `0` (representing water) and `1` (representing land).

## 📋 Function Description

### [`island_perimeter(grid)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2Falx-interview%2F0x08-island_perimeter%2F0-island_perimeter.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A4%7D%5D "0x08-island_perimeter/0-island_perimeter.py")

#### Arguments:
- [`grid`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2Falx-interview%2F0x08-island_perimeter%2F0-island_perimeter.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A15%7D%5D "0x08-island_perimeter/0-island_perimeter.py") (list of lists of integers): The grid that describes the island, containing `0` (water) and `1` (land).

#### Returns:
- The perimeter of the island.

## 🛠️ Usage

### Example
```python
from 0-island_perimeter import island_perimeter

# Example
```python
    print(island_perimeter([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]))  # Expected output: 16
```
