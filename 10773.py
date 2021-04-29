# 백준 10773 제로
import sys
input = sys.stdin.readline
n = int(input())
n_list = []

for i in range(n):
    num = int(input())
    if num == 0:    # 0을 받으면 최근의 수를 지우고
        n_list.pop()
    else:           # 아닐 경우에는 해당 수를 쓴다.
        n_list.append(num)
print(sum(n_list))
