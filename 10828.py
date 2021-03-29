# 백준 10828 스택
import sys
# 정수 x를 스택에 넣는 연산.
def push(x):
    stack.append(x)
# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()
# 스택에 들어있는 정수의 개수를 출력한다.
def size():
    return len(stack)
# 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    return 0 if stack else 1
# 스택의 가장 위에 있는 정수를 출력한다.
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    return stack[-1] if stack else -1
    
# 시작
N = int(sys.stdin.readline()) # 명령의 수 N에 저장
stack = []                    # stack 변수에 명령 저장

for _ in range(N): # N회 입벽
    input = sys.stdin.readline()
    input_split = input.split()
    
    order = input_split[0]
    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())