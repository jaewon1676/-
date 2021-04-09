# 백준 14720 우유 축제
import sys
input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))
count = 0
for i in range(n):
    if c[i] == count % 3:
        count += 1

print(count)