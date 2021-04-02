# 백준 10845 큐

import sys
input = sys.stdin.readline

n = int(input())             # 명령의 수
queue= []                    # 결과 보관

for i in range(n):
    s1 = input().split()         # 문자열 입력
    if s1[0] == "push":          # 큐에 정수를 넣는다.
        queue.insert(0, s1[1])   # 큐의 맨 앞자리에 s1[1] 삽입

    elif s1[0] == "pop":         # 큐에서 가장 앞에있는 정수를 뺌
        if len(queue) != 0:
            print(queue.pop())   
        else:
            print(-1)

    elif s1[0] == "size":        # 큐에 들어있는 정수의 개수 출력
        print(len(queue))        # len 함수 사용

    elif s1[0] == "empty":       # 큐가 비어있으면 1 아니면 0 출력
        if len(queue) == 0:      # len 함수 사용
            print(1)              
        else : print(0)

    elif s1[0] == "front":      # 큐의 가장 앞에 있는 정수 출력
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[len(queue) -1])

    elif s1[0] == "back":       # 큐의 가장 뒤에 있는 정수 출력
        if len(queue) == 0:     # 처음에 입력한 수 
            print(-1)
        else: 
            print(queue[0])      