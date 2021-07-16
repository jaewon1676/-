import sys
input = sys.stdin.readline
n = int(input())

dp = []

for i in range(n):
    dp.append(list(map(int, input().split())))