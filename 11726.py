# 백준 11726 2*n 타일링
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

# 크기 n 입력
n = int(input())
# 타일 초기화, 생성
dp = [0 for _ in range(n+1)]

if n <= 3:
    print(n)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[i] % 10007)