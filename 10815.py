# 숫자 카드

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dict1 = {m_list[i]: 0 for i in range(len(m_list))}

for i in range(n):
    if n_list[i] in dict1.keys(): 
        dict1[n_list[i]] += 1
print(" ".join(map(str, list(dict1.values()))))