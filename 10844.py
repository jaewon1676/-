# 백준 10844 쉬운 계단 수
# 2차원 DP
import sys
input = sys.stdin.readline
N = int(input())
dp = [[0 for i in range(10)] for j in range(101)] # 2차원 DP

#첫 시행 초기화
for i in range(1,10):
    dp[1][i] = 1

#카운팅  0, 9,1~8 은 규칙이 다른것을 생각하자
for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N]) % 1000000000)