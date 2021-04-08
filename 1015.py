# 백준 1015 수열 정렬
# B[P[0]] = A[0] -> B[1] = 2
# B[P[1]] = A[1] -> B[2] = 3
# B[P[2]] = A[2] -> B[0] = 1
import sys
input = sys.stdin.readline

N = int(input())                    # 3
A = list(map(int, input().split())) # A[2 3 1]

P = [-1] * N        # A와 같은 길이의 P 생성
idx = 0

for i in range(N):
    min_idx = A.index(min(A))   # 수열 A에서 가장 작은 수의 인덱스(위치)를 구한다
    A[min_idx] = 1001           # 수열 A에서 가장 작은 수를 가장 큰 수로 치환
    P[min_idx] = idx            # 위에서 구한 인덱스에 0부터 넣어줌
    idx += 1
print(*P)
