# 백준 9461 파도반 수열
# DP P[i] = P[i-2] + P[i-3]
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 케이스

DP = [0] * 101  # or [1 for i in range(T)]
DP[1] = 1   # DP[1 ~ 4]까지는 따로 선언해준다.
DP[2] = 1
DP[3] = 1
DP[4] = 2
for _ in range(T):
    N = int(input())
    for i in range(5, N+1):
        DP[i] = DP[i-2] + DP[i-3]
    print(DP[N])


