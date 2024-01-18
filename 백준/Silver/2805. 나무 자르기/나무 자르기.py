import sys
input = sys.stdin.readline
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

def determination(H):
    sum = 0
    for x in a:
        if x > H:
            sum += x - H
    return sum >= m

l, r, ans = 0, 2000000000, 0
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)