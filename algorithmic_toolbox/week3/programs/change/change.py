# Uses python3
import sys

# Min coins required, declared as a global variable.
min_coins = 0

# Given an amount n , it choses max coin possible
def choose_max_coin(n):
  max_coin = None

  if n >= 10:
    max_coin = 10
  elif n >= 5:
    max_coin = 5
  elif n >= 1:
    max_coin = 1

  return max_coin

def get_change(n):
  global min_coins

  # If n == 0 we return as we already have min coins
  if n == 0:
    return min_coins

  # We chose the coin with largest quantity possible for input n. This is a safe choice
  # for our greedy solution.
  coin = choose_max_coin(n)

  # Subtracting to get the remainder value and also incrementing min_coins
  n -= coin
  min_coins +=1

  # Recursively solving a smaller problem.
  return get_change(n)

if __name__ == '__main__':
  n = int(sys.stdin.readline())

  print(get_change(n))
