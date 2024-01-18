import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split(' '))
nums = sorted(list(map(int, input().split(' '))))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]

# N개의 자연수 중에서 M개를 고른 수열
# 중복되는 수열 X
# 수열은 사전 순으로 증가하는 순서로 출력
def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        last_cand = 0
        for cand in range(n):
            if used[cand] == 1 or nums[cand] == last_cand:
                continue
            last_cand = nums[cand]

            selected[k] = nums[cand]
            used[cand] = 1

            rec_func(k+1)

            selected[k] = 0
            used[cand] = 0

rec_func(0)