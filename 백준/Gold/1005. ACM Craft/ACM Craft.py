import sys
from collections import deque
si = sys.stdin.readline

Q = int(si())
for _ in range(Q):
    n, m = map(int, si().split())
    T = [0] + list(map(int, si().split()))
    T_done = [0] * (n + 1)
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
            T_done[i] = T[i]
            
    while Q:
        x = Q.popleft()
        for y in con[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                Q.append(y)
            T_done[y] = max(T_done[y], T_done[x] + T[y])
    W = int(si())
    print(T_done[W])