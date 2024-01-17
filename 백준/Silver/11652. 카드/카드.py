import sys

# 입력
n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

# 정렬
a.sort()

mode = a[0] # 최빈값
modeCnt = 1 # 최빈값 개수
curCnt = 1 # 현재 보고 있는 수의 개수

for i in range(1, n):
    if a[i] == a[i-1]:
        curCnt += 1
    else:
        curCnt = 1
    if modeCnt < curCnt:
        modeCnt = curCnt
        mode = a[i]

print(mode)