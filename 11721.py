# 열 개씩 끊어 출력하기


# a = BaekjoonOnlineJudge, d = 19
a = input()
d = len(a) 
for b in range(0, d, 10):
    e = b + 10 # e = 10, e = 20
    print(a[b:e])