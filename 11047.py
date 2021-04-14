# 백준 11047 동전 0
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
#동전을 입력받을 리스트 초기화, n만큼 입력, 내림차순 정렬
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

#동전개수 셀 변수 초기화
count = 0

for i in coin:
    if k == 0: break
    count += k // i 
    k %= i

print(count)