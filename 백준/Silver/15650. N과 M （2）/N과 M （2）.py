import sys

# 입력
N, M = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(M)]

# 재귀함수
def rec_func(k):
    if k == M:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        start = 1 if k == 0 else selected[k-1]+1
        for cand in range(start, N+1):
            selected[k] = cand
            rec_func(k+1)
            selected[k] = 0

rec_func(0)