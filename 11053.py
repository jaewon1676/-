# 백준 11053 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d=[1] * n

for i in range(1,n):
  for j in range(i):         
    if a[j] < a[i]:            
      d[i] = max(d[i],d[j]+1)

print(max(d))