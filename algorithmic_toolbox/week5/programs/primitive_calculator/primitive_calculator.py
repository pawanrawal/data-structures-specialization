# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def correct_sequence(n):
    numSteps = [0] * (n+1)
    lastPointers = [0] * (n+1)
    for i in range(2,n + 1):
        minCount = sys.maxsize
        if i % 3 == 0:
            count = numSteps[i//3] + 1
            if count < minCount:
                minCount = count
                numSteps[i] = count
                lastPointers[i] = i//3
        if i % 2 == 0:
            count = numSteps[i//2] + 1
            if count < minCount:
                minCount = count
                numSteps[i] = count
                lastPointers[i] = i//2
        if i >= 1:
            count = numSteps[i-1] + 1
            if count < minCount:
                minCount = count
                numSteps[i] = count
                lastPointers[i] = i - 1

    sequence = []
    while n > 0:
        sequence.append(n)
        n = lastPointers[n]

    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(correct_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
