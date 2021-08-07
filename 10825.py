# 국영수

import sys
input = sys.stdin.readline

n = int(input())
n_list = []
for i in range(n):
    m = input().split()
    n_list.append(m)

# 국어점수 내림차순, 영어점수 오름차순, 수학점수 내림차순, 영어 이름 오름차순
n_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in n_list:
    print(i[0], end='\n')