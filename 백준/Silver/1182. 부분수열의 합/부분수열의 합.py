from itertools import combinations

# 입력
N, S = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for num_elements in range(1, N+1):
    for c in list(combinations(A, num_elements)):
        if sum(c) == S:
            ans += 1

print(ans)