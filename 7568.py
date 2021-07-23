# 덩치

n = int(input())
student_list = []

for _ in range(n):
    w, h = map(int, input().split())
    student_list.append((w, h))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')