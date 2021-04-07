# 백준 1934 최소공배수
import sys
input = sys.stdin.readline

def gcd(a, b):  # 최대공약수
    return gcd(b, a % b) if b else a
def lcm(a, b):  # 최소공배수
    return a * b // gcd(a, b)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
