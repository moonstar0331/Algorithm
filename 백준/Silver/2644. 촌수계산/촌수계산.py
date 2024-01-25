import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
st, ed = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

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

bfs(st)
print(dist[ed])