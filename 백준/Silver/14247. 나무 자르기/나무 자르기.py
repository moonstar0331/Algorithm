import sys

# 입력
N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
I = list(range(N))

# 정렬
I = sorted(I, key=lambda i: A[i])

ans = 0
for i in range(N):
    index = I[i]
    ans += H[index] + i * A[index]

print(ans)