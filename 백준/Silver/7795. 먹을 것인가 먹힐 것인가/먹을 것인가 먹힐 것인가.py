import sys
input = sys.stdin.readline

# A[L..R]에서 X 미만의 수(X 보다 작은 수) 중 제일 오른쪽 인덱스를 return 하는 함수
def lower_bound(a, l, r, x):
    res = l -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] < x:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res

def solve():
    b.sort()
    ans = 0
    for x in a:
        ans += lower_bound(b, 0, m - 1, x) + 1
    print(ans)

TT = int(input())
for _ in range(TT):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve()