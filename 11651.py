# 좌표 정렬하기 2

import sys
input = sys.stdin.readline

n = int(input())
m = []

for _ in range(n):
    a, b = map(int, input().split())
    m.append((a, b))

# y좌표 오름차순 우선정렬, x좌표 오름차순정렬
m.sort(key = lambda a:(a[1], a[0]))

for i in range(n):
    print(m[i][0], m[i][1])