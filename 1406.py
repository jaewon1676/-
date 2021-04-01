# 백준 1406 에디터
# L = 왼쪽으로 한 칸 옮김     D = 오른쪽으로 한 칸 옮김
# B = 왼쪽에 있는 문자 삭제 P $ = $라는 문자를 커서 왼쪽에 추가함

import sys
input = sys.stdin.readline
s1 = list(input().strip()) # 문자열 입력, strip()으로 문자열 조합 제거
s2 = []                    # 스택2
m = int(input())           # 입력 할 명령어 개수

for i in range(m):         # m만큼 입력받는다
    com = input().strip() 
    if com[0] == "P":
        s1.append(com[2])    # com[1]은 띄어쓰기니까 com[2] append
    elif com[0] == "L" and s1 != []:
        s2.append(s1.pop())  # s1에서 pop 하고 s2로 옮김
    elif com[0] == "D" and s2 != []:
        s1.append(s2.pop())  # s2에서 pop 하고 s1로 옮김
    elif com[0] == "B" and s1 != []:
        s1.pop()
print("".join(s1 + list(reversed(s2))))