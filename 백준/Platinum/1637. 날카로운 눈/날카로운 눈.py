import sys
input = sys.stdin.readline

# 입력
n = int(input())
info = []
for i in range(n):
    info.append(list(map(int, input().split())))

# 정수가 여러 개 모여 있는 정수더미
# 어떤 특정한 정수 하나만 홀수개 존재
# 나머지 정수는 모두 짝수개 존재
# 그 안에 홀수개 존재하는 정수를 찾기
# 홀수개 존재하는 정수 & 몇 개인지 // 없다면 NOTHING

def count(A, C, B, X):
    if X < A:
        return 0
    if C < X:
        return (C - A) // B + 1
    return (X - A) // B + 1

def determination(candidate):
    sum = 0
    for i in info:
        sum += count(i[0], i[1], i[2], candidate)
    return sum % 2 == 1

l, r, ans, ansCnt = 1, 1 << 31, 0, 0
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

if ans == 0:
    print("NOTHING")
else:
    for i in info:
        if i[0] <= ans and ans <= i[1] and (ans - i[0]) % i[2] == 0:
            ansCnt += 1
    print(ans, ansCnt)