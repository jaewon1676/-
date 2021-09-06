# 숫자 카드 2

import sys
input = sys.stdin.readline

# m_list에 있는 리스트의 숫자가 n_list에 몇 개 있는지 검사.
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 딕셔너리 활용
dic = dict()

for i in n_list:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for i in m_list:
    try:
        print(dic[i], end =' ')
    except:
        print(0, end=' ')