#Uses python3

import sys

def commonseq(i,j,A,a):
    if i == 0 and j == 0:
        return
    if i > 0 and A[i][j] == A[i-1][j]:
        commonseq(i-1,j,A,a)
    elif j>0 and A[i][j] == A[i][j-1]:
        commonseq(i,j-1,A,a)
    else:
        if A[i][j] == A[i-1][j-1] + 1:
            # If we have a match of a[i-1] and b[j-1] ,then we append that entry
            # to our substr list.
            substr.append(a[i-1])
        commonseq(i-1, j-1,A,a)


def lcs2(a, b):
    global substr
    substr = []
    # A represents alignment score
    A = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                A[i][j] = max(A[i-1][j-1]+1, A[i-1][j], A[i][j-1])
            else:
                A[i][j] = max(A[i-1][j-1], A[i-1][j], A[i][j-1])

    commonseq(len(a),len(b),A,a)
    return list(reversed(substr))

def lcs3(a, b, c):
    commonAB = lcs2(a,b)
    commonBC = lcs2(b,c)
    commonABC = lcs2(commonAB, commonBC)
    return len(commonABC)

if __name__ == '__main__':
    global a,b,c
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
