# 입력
N, M = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

# 이차원 누적합 구하기
psum = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i==0 and j==0:
            psum[i][j] = a[i][j]
        elif i==0 and j!=0:
            psum[i][j] = a[i][j] + psum[i][j-1]
        elif i!=0 and j==0:
            psum[i][j] = a[i][j] + psum[i-1][j]
        else:
            psum[i][j] = a[i][j] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1]

K = int(input())
for i in range(K):
    a, b, c, d = map(int, input().split())

    if a==1 and b==1:
        print(psum[c-1][d-1])
    elif a==1 and b!=1:
        print(psum[c-1][d-1] - psum[c-1][b-2])
    elif a!=1 and b==1:
        print(psum[c-1][d-1] - psum[a-2][d-1])
    else:
        print(psum[c-1][d-1] - psum[c-1][b-2] - psum[a-2][d-1] + psum[a-2][b-2])