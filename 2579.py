# 백준 2579 계단 오르기
# DP
import sys
input = sys.stdin.readline
dp = [0 for _ in range(301)]
s = [0 for _ in range(301)]
# 계단의 점수 합을 구할 dp와, 계단의 점수 s
n = int(input())
for i in range(n):
    s[i] = int(input())
    # s[0] ~ s[n]까지에 계단의 점수 저장

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
#dp[2]까지는 점수 합을 미리 설정 해준다.
for i in range(3, n):    
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], 
                # 마지막 계단의 전 계단을 밟는 경우와
                dp[i - 2] + s[i])  
                # 마지막 계단의 전 계단을 밟지 않는 경우
print(dp[n - 1])