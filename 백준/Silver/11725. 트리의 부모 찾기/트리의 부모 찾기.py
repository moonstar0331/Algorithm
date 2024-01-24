import sys
from collections import deque
input = sys.stdin.readline

# 입력
n = int(input())
adj = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n - 1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

# 루트 없는 트리
# 트리의 루트를 1이라고 정했을 때
# 각 노드의 부모를 구하기
visit = [0] * (n+1)
def bfs(x):
    queue = deque()
    queue.append(x)
    visit[x] = 1
    while queue:
        x = queue.popleft()
        for y in adj[x]:
            if visit[y]:
                continue
            visit[y] = 1
            parent[y] = x
            queue.append(y)
        
bfs(1)
for i in range(2, n + 1):
    print(parent[i])
