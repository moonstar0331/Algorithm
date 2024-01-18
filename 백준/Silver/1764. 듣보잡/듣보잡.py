import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
a = sorted([input() for _ in range(n)])
b = sorted([input() for _ in range(n)])

def bin_search(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False

ans = [x for x in b if bin_search(a, 0, n-1, x)]
print(len(ans))
for x in ans:
    print(x, end="")