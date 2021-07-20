# 백준 1931 회의실 배정
# 그리디

import sys
input = sys.stdin.readline

n = int(input()) # n개의 회의
s = [] # 배열
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

# 배열속 수 람다함수로 정렬
s = sorted(s, key=lambda a:a[0]) # 0열(회의 시작시간) 기준으로 오름차순정렬
s = sorted(s, key=lambda a:a[1]) # 1열(회의 종료시간) 기준으로 오름차순정렬

last = 0 # 회의 끝나는 시간
cnt = 0 # 회의 횟수
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)