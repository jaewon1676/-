# 백준 1309 동물원
import sys
input = sys.stdin.readline

n = int(input())
p = [[0] * 3 for _ in range(100001)] # 2차원 배열

for i in range(3):
    p[1][i] = 1  

for i in range(2, 100001):
    p[i][0] = p[i - 1][1] + p[i - 1][2] % 9901 # p[n][0]의 경우는 맨 위의 두칸 중 사자가 왼쪽에 있을 
    p[i][1] = p[i - 1][0] + p[i - 1][2] % 9901 # p[n][1]의 경우는 맨 위의 두칸 중 사자가 오른쪽에 있을 
    p[i][2] = p[i - 1][0] + p[i - 1][1] + p[i - 1][2] % 9901 # p[n][0]의 경우는 맨 위의 두칸 중 어느 곳에도 있지 않는 경우
print(sum(p[n]) % 9901)
