# 백준 2164 카드2
# 큐
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque() # 큐

# queue에 1부터 n까지의 숫자를 입력받는다.
for i in range(n):
    queue.append(i+1) 

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())