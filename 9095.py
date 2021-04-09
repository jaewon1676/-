# 백준 9095 1, 2, 3 더하기
# DP, 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 정수 n이 주어진다. n은 양수이며 11보다 작다.
import sys
input = sys.stdin.readline

dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# for _ in range(4,12): 
#    dp.append(sum(dp[-3:]))

n = int(input())
for _ in range(n):
    input_n = int(input())
    print(dp[input_n])
# for _ in range(int(input())): 
#    print(dp[int(input())])