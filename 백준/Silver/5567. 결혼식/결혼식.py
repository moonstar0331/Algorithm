import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

dist = [-1] * (n + 1)

def bfs(x):
    queue = deque()
    queue.append(x)
    dist[x] = 0

    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if dist[y] != -1:
                continue
            dist[y] = dist[x] + 1
            queue.append(y)

bfs(1)
ans = 0
for i in range(2, n+1):
    if dist[i] == 1 or dist[i] == 2:
        ans += 1

print(ans)