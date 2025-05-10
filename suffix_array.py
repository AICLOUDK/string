# python3
import sys
t=sys.stdin.readline().strip()
print(' '.join(map(str,sorted(range(len(t)),key=lambda i:t[i:]))))