import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
a = []

# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 X
for i in range(n):
    a.append(list(map(int, input().split())))

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

queue = deque()
cnt = 0
status = True
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            queue.append((i, j, cnt))
        elif a[i][j] == 0:
            status = False

if status:
    cnt = 0
else:
    while queue:
        x, y, cnt = queue.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if a[nx][ny] == -1:
                continue
            if a[nx][ny] == 0:
                a[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))


for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            cnt = -1
            break

print(cnt)