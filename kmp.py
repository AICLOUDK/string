# python3
import sys

def compute_prefix_function(pattern):
    prefix = [0] * len(pattern)
    k = 0
    for i in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        prefix[i] = k
    return prefix

def find_pattern(pattern, text):
    prefix = compute_prefix_function(pattern)
    result = []
    q = 0
    for i in range(len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = prefix[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == len(pattern):
            result.append(i - len(pattern) + 1)
            q = prefix[q - 1]
    return result

if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
