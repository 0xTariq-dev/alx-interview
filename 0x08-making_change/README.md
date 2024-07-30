### Making Change Challenge

# 💰 Make Change Function

This repository contains a Python function [`makeChange`](./0-making_change.py) that calculates the minimum number of coins needed to make a given amount of change. If it's not possible to make the exact amount, the function returns `-1`.

## 📋 Function Description

### [`makeChange(coins, total)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2Falx-interview%2F0x08-making_change%2F0-making_change.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A4%7D%5D "0x08-making_change/0-making_change.py")

#### Arguments:
- [`coins`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2Falx-interview%2F0x08-making_change%2F0-making_change.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A15%7D%5D "0x08-making_change/0-making_change.py") (list of integers): Available coin denominations.
- [`total`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fhome%2F0xTariq%2Frepos%2Falx-interview%2F0x08-making_change%2F0-making_change.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A22%7D%5D "0x08-making_change/0-making_change.py") (int): The total amount of change to be returned.

#### Returns:
- The minimum number of coins needed to meet the total.
- `0` if the total equals `0`.
- `-1` if the total can't be met by any combination of the coins.

## 🛠️ Usage

### Example
```python
from 0-making_change import makeChange

# Test cases
print(makeChange([1, 2, 25], 37))  # Expected output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
```

### Explanation
- The function first sorts the list of coins in descending order.
- It then iterates through each coin, using as many of that coin as possible.
- If the remaining amount is zero after using the coins, it returns the total number of coins used.
- If it's not possible to make the exact amount, it returns `-1`.

## 📂 File Structure
```
.
├── 0-making_change.py
└── README.md
```
