import sys
input = sys.stdin.readline

# 입력
n = int(input())
a = []

for i in range(n):
    a.append(input().strip())

# 알파벳 소문자로 이루어진 N개의 단어
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 중복된 단어는 하나만 남기고 제거

a.sort(key = lambda x: ((len(x), x)))

for i in range(n):
    if i == 0 or a[i] != a[i-1]:
        print(a[i])