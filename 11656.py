# 접미사 배열

n = str(input())
n_list = []

for _ in n:
    n_list.append(n)
    n = n[1:]

for i in sorted(n_list):
    print(i)