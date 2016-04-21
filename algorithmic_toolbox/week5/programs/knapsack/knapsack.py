# Uses python3
import sys

def optimal_weight(W, w):
    n = len(w)
    opt_value = [[0 for i in range(n + 1)]  for j in range(W+1)]

    for i in range(1,n + 1):
      for weight in range(1,W + 1):
        opt_value[weight][i] = opt_value[weight][i-1]
        # Weight of ith item
        Wi = w[i-1]
        if Wi <= weight:
          # Vi = Wi as its a gold bar
          value = opt_value[weight-Wi][i-1] + Wi
          if value > opt_value[weight][i]:
            opt_value[weight][i] = value
    return opt_value[W][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
