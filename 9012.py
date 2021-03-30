# 백준 9012 괄호
import sys
input = sys.stdin.readline

t = int(input()) # 테스트케이스

for _ in range(t):
    stack = []
    vps = input()
    check = 0
    for c in vps:
        if c == '(':
            stack.append(c)
        elif c ==')':
            if len(stack) == 0:
                print('NO')
                check = 1
                break
            else:
                stack.pop(-1)
    if len(stack) != 0 and check == 0: 
        print('NO') 
    elif len(stack) == 0 and check == 0: 
        print('YES')
