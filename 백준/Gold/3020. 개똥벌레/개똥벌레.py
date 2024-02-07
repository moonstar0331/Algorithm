import sys
input = sys.stdin.readline

# 입력
n, h = map(int, input().split())
h_arr, l_arr = [], []

for i in range(n):
    t = int(input())
    if i % 2 == 0:
        l_arr.append(t)
    else:
        h_arr.append(t)

l_arr.sort()
h_arr.sort()

# 높이가 h일 때, 부딪히는 장애물의 개수 체크
def check(height, cave):
    l, r = 0, len(cave) - 1
    while l <= r:
        mid = (l + r) // 2
        if cave[mid] <= height:
            l = mid + 1
        else:
            r = mid - 1
    return len(cave) - (r + 1)

ans, ans_cnt = sys.maxsize, 0

# 모든 높이 탐색
for i in range(1, h + 1):
    l_cnt = check(i - 1, l_arr)
    h_cnt = check(h - i, h_arr)
    cur_cnt = l_cnt + h_cnt

    if cur_cnt < ans:
        ans = cur_cnt
        ans_cnt = 1
    elif cur_cnt == ans:
        ans_cnt += 1
    else:
        pass

print(ans, ans_cnt)