# 백준 11660 구간 합 구하기 5
# DP

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Matrix = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열에 수 입력
DP = [[0] * (N + 1) for _ in range(N + 1)] # 값을 저장할 0만 있는 2차원 배열

for i in range(1, N + 1):
    for j in range(1, N + 1):
        DP[i][j] = Matrix[i-1][j-1] + DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1])
