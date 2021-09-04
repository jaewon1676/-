# 일곱 난쟁이

import sys
input = sys.stdin.readline

list = [int(input()) for i in range(9)] # 아홉 난쟁이 키 입력
total = sum(list) # 아홉 난쟁이의 키 총합 저장

for i in range(9):
    for j in range(i+1, 9):
        if 100 == total - (list[i] + list[j]):
            num1, num2 = list[i], list[j]

            list.remove(num1)
            list.remove(num2)
            list.sort()

            for i in range(len(list)):
                print(list[i])
            break
    if len(list)<9:
        break