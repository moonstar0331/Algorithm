import sys
input = sys.stdin.readline

# 사과 1개 | 장애물 | 빈칸
# 상하좌우
# 지나가면 장애물로 됨
# 사과 3개를 먹는 최소 이동 횟수 -> 먹을 수 없으면 -1
# 1: 사과, 0: 빈칸, -1: 장애물
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# 입력
a = [[0] * 5 for _ in range(5)]
for i in range(5):
    a[i] = list(map(int, input().split()))
r, c = map(int, input().split())

ans = -1
def dfs(x, y, apple_cnt, cnt):
    global ans
    if apple_cnt == 3:
        if ans == -1:
            ans = cnt
            return
        else:
            ans = min(ans, cnt)
            return
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx > 4 or ny > 4:
            continue
        if a[nx][ny] == -1:
            continue
        
        if a[nx][ny] == 1:
            a[nx][ny] = -1
            dfs(nx, ny, apple_cnt+1, cnt+1)
            a[nx][ny] = 1
        elif a[nx][ny] == 0:
            a[nx][ny] = -1
            dfs(nx, ny, apple_cnt, cnt+1)
            a[nx][ny] = 0
    
if a[r][c] == 1:
    a[r][c] = -1
    dfs(r, c, 1, 0)
else:
    a[r][c] = -1
    dfs(r, c, 0, 0)
print(ans)