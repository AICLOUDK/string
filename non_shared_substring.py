# python3
import sys

def find_shortest_non_shared_substring(a, b):
    H = len(a)
    for l in range(1, H + 1):
        for C in range(H - l + 1):
            substring = a[C:C + l]
            if substring not in b:
                return substring
    return ""

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
result = find_shortest_non_shared_substring(a, b)
print(result)