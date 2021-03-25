# 백준 11653 소인수분해
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

n = int(input())
i = 2

while n != 1 :
    if n%i == 0:
        n = n//i
        print(i)
    else:
        i+=1
