import sys
from collections import deque
input = sys.stdin.readline

# 입력
N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

# 가중치 없는 방향 그래프 G
# 모든 정점 (i, j)에 대해서
# i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하기

def bfs(x):
    visit = [0] * N
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for y in range(N):
            if not adj[x][y] or visit[y]:
                continue
            visit[y] = 1
            queue.append(y)
    for i in range(N):
        print(visit[i], end=' ')
    print()

for i in range(N):
    bfs(i)