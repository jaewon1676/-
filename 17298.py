# 백준 17298 오큰수
# 자료구조, 스택
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1 for _ in range(n)]

for i in range(len(arr)): # arr에 입력받은 수만큼 반복
    while stack and arr[stack[-1]] < arr[i]: 
    # stack이 들어있고 arr[스택 맨 뒤]가 arr[i]보다 작으면 반복
        answer[stack.pop()] = arr[i] 
        # answer의 stack.pop한 자리에 arr[i] 추가
    stack.append(i) # stack에 i 추가
print(*answer) # 앞에 *를 붙여 원소만 나열