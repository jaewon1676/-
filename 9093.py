# 백준 9093 단어 뒤집기
import sys
input = sys.stdin.readline

t = int(input()) # 입력 할 숫자 입력

for _ in range(t):
    n = list(map(str,input()))
    if n.count('(') == n.count(')'):
        print('YES')
    else:
        print('NO')
        