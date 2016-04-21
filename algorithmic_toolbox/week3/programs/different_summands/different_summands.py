# Uses python3
import sys

def optimal_summands(n):
    summands = []
    summand = 1

    while n > 0:
      # According to lema mentioned in notes summand can be used if
      # 2 * summand > n , else we take n as a summand.
      if n <= 2 * summand:
        summands.append(n)
        n = 0
      else:
        # If summand can be used, we append it and decrease n. We also increment summand to be used
        # for next iteration.
        summands.append(summand)
        n -= summand
        summand += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
