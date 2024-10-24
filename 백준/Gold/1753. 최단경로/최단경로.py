import heapq
import sys
si = sys.stdin.readline

n, m = map(int, si().split())
start = int(si())
con = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, weight = map(int, si().split())
    con[u].append((v, weight))
    
dist = [20001 * 10] * (n + 1)
dist[start] = 0

Q = []
heapq.heappush(Q, (0, start))

while Q:
    dist_x, x = heapq.heappop(Q)
    
    if dist[x] != dist_x: continue
    
    for u, weight in con[x]:
        if dist[u] > dist[x] + weight:
            dist[u] = dist[x] + weight
            heapq.heappush(Q, (dist[u], u))
            
for i in range(1, n + 1):
    if dist[i] != 20001 * 10:
        print(dist[i])
    else:
        print('INF')