# 백준 10430 나머지
import sys
input = sys.stdin.readline

a, b, c = map(int,input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)