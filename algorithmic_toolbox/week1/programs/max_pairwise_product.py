# Uses python3
import random

def maxPairwiseProduct(a):
  largest = 0

  for i in range(0,n):
    for j in range(0,n):
      if a[i] * a[j] > largest and j!=i:
        largest = a[i]*a[j]

  return largest

def maxPairwiseProductFast(a):
  n = len(a)
  largestValIndex = 0
  secondLargestVal = 0

  for i in range(0, n):
    if a[i] > a[largestValIndex]:
      largestValIndex = i

  for j in range(0,n):
    if a[j] > secondLargestVal and j != largestValIndex:
      secondLargestVal = a[j]

  return a[largestValIndex]*secondLargestVal

# Stress testing code
# while True:
#   n = random.randint(2,11)
#   print('n', n, '\n')
#   a = [random.randint(0, 100000) for i in range(n)]
#   print('a ', a, '\n')
#   res1 = maxPairwiseProduct(a)
#   res2 = maxPairwiseProductFast(a)

#   if res1 != res2:
#     print('Wrong answer: ', res1, ' ', res2)
#     break
#   else:
#     print('Ok')

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)
print(maxPairwiseProductFast(a))

