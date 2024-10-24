import sys
si = sys.stdin.readline

n = int(si())
dy = [[0] * 10 for _ in range(n + 1)]

for num in range(10):
    dy[1][num] = 1
    
for len in range(2, n + 1):
    for num in range(10):
        for prev in range(num + 1):
            dy[len][num] += dy[len-1][prev]
            dy[len][num] %= 10007
            
print(sum(dy[n]) % 10007)