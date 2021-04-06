# 백준 2193 이친수
# DP
import sys
input = sys.stdin.readline

n = int(input())   # 수 입력
dp = [0] * 91      # 1차원 배열 생성

dp[1] = 1
dp[2] = 1
for i in range(3, 91):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])