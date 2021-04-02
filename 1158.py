# 백준 1158 요세푸스 문제

import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 7, 3
people = list(range(1, n+1))     # 1 ~ 7 까지 리스트
result = []
i = k-1                          # i = 2

while True:
    result.append(people.pop(i)) # 1번째 (2) = 3
    if not people:            # people 비어있으면 종료
        break
    i  = (i+k-1) % len(people)  
    # 2번째 4 % 6 = (4) = 6, 3번째 6 % 5 = (1) = 2
    # 4번째 3 % 4 = (3) = 7, 5번째 5 % 3 = (2) = 5
    # 6번째 4 % 2 = (0) = 1, 6번째 2 % 1 = (0) = 4
    print(result)


print('<'+', '.join(map(str,result)) + '>')

