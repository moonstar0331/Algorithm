import sys

# 입력
N, M = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(M)]
used = [0 for _ in range(N+1)]

# 재귀함수
def rec_func(k):
    if k == M:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        for cand in range(1, N+1):
            if used[cand]:
                continue
            selected[k] = cand
            used[cand] = 1
            rec_func(k+1)
            selected[k] = 0
            used[cand] = 0

rec_func(0)