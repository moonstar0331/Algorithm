import sys
input = sys.stdin.readline

# 입력
K, N = map(int, input().split())
A = []
for _ in range(K):
    A.append(int(input()))

# 이미 K개의 랜선 - K개의 랜선 길이 제각각
# N개의 같은 길이의 랜선으로 만들길 원함
# K개의 랜선을 잘라서 만들어야 함
# 최대 랜선의 길이
# 매개변수 탐색
    
def determination(x):
    cnt = 0
    for num in A:
        cnt += (num // x)
    
    return cnt >= N

l, r, ans = 1, max(A), 0
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
    
print(ans)