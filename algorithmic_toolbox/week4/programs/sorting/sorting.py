# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    # We do this in two iterations. The first is same as partition2
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[j],a[l] = a[l],a[j]

    # We now go through a part of the array(upto j) again and divide into two parts
    # l-k , k-j such that elements a[k] to a[j] = x
    k = j

    i = l
    while i < k:
        if a[i] == x:
            k -= 1
            a[i], a[k] = a[k], a[i]
        i += 1

    return k, j


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
