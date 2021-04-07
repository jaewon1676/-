# 백준 1912 연속합
# DP.
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(n-1): # 0부터 n-1까지 반복
    sum.append(max(sum[i] + a[i+1], a[i+1]))
                  #sum[0] + a[1],   a[1] 중 큰 걸 sum 뒤에 추가
                  #sum[1] + a[2],   a[2] 중 큰 걸 sum 뒤에 추가
                  #sum[2] + a[3],   a[3] 중 큰 걸 sum 뒤에 추가
print(max(sum))