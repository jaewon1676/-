#백준 11000 강의실 배정
#자료구조, 그리디, 정렬, 우선순위 큐
import heapq #보통리스트를 힙처럼 다루는 모듈
import sys
input = sys.stdin.readline
n = int(input())
c = [] # 수업 시간을 입력받는 리스트
h = [] # 수업하는 강의실을 저장하는 리스트
# n만큼 리스트 c에 정수를 추가한다.
for i in range(n):
    c.append(list(map(int, input().split())))
#람다함수 사용, 수업을 시간하는 시간을 기준으로 정렬한다.
#x[0] = 수업을 시간하는 시간 기준으로 정렬
#x[1] = 수업 끝나는 시간 기준으로 정렬
c = sorted(c, key = lambda x: x[0])

for i in range(n):
    #리스트 h가 비어있지 않고 리스트 h의 저장된 끝나는시간
    if len(h) != 0 and h[0]<= c[i][0]: 
        # 리스트 h[0] 값을 빼준다.
        heapq.heappop(h)
    #리스트 h에 c[i][1]값을 넣는다.
    heapq.heappush(h,c[i][1])
print(len(h))