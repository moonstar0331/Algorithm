import sys

# 입력
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 누적합 구하기
psum = [0] * N
psum[0] = a[0]
for i in range(1, N):
    psum[i] = psum[i-1] + a[i]

# 쿼리
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    # (구간 [a, b]의 원소의 합) = (구간 [1, b]의 원소의 합) - (구간 [1, a-1]의 원소의 합)
    if a == 1:
        answer = psum[b-1]
    else:
        answer = psum[b-1] - psum[a-2]
    
    print(answer)