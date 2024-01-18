import sys
input = sys.stdin.readline

# 입력
L, C = map(int, input().split(' '))
A = sorted(input().strip().split(' '))

used = [0] * C
selected = [0] * L

# 암호는 서로 다른 L개의 알파벳 소문자로 구성
# 최소 한 개의 모음(a, e, i, o u)
# 최소 두 개의 자음
# 알파벳이 암호에서 증가하는 순서

def is_vowel(x: str):
    return x in "aeiou"

def rec_func(k):
    if k == L:
        vowel, consonant = 0, 0
        for x in selected:
            if is_vowel(A[x]):
                vowel += 1
            else:
                consonant += 1
        if (vowel >= 1) and (consonant >= 2):
            for x in selected:
                print(A[x], end='')
            print()
    else:
        st = -1 if k == 0 else selected[k-1]
        for i in range(st+1, C):
            selected[k] = i
            rec_func(k+1)
            selected[k] = 0

rec_func(0)