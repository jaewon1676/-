# 백준 2010 플러그
import sys
n = int(sys.stdin.readline())
sum = 0
for i in range(n):
    sum += int(sys.stdin.readline())
print(sum - (n - 1))