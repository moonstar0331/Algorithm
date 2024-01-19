import sys
input = sys.stdin.readline

# 입력
n = int(input())
a = input().strip()
cnt = [0] * 30
kind = 0

def add(x):
    global kind
    t = ord(x) - ord('a')
    cnt[t] += 1
    if cnt[t] == 1:
        kind += 1
    
def erase(x):
    global kind
    t = ord(x) - ord('a')
    cnt[t] -= 1
    if cnt[t] == 0:
        kind -= 1

L = 0
ans = 0
for R in range(len(a)):
    add(a[R])
    while kind > n:
        erase(a[L])
        L += 1
    ans = max(ans, R-L+1)

print(ans)