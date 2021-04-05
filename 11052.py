# 백준 11052 카드 구매하기
# dp, 점화식은 dp[i] = dp[i - k] + p[k]
# 카드를 i개 구매하는 최대 비용은 다음과 같다.
# p[1] + dp[i-1]
# p[2] + dp[i-2]
# p[3] + dp[i-3]
# . . . 
# p[i] + dp[0]
import sys
input = sys.stdin.readline

n = int(input())  # 4
# dp[i] = 카드 i개 구매하는 최대 가격, 
dp = [0 for _ in range(n+1)]              # dp[0, 0, 0, 0, 0] 
# p[k] = k개가 들어있는 카드팩 가격
p = [0] + list(map(int, input().split())) #  p[0, 1, 5, 6, 7]  

for i in range(1, n+1):                   # 1,2,3,4
    for k in range(1, i+1):               # 1,2,3,4
        dp[i] = max(dp[i], dp[i-k] + p[k])

print(dp[i])