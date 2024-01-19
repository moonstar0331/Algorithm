import sys
input = sys.stdin.readline

# 입력
n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 100005

ans = 0
R = -1
for L in range(n):
    while R+1 < n and cnt[a[R+1]] == 0:
        R += 1
        cnt[a[R]] += 1
    ans += R - L + 1
    cnt[a[L]] -= 1

print(ans)