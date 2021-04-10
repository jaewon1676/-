# 백준 5585 거스름돈
import sys
input = sys.stdin.readline

n = 1000 - int(input()) # 1000원 - 입력한 
count = 0
array = [500, 100, 50, 10, 5, 1]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)