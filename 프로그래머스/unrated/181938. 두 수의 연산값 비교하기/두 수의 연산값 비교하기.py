def solution(a, b):
    answer = 0
    A = int(f"{a}{b}")
    B = 2 * a * b
    if A >= B:
        answer = A
    else:
        answer = B
    return answer