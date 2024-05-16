# Minimum Opertions Interview Preparation

## Description
Given a file with a single character `H` and a number `n`
You can only perform one of the following operations:
- `CopyAll` - Copy all the characters of the file
- `Paste` - paste the copied characters

The script will find the minimum number of operations required to get n`H` characters in the file.
The Script uses Prime Factorization to find the minimum number of operations required.


## Example
The input data will be a single line with a single character `H` and a number `n` separated by a space.
> i.e.
```
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```
> Output:
```
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
```

## Requirements
- Python 3.6 or higher


