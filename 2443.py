# 별 찍기 - 6

n = int(input())

for i in range(n, 0,-1):
    s = print(' ' * (n - i)+'*'* (i*2-1))