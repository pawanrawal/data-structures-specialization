# Uses python3
import sys

def get_fibonacci_last_digit(n):
  if (n > 1):
    for i in range(2, n+1):
      fib_array[i] = (fib_array[i-1] + fib_array[i-2]) % 10
  return fib_array[n]

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)

    fib_array = [None] * (n + 1)

    fib_array[0] = 0
    fib_array[1] = 1

    print(get_fibonacci_last_digit(n))
