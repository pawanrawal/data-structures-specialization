# Uses python3
import sys

# Starter code had a bug , read() should instead be readline.
input = sys.stdin.readline()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
