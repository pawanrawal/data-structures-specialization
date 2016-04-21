# Uses python3
import sys

def gcd(a, b):
  rem = 0
  if b == 0:
    return a
  else:
    rem = a % b
    return gcd(b, rem)


if __name__ == "__main__":
  input = sys.stdin.readline()
  a, b = map(int, input.split())
  print(gcd(a, b))
