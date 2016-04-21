# Uses python3
def calc_fib(n):
  # We need to calculate nth fibonacci number only if n > 1 (n=0 and 1 have already been initialized)
  if (n > 1):
    for i in range(2, n+1):
      fib_list.append(fib_list[i-1] + fib_list[i-2])
  return fib_list[n]

n = int(input())

# Initializing a list
fib_list = []
# Initializing values for 0th and 1st fibonacci number
fib_list.append(0)
fib_list.append(1)

print(calc_fib(n))
