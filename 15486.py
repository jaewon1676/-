# 백준 15486 퇴사 2
import sys
input = sys.stdin.readline

n = int(input()) # 전체 상담일
t = [] # 상담이 걸리는 기간
p = [] # 상담 후 받는 금액
dp = [0] * (n+1) # 금액의 합계
for i in range(n):
    a, b = map(int,input().split())
    t.append(a)
    p.append(b)

for i in range(n): 
    if t[i] <= n - i: # 상담에 걸리는 시간보다 전체 상담일 - i가 같거나 클 경우
        dp[i+t[i]] = max(dp[i+t[i]], dp[i]+p[i])
    dp[i+1] = max(dp[i+1], dp[i])

print(dp[n])