# 백준 1932 정수 삼각형
# DP

import sys
input = sys.stdin.readline
n = int(input())

DP = [] # 배열 생성

for i in range(n):
    DP.append(list(map(int, input().split())))
k = 2

for i in range(1, n):   # i = 1부터 n-1까지 for
    for j in range(k):  # j = 0부터 k-1까지 for
        if j == 0:
            DP[i][j] = DP[i][j] + DP[i-1][j]
        elif i == j:
            DP[i][j] = DP[i][j] + DP[i-1][j-1]
        else:
            DP[i][j] = DP[i][j] + max(DP[i-1][j-1], DP[i-1][j]) 
    k += 1 # 1행 증가 하면 1열씩 추가
print(max(DP[n-1]))