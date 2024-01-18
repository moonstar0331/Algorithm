import sys
input = sys.stdin.readline

# 입력
n = int(input())
ext = []

for _ in range(n):
    ext.append(input().strip().split('.')[1])

# 힌트는 확장자
# 확장자 별로 정리해서 몇 개씩 있는지
# 보기 편하게 확장자들을 사전 순으로 정렬
ext.sort()

i = 0
while i < n:
    cnt = 1
    for j in range(i + 1, n):
        if ext[j] == ext[i]:
            cnt += 1
            i += 1
        else:
            break
    print(ext[i], cnt)
    i += 1
