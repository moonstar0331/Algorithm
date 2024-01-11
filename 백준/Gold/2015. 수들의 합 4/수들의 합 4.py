import sys

# 입력
N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 누적합 구하기
psum = [0] * N
psum[0] = a[0]
for i in range(1, N):
    psum[i] = psum[i-1] + a[i]

count = {} # Dictionary, count[key] = 내 앞에 psum값이 key인 것의 갯수
answer = 0
for i in range(N):
    goal = psum[i] - M

    if goal in count:
        answer += count[goal]
    if goal == 0:
        answer += 1

    if psum[i] not in count:
        count[psum[i]] = 0
    count[psum[i]] += 1

print(answer)