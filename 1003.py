# 백준 1003 피보나치 함수
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    zero, one, tmp = 1, 0, 0
# n : 0 1 2 3 4 5 6
# 0 : 1 0 1 1 2 3 5
# 1 : 0 1 1 2 3 5 8
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)

