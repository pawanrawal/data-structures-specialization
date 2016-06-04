# python3
import random

p = 1000000007 #big prime
x = random.randint(1,p-1)

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def precompute_hashes(text,plen,pattern,x):
    H = [0 for i in range(len(text)- len(pattern)+1)]
    S = text[len(text)-plen:]
    H[len(text)-plen] = poly_hash(S)
    y = 1
    for i in range(1,plen+1):
        y = y*x % p

    for i in range(len(text)-plen-1,-1,-1):
        H[i] = (x*H[i+1] + ord(text[i]) - y*ord(text[i+plen])) % p
    return H

def poly_hash(pattern): 
    ans = 0
    for c in reversed(pattern):
        ans = (ans * x + ord(c)) % p
    return ans

def get_occurrences(pattern, text):
    result = []
    pHash = poly_hash(pattern)
    H = precompute_hashes(text,len(pattern),pattern,x)
    for i in range(0,len(text)-len(pattern)+1):
        if pHash != H[i]:
            continue
        if pattern == text[i:i+len(pattern)]:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

