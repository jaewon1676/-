# 백준 1010 다리 놓기
# mCn 조합
import sys
t = int(input())

for _ in range(t):
    m, n = map(int, input().split()) # 1 5
    answer = 1
    k = n  - m # 4
    while n > k:
        answer *= n
        n -= 1
    while m > 1:
        answer = answer // m
        m -= 1
    
    print(answer)