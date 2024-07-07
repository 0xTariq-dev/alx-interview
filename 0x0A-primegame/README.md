# Prime Game Challenge Interview Preparation

## Description :page_with_curl:
Maria and Ben are playing a game. Given a set of consecutive integers starting from `1` up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
They play `x` rounds of the game, where `n` may be different for each round.
Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

## Function Description :gear:
- Prototype: `def isWinner(x, nums)`
- `x`: an integer representing the number of rounds
- `nums`: an array of `n` integers
- Returns: The name of the player that won the most rounds
- You can assume that `n` and `x` will not be larger than `1000`
- You cannot import any libraries or packages.

## Example :memo:
- `x = 3, nums = [4, 5, 1]`
- First round: `n = 4`
  - Maria picks 2 and removes 2, 4
  - Ben picks 3 and removes 3
  - Ben wins because there are no prime numbers left for Maria to choose

- Second round: `n = 5`
    - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    - Ben picks 3 and removes 3, leaving 1, 5
    - Maria picks 5 and removes 5
    - Maria wins because there are no prime numbers left for Ben to choose

- Third round: `n = 1`
    - Ben wins because there are no prime numbers for Maria to choose

- __Result__: _Ben won 2 out of 3 rounds, so the winner is Ben_

> i.e.
```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

```bash
$ python 0-main.py
Winner: Ben
```
## Requirements :hammer_and_wrench:
- `Python 3.7` or higher


