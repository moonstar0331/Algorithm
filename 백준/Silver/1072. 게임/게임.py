import math
import sys
input = sys.stdin.readline

# 입력
x, y = map(int, input().split())
# z = math.floor((y / x) * 100)
z = (y * 100) // x

ans = -1
lt, rt = 1, 1000000001
while lt <= rt:
    mid = (lt + rt) // 2

    # if math.floor(((y + mid) / (x + mid)) * 100) > z:
    if ((y + mid) * 100) // (x + mid) > z:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)