# Uses python3
import sys

def get_number_of_inversions(a):
    number_of_inversions = 0
    if len(a) <= 1:
        return number_of_inversions
    mid = len(a) // 2

    lefthalf = a[:mid]
    righthalf = a[mid:]
    number_of_inversions += get_number_of_inversions(lefthalf)
    number_of_inversions += get_number_of_inversions(righthalf)

    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] > righthalf[j]:
            a[k] = righthalf[j]
            j += 1
            # If an element in the righthalf at index j is less than an element in the lefthalf at index i ,
            # then it is less than all elements in the left half half from index i to mid - 1
            number_of_inversions += (mid - i)
        else:
            a[k] = lefthalf[i]
            i += 1
        k += 1

    while j < len(righthalf):
        a[k] = righthalf[j]
        j += 1
        k += 1
    while i < len(lefthalf):
        a[k] = lefthalf[i]
        i += 1
        k += 1

    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a))
