# Uses python3
import sys

def get_majority_element(a):
    mapElem = {}
    for elem in a:
        mapElem[elem] = mapElem.get(elem, 0) + 1

    for _, val in mapElem.items():
        if val > len(a)//2:
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
