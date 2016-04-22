#Uses python3

import sys

def lcs3(a, b,c):
    # A represents alignment score
    A = [[[0 for j in range(len(c)+1)] for i in range(len(b)+1)] for k in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            for k in range(1, len(c)+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    A[i][j][k] = max(A[i-1][j-1][k-1]+1, A[i][j-1][k],A[i-1][j][k], A[i-1][j-1][k],
                        A[i-1][j][k-1], A[i][j-1][k-1], A[i][j][k-1])
                else:
                    A[i][j][k] = max(A[i-1][j-1][k-1], A[i][j-1][k],A[i-1][j][k], A[i-1][j-1][k],
                        A[i-1][j][k-1], A[i][j-1][k-1], A[i][j][k-1])

    return A[len(a)][len(b)][len(c)]

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
