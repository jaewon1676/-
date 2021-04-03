# 백준 10799 쇠막대기
# 스택
bar = list(input())              
answer = 0
stack = []

for i in range(len(bar)):
    if bar[i] == '(':            # 스택 쌓기
        stack.append('(')
    else:    
        if bar[i-1] == '(':      # ()라면 (를 pop하고 현재 스택에 
            stack.pop()          # 들어있는 ( 수만큼 값을 더해준다.
            answer += len(stack) 
        else:
            stack.pop() 
            answer += 1          #끝머리 막대기 부분을 더해준다

print(answer)