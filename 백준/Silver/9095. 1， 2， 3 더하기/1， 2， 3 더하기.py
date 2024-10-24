import heapq
import sys
si = sys.stdin.readline

dy = [0] * 12
dy[1], dy[2], dy[3] = 1, 2, 4

for i in range(4, 12):
    dy[i] = dy[i - 1] + dy[i - 2] + dy[i - 3]
    
T = int(si())
for _ in range(T):
    print(dy[int(si())])