# Uses python3
import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

operands = []
m = []
M = []

def MinAndMax(i,j):
    minimum = sys.maxsize
    maximum = -sys.maxsize - 1
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], operands[k])
        b = evalt(M[i][k], m[k+1][j], operands[k])
        c = evalt(m[i][k], M[k+1][j], operands[k])
        d = evalt(m[i][k], m[k+1][j], operands[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return minimum, maximum


def get_maximum_value(dataset):
    global m,M,operands
    data = list(dataset)
    digits = list(map(int,data[0::2]))
    operands = data[1::2]
    n = len(digits)

    m = [[0 for i in range(n)] for j in range(n)]
    M = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1,n):
        for i in range(n-s):
            j = i+s
            m[i][j], M[i][j] = MinAndMax(i,j)
    #write your code here
    return M[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
