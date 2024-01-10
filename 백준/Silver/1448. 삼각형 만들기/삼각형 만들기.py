import sys

# 입력
N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

# 정렬
A.sort()

answer = -1
for i in range(N - 1, 1, -1):
    if A[i] < A[i-1] + A[i-2]:
        answer = A[i] + A[i-1] + A[i-2]
        break

print(answer)