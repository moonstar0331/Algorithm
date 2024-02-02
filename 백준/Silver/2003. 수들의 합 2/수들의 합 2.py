import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

# A[i] + ... A[j] = M
R, sum, ans = -1, 0, 0
for L in range(n):
    while R + 1 < n and sum < m:
        R += 1
        sum += a[R]
    
    if sum == m:
        ans += 1
    
    sum -= a[L]

print(ans)