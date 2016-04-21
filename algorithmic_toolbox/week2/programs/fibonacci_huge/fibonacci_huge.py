# Uses python3
import sys

def get_period(m):
  i = 2

  while True:
    # while we don't find a repeating sequence indicated by a 0 and 1
    # we keep on appending nth fibonnaci number module m to the list
    fib_list.append((fib_list[i-1] + fib_list[i-2]) % m)

    # if we find a repeating sequence we break and return i - 1 which would be
    # the length of the repeating sequence.
    if fib_list[i] == 1 and fib_list[i-1] == 0:
      break

    i = i + 1

  return i - 1

def get_fibonaccihuge(n, m):
  period = get_period(m)
  # Once we have the period the remainder of fib(n) % m is same as
  # the remainder of the (n % period) fibonacci number as explained in the instructions for the exercise.
  return fib_list[n % period]


if __name__ == '__main__':
  input = sys.stdin.readline();
  n, m = map(int, input.split())

  # We create a dynamic list , as we don't know the size for the list
  fib_list = []
  fib_list.append(0)
  fib_list.append(1)

  # print(get_period(m))
  print(get_fibonaccihuge(n, m))
