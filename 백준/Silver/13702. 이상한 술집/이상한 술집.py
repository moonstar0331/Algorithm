import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

# N개 주전자 주문
# K명에게 똑같은 양으로 나눠주려 함
# 막걸리가 조금 남아 있다면 그냥 버림
# K명에게 최대한의 많은 양의 막걸리를 분배할 수 있는 용량은?
# 항상 N <= K -> 주전자의 개수가 사람 수보다 많을 수는 없다

def determination(amount):
    if amount == 0:
        return False
    sum = 0
    for x in A:
        sum += x // amount
    return sum >= K

l, r, ans = 0, 1 << 31, 0
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)