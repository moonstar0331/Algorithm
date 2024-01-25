import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
a = []
for h in range(H):
    a.append([])
    for n in range(N):
        a[h].append(list(map(int, input().split())))

dist = [[[-1 for m in range(M)] for n in range(N)] for h in range(H)]

dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if a[h][n][m] == 1:
                dist[h][n][m] = 0
                queue.append((h, n, m))

while queue:
    h, n, m = queue.popleft()
    for dh, dn, dm in dir:
        nh, nn, nm = h + dh, n + dn, m + dm
        if nh < 0 or nn < 0 or nm < 0 or nh >= H or nn >= N or nm >= M:
            continue
        if dist[nh][nn][nm] != -1:
            continue
        if a[nh][nn][nm] == -1:
            continue
        queue.append((nh, nn, nm))
        dist[nh][nn][nm] = dist[h][n][m] + 1

ans = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if a[h][n][m] == -1:
                continue
            if dist[h][n][m] == -1:
                ans = -1
            if ans == -1:
                continue
            ans = max(ans, dist[h][n][m])

print(ans)