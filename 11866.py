# 백준 11866 요세푸스 문제0
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = deque([])
for i in range(1, n+1):
    s.append(i)
print('<', end='')

while s:
    for i in range(k-1):
        s.append(s[0])
        s.popleft()

    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')