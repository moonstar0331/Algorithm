import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline

n, m, R = map(int, input().split())
a = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)

cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

def dfs(s):
    global cnt
    visit[s] = cnt
    a[s].sort()
    for x in a[s]:
        if visit[x] == 0:
            cnt += 1
            dfs(x)

dfs(R)
for i in range(1, n + 1):
    print(visit[i])