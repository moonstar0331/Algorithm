import sys
input = sys.stdin.readline

# 입력
N = int(input())
M = int(input())
X = list(map(int, input().split()))

# 가로등을 설치할 개수 M
# 각 가로등의 위치 x 들의 결정
# 각 가로등은 높이만큼 주위를 비출 수 있다
# 최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다
# 최소한의 예산이 들 높이를 구하자
# 단, 가로등의 높이는 모두 같아야 한다.
# 가로등의 높이가 H라면, 왼쪽으로 H, 오른쪽으로 H만큼 비춘다
# 가로등의 위치는 오름차순

def determination(height):
    last = 0
    for x in X:
        if x - last <= height:
            last = x + height
        else:
            return False
    return last >= N

l, r, ans = 0, N, N
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)