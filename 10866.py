# 백준 10866 덱
from collections import deque 
import sys
input = sys.stdin.readline

n = int(input())        # 수 입력
deque = deque()         # 덱 구현

for i in range(n):
    deque_input = list(input().split())
    #  덱은 앞과 뒤에서 push와 pop이 가능하다.
    #  front □□□□□□□□□ back
    if deque_input[0] == 'push_front':   # 정수 X를 덱의 앞자리에 넣는다.
        deque.appendleft(deque_input[1])

    elif deque_input[0] == 'push_back':  # 정수 X를 덱의 뒤에 넣는다.
        deque.append(deque_input[1])

    elif deque_input[0] == 'pop_front': # 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력
        if len(deque) == 0:
            print("-1")
        else:
            tmp = deque.popleft()
            print(tmp)

    elif deque_input[0] == 'pop_back': # 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력
        if len(deque) == 0:
            print("-1")
        else:
            tmp = deque.pop()
            print(tmp)

    elif deque_input[0] == 'size': # 덱에 들어있는 정수의 개수를 출력
        print(len(deque))

    elif deque_input[0] == 'empty': # 덱이 비어있으면 1을, 아니면 0을 출력
        if len(deque) == 0:
            print("1")
        else:
            print("0")
    elif deque_input[0] == 'front': # 덱의 가장 앞에 있는 정수를 출력
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[0])

    elif deque_input[0] == 'back': # 덱의 가장 뒤에 있는 정수를 출력
        if len(deque) == 0:
            print("-1")
        else:
            print(deque[len(deque)-1])

