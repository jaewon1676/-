# 백준 1874 스택 수열

import sys
input = sys.stdin.readline

n = int(input())   # 첫 줄 입력
stack = []         # 숫자 저장
result = []        # +, - 연산을 저장
count = 0
X = True

for i in range(n):         # n만큼 반복
    num = int(input())     # 

    while count < num:     
        count += 1
        stack.append(count)
        result.append("+") 

    if stack[-1] == num:   
        stack.pop()        
        result.append("-") 
    else:
        X = False          
        break

if X == False:
    print("NO")
else:
    for i in result:
        print(i)