import sys
input = sys.stdin.readline

# . - 빈 필드, # - 울타리, o - 양, v - 늑대
# 탈출할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주
# 영역 안의 양의 수가 늑대의 수보다 많으면 이기고, 늑대를 우리에서 쫒아냄
# 그렇지 않으면 늑대가 그 지역 안의 모든 양을 먹는다

n, m = map(int, input().split())
a = [input().strip() for _ in range(n)]
sys.setrecursionlimit(100000)

visit = [[False] * m for _ in range(n)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
totalSheep, totalWolf, sheep, wolf = 0, 0, 0, 0

def dfs(x, y):
    global sheep, wolf
    if a[x][y] == 'o':
        sheep += 1
    if a[x][y] == 'v':
        wolf += 1
    visit[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visit[nx][ny]:
            continue
        if a[nx][ny] == '#':
            continue
        dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if a[i][j] != '#' and not visit[i][j]:
            sheep, wolf = 0, 0
            dfs(i, j)
            if sheep > wolf:
                totalSheep += sheep
            else:
                totalWolf += wolf
                
print(totalSheep, totalWolf)