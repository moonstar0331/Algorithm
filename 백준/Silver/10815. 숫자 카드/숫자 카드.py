import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if B[i] in A:
        print(1, end=" ")
    else:
        print(0, end=" ")