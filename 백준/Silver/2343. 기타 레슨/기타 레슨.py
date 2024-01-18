import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 블루레이에는 총 N개의 강의 들어감
# 강의의 순서가 바뀌면 안됨
# 블루레이의 개수를 최소화
# M개의 블루레이에 모두 녹화
# 블루레이의 크기(녹화 가능한 길이)를 최소를 구하기
# M개의 블루레이는 모두 같은 크기이어야 한다.

def determination(len):
    cnt, sum = 1, 0
    for x in A:
        if sum + x > len:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt <= M

l, r, ans = max(A), 1000000000, 0
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)