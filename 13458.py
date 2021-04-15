#백준 13458 시험감독
#수학
import sys
input = sys.stdin.readline
n = int(input())
# 응시자의 수를 리스트 형식으로 여러개 입력받음
a = list(map(int, input().split()))
# 감독관이 감시 할 수 있는 수를 입력받음
b, c = map(int, input().split())
count = 0

for i in range(n): 
    if a[i] > 0:  # 총 감독관 1명이 감독할 수 있는 학생 수를 뺀다.
        a[i] -= b
        count += 1
    if a[i] > 0:   # 나머지는 부 감독관이 감독할 수 있는 
        count += int(a[i]/c) # 학생 수를 모두 뺀다.
        if a[i] % c != 0:
            count += 1
    
print(count)