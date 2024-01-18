import sys
input = sys.stdin.readline

# 입력
n = int(input())
A = sorted(list(map(int, input().split(' '))))

M = int(input())
B = list(map(int, input().split(' ')))

# 배열 B에 있는 원소들을 몇 개씩 가지고 있는지 출력
def lower_bound(a, l, r, x):
    res = r + 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            res = mid
            r = mid -1
        else:
            l = mid + 1
    return res

def upper_bound(a, l, r, x):
    res = r + 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

for x in B:
    print(upper_bound(A, 0, n-1, x) - lower_bound(A, 0, n-1, x), end=' ')
