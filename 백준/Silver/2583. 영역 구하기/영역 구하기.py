import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
a = [[0] * n for _ in range(m)]

# y 행, x 열
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            a[i][j] += 1

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = []

def bfs(i, j):
    cnt = 1
    queue = deque()
    a[i][j] += 1
    queue.append((i, j))

    while queue:
        y, x = queue.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if a[ny][nx] != 0:
                continue
            a[ny][nx] += 1
            cnt += 1
            queue.append((ny, nx))

    ans.append(cnt)

count = 0
for i in range(m):
    for j in range(n):
        if a[i][j] == 0:
            count += 1
            bfs(i, j)

print(count)
ans.sort()
for x in ans:
    print(x, end=' ')