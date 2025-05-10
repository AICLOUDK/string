# python3
def build_suffix_array(s):
    n = len(s)
    R = [ord(c) for c in s]
    SA = list(range(n))
    k = 1
    while k < n:
        SA.sort(key=lambda x: (R[x], R[x + k] if x + k < n else -1))
        NR = [0] * n
        for i in range(1, n):
            prev, curr = SA[i-1], SA[i]
            NR[curr] = NR[prev]
            if (R[prev], R[prev + k] if prev + k < n else -1) != \
               (R[curr], R[curr + k] if curr + k < n else -1):
                NR[curr] += 1
        R = NR
        k <<= 1
        if R[SA[-1]] == n - 1:
            break
    return SA

import sys
text = sys.stdin.readline().strip()
print(" ".join(map(str, build_suffix_array(text))))