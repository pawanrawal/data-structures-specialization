# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    n = len(weights)

    # We get a list of value per weight.
    valueperweight = [v/w for v,w in zip(values, weights)]

    # This sorts the weight array according to decreasing value per weight values.
    weights = [x for y,x in sorted(zip(valueperweight, weights), reverse=True)]
    # This sorts the values array according to decreasing value per weight values.
    values = [x for y,x in sorted(zip(valueperweight, values), reverse= True)]

    # Finally sorting value per weight according to decreasing value per weight
    valueperweight = sorted(valueperweight, reverse= True)

    for i in range(0,n):
      if capacity == 0:
        return value

      w = min(weights[i], capacity)
      capacity -= w
      # increasing value according to weight which is added to capacity.
      value += w * valueperweight[i]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
