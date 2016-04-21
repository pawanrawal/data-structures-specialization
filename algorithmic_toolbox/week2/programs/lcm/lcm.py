# Uses python3
import sys

def calc_gcd(a, b):
  rem = 0
  if b == 0:
    return a
  else:
    rem = a % b
    return calc_gcd(b, rem)

def lcm(a, b):
  gcd = calc_gcd(a , b)
  return (a * b)//gcd

if __name__ == '__main__':
  input = sys.stdin.readline()
  a, b = map(int, input.split())
  print(lcm(a, b))

