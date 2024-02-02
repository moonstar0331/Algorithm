import sys
input = sys.stdin.readline

n, K = map(int, input().split())
a = input().split()

R, ans, cnt = -1, -1, 0

# 라이언 1, 어피치 2
# 라이언 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기

for L in range(n):
    while R + 1 < n and cnt < K:
        R += 1
        if a[R] == '1':
            cnt += 1
    
    if cnt == K:
        if ans == -1:
            ans = R - L + 1
        ans = min(ans, R - L + 1)
    
    if a[L] == '1':
        cnt -= 1

print(ans)