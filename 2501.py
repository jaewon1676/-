# 백준 2501 약수 구하기
# 두 개의 자연수 N과 K가 주어졌을 때, 
# N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
n, k=map(int,input().split()) # int형으로 두 개 입력 받는다.
num_list=[]

for i in range(1,n+1):
    if n%i==0:             # n을 i로 나누어 나머지가 0이 되면
        num_list.append(i) # i를 추가

if len(num_list)>=k:
    print(num_list[k-1])
else:
    print(0)