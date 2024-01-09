def solution(a, b):
    answer = 0
    A = str(a) + str(b)
    B = str(b) + str(a)
    if int(A) >= int(B):
        answer = int(A)
    else:
        answer = int(B)
    return answer