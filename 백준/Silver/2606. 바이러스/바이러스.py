import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

ans = 0

def dfs(x):
    global ans
    visit[x] = True
    for y in adj[x]:
        if visit[y] == True:
            continue
        ans += 1
        dfs(y)

dfs(1)
print(ans)