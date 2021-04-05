# 백준 9095 1, 2, 3 더하기
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline
input_list = []
n = int(input())               # 정수 n 입력

for i in range(n):
    input_list.append(int(input()))        

dp = [1, 2, 4]   # 타일 초기화 및 생성

for i in range(3, max(input_list)):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

for i in input_list:
    print(dp[i-1])