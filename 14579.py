# 백준 14579 덧셈과 곱셈
import sys
input = sys.stdin.readline
a,b = map(int,input().strip().split())
result = 1
for i in range(a,b+1):
    result*=(i*(i+1)//2)
print(result%14579)
