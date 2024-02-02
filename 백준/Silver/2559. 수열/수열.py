import sys
input = sys.stdin.readline

n, K = map(int, input().split())
a = list(map(int, input().split()))

R, sum, ans = -1, 0, -100 * n

for L in range(n - K + 1):
    while R + 1 <= L + K -1:
        R += 1
        sum += a[R]
    
    ans = max(ans, sum)
    sum -= a[L]

print(ans)
