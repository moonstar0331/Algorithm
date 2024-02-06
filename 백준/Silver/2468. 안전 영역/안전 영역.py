import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
a = []
max_height = 0
for _ in range(n):
    a.append(list(map(int, input().split())))
    max_height = max(max_height, max(a[-1]))

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(x, y, h):
    visit[x][y] = True

    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visit[nx][ny]:
            continue
        if a[nx][ny] <= h:
            continue
        dfs(nx, ny, h)

result = 0
for h in range(max_height):
    count = 0
    visit = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if a[x][y] > h and not visit[x][y]:
                dfs(x, y, h)
                count += 1

    result = max(result, count)

print(result)