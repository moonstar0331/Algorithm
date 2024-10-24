import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
con = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, si().split())
    con[x].append(y)
    indeg[y] += 1
    
Q = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        Q.append(i)
        
while Q:
    x = Q.popleft()
    print(x, end = ' ')
    for y in con[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            Q.append(y)