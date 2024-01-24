import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(x, y):
    visit[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[nx][ny]:
            continue
        if a[nx][ny] == 0:
            continue
        dfs(nx, ny)

T = int(input())
while T:
    T -= 1
    m, n, K = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    for i in range(K):
        y, x = map(int, input().split())
        a[x][y] = 1

    visit = [[False] * m for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 or visit[i][j]:
                continue
            ans += 1
            dfs(i, j)

    print(ans)