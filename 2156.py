# 백준 2156 포도주 서식
# DP
import sys
input = sys.stdin.readline

n = int(input())    # 테스트케이스
w = [0]     
for i in range(n):  
    w.append(int(input())) # 포도주의 양
dp = [0]    
 
dp.append(w[1])
if n > 1:
    dp.append((w[1] + w[2]))

for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i]))
print(dp[n])