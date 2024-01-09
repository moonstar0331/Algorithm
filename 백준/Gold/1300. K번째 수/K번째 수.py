# 입력
n = int(input())
k = int(input())

# 문제에서 주어진 n x n 이차원 배열에서 x보다 작은 수의 개수를 구하여 반환하는 함수
def get_num_smaller(x: int) -> int:
    num_smaller = 0
    for i in range(1, n+1):
        # i 번째 행에서 x보다 작은 수의 개수는 min(n, (x-1)) // i) 개
        num_smaller += min(n, (x - 1) // i)
    return num_smaller

# 문제에서 주어진 n x n 이차원 배열에서 x보다 큰 수의 개수를 구하여 반환하는 함수
def get_num_bigger(x: int) -> int:
    num_bigger = 0
    for i in range(1, n+1):
        # i 번째 행에서 x보다 큰 수의 개수는 n - min(n, x // i) 개
        num_bigger += n - min(n, x // i)
    return num_bigger

# 이분 탐색을 수행하는 메인 로직
low  = 1
high = min(n*n, int(1e9))
answer = -1

while low <= high:
    mid = (low + high) // 2

    num_smaller = get_num_smaller(mid)
    num_bigger = get_num_bigger(mid)

    # mid 보다 작은 수가 너무 많으면 답은 low ~ mid-1 사이에 존재한다.
    if num_smaller > k - 1:
        high = mid - 1
    # mid 보다 큰 수가 너무 많으면 답은 mid+1 ~ high 사이에 존재한다.
    elif num_bigger > n*n-k:
        low = mid + 1
    # mid 보다 작은 수가 k-1개 이하이고 큰 수가 n-k개 이하이면 mid는 k번째 수이다.
    else:
        answer = mid
        break

print(answer)