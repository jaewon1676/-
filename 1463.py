# 백준 1463 1로 만들기
# DP, 점화식
# dp(N) = min ( dp(N//3) +1, dp(N//2)+1 , dp(N-1)+1 )
import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)] # 0이 들어있는 n개짜리 배열 생성

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1  

    if i%2 == 0 and dp[i] > dp[i//2] + 1 :
        dp[i] = dp[i//2] + 1
        
    if i%3 == 0 and dp[i] > dp[i//3] + 1 :
        dp[i] = dp[i//3] + 1
        
print(dp[n])