#백준 2501 약수 구하기

n, k = map(int,input().split())

num_list=[]

for i in range(1,n+1):
    if n%i==0:
        num_list.append(i)

if len(num_list)>=k:
    print(num_list[k-1])
else:
    print(0)


