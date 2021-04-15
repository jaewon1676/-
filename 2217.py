#백준 2217 로프
#그리디
import sys
input = sys.stdin.readline
n = int(input())
#물체를 입력받을 리스트 초기화, n만큼 입력받고 내림차순 정렬
w = []
for _ in range(n):
    w.append(int(input()))
w.sort(reverse=True)
#가장무거운 질량은 로프를 1개 사용하고 
#다음으로 무거운 순으로 로프를하나씩 늘려간다
for i in range(n):
    w[i] = w[i] * (i + 1)
print(max(w))