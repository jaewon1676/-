# 백준 11727 2*n 타일링 2
# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline
# n  m
# 1  1
# 2  3
# 3  5
# 4 11
# 5 21
# dp[i] = dp[i-1] + (dp[i-2]*2)

# 직사각형 길이 입력
n = int(input())
# 타일 초기화, 생성
dp = [0 for _ in range(n+1)]

# n이 0, 1, 2인 경우에는 따로 출력해준다.
if n <= 1:
    print(n)
elif n == 2:
    print(n+1)
else:
    dp[1] = 1
    dp[2] = 3
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    print(dp[n] % 10007)