# 백준 1541 잃어버린 괄호
# 그리디

arr = input().split('-') # - 기준으로 자름
s = 0

for i in arr[0].split('+'):
    s += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)

