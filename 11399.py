#백준 11399 ATM
#그리디 알고리즘
import sys
input = sys.stdin.readline
#인원수를 입력받는다.
n = int(input())
#걸리는 시간을 입력받을 리스트 초기화,
#list 형식으로 여러번 입력받음, 오름차순 정렬
time = list(map(int, input().split()))
time.sort()
#걸리는 시간의 합계를 저장할 변수 초기화
sum = 0
for i in range(n):  # 이중 for문을 써서 1, 1+2, 1+2+3
    for j in range(i+1): # 형식으로 계속 더해준다
        sum += time[j]
print(sum)