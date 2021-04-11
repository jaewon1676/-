# 백준 10826 파보나치 수 4
# DP
import sys
input = sys.stdin.readline

p = [0, 1]
for i in range(2, 10001):
    p.append(p[i-1] + p[i-2])

n = int(input())
print(p[n])