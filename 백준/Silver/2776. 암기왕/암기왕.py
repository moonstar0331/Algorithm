import sys

# 입력
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    A = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    B = list(map(int, sys.stdin.readline().split()))

    for i in range(M):
        if B[i] in A:
            print(1)
        else:
            print(0)